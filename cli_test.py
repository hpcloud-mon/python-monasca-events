# Copyright (c) 2015 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import time

from monasca_events import client as event_client
from monasca_events import ksclient

auth_url = "http://192.168.10.5:35357/v3/"
event_endpoint = "http://192.168.10.4:8082/v2.0"


def cli_client(username, password, auth_url, endpoint):
    kwargs = {
        'username': username,
        'password': password,
        'auth_url': auth_url
    }

    _ksclient = ksclient.KSClient(**kwargs)
    kwargs = {'token': _ksclient.token}
    api_version = '2_0'
    return event_client.Client(api_version, endpoint, **kwargs)


def test_stream_definition(c):
    print("Test POST /stream-definitions")

    # only one when checking notification-list
    action_id = "4b5bb51f-68bf-43f5-95aa-5005af3ffa26"

    fields = {
        "definition": {
            "fire_criteria": [{"event_type": "compute.instance.create.start"},
                              {"event_type": "compute.instance.create.end"}],
            "description": "provisioning duration",
            "name": str(time.time()),
            "group_by": ["instance_id"],
            "expiration": 3000,
            "select": [{"traits": {"tenant_id": "406904"},
                        "event_type": "compute.instance.create.*"}],
            "fire_actions": [action_id],
            "expire_actions": [action_id]
        }
    }

    response = c.stream_definitions.create(**fields)
    assert response.status_code == 201
    print("POST /stream-definitions success")

    print("Test GET /stream-definitions")

    response = c.stream_definitions.list()
    assert response[0]['fire_actions'][0] == action_id
    print("GET /stream-definitions success")

    print("Test DELETE /stream-definitions")
    response = c.stream_definitions.list()
    stream_id = str(response[0]['id'])
    fields ={
        'definition_id': stream_id
    }
    response = c.stream_definitions.delete(**fields)
    assert response.status_code == 204
    print("DELETE /stream-definitions success")


def test_event_transform(c):
    print("Test POST /transforms")
    fields = {
        "transform": {
            "name": 'func test',
            "description": 'a really short description of this thing',
            "specification": 'some sorta specification'
        }
    }
    response = c.transforms.create(**fields)
    assert response.status_code == 200
    print("POST /transforms success")

    print("Test GET /transforms")
    response = c.transforms.list()
    assert response[0]['name'] == 'func test'
    print("GET /transforms success")

    print("Test DELETE /transforms")
    response = c.transforms.list()
    transform_id = response[0]['tenant_id']
    fields = {
        "transform_id": transform_id
    }
    response = c.transforms.delete(**fields)
    assert response.status_code == 204
    print("DELETE /transforms success")


def main():
    c = cli_client('mini-mon', 'password', auth_url, event_endpoint)
    test_stream_definition(c)
    test_event_transform(c)

    return 0



if __name__ == "__main__":
    sys.exit(main())
