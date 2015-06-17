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

from monasca_events.common import monasca_manager
from monasca_events.openstack.common.apiclient import base




class Events(base.Resource):

    def __repr__(self):
        return "<Events %s>" % self._info


class EventsManager(monasca_manager.MonascaManager):
    resource_class = Events
    base_url = "/events"

    def get(self, **kwargs):
        """Get specific event."""
        url_str = self.base_url + "/%s" % kwargs['event_id']
        newheaders = self.get_headers()
        resp, body = self.client.json_request('GET', url_str,
                                              headers=newheaders)
        return body

    def list(self, **kwargs):
        """Get a list of events."""
        url_str = self.base_url
        newheaders = self.get_headers()
        resp, body = self.client.json_request('GET', url_str,
                                              headers=newheaders)
        return body


class Transforms(base.Resource):

    def __repr__(self):
        return "<Transforms %s>" % self._info


class TransformsManager(monasca_manager.MonascaManager):
    resource_class = Transforms
    base_url = "/transforms"

    def get(self, **kwargs):
        """Get specific transform"""
        url_str = self.base_url + "/%s" % kwargs['transform_id']
        newheaders = self.get_headers()
        resp, body = self.client.json_request('GET', url_str,
                                              headers=newheaders)
        return body

    def list(self, **kwargs):
        """Get a list of transforms"""
        url_str = self.base_url
        newheaders = self.get_headers()
        resp, body = self.client.json_request('GET', url_str,
                                              headers=newheaders)
        return body

    def create(self, **kwargs):
        """Create a transform"""
        url_str = self.base_url
        newheaders = self.get_headers()
        payload = kwargs['transform']
        resp, body = self.client.json_request('POST',
                                              url_str,
                                              data=payload,
                                              headers=newheaders)
        return resp

    def delete(self, **kwargs):
        """Delete a specific transform"""
        url_str = self.base_url + "/%s" % kwargs['transform_id']
        newheaders = self.get_headers()
        resp, body = self.client.json_request('DELETE', url_str,
                                              headers=newheaders)
        return resp


class StreamDefinitions(base.Resource):

    def __repr__(self):
        return "<Transforms %s>" % self._info


class StreamDefinitionsManager(monasca_manager.MonascaManager):
    resource_class = StreamDefinitions
    base_url = "/stream-definitions"

    def get(self, **kwargs):
        """Get specific stream definition"""
        url_str = self.base_url + "/%s" % kwargs['definition_id']
        newheaders = self.get_headers()
        resp, body = self.client.json_request('GET', url_str,
                                              headers=newheaders)
        return body

    def list(self, **kwargs):
        """Get a list of transforms"""
        url_str = self.base_url
        newheaders = self.get_headers()
        resp, body = self.client.json_request('GET', url_str,
                                              headers=newheaders)
        return body

    def create(self, **kwargs):
        """Create a stream definition"""
        url_str = self.base_url
        newheaders = self.get_headers()
        payload = kwargs['definition']
        resp, body = self.client.json_request('POST', url_str,
                                              data=payload,
                                              headers=newheaders)
        return resp

    def delete(self, **kwargs):
        """Delete a specific transform"""
        url_str = self.base_url + "/%s" % kwargs['definition_id']
        newheaders = self.get_headers()
        resp, body = self.client.json_request('DELETE', url_str,
                                              headers=newheaders)
        return resp
