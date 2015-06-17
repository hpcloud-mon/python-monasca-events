Python bindings to the Monasca Events API
=======================================

This is a client library for Monasca built to interface with the Monasca Events API. It
provides a Python API (the ``monasca-events`` module) and a command-line tool
(``monasca-events``).

The Monasca Events Client was written using the OpenStack Heat Python client as a framework.


Ubuntu Install
--------------

Manual Install Steps:
  - cd to your python-monasca-events repo
  - sudo pip install -r requirements.txt
  - python setup.py install

Command-line API
----------------
Installing this distribution gets you a shell command, ``monasca-events``, that you
can use to interact with the Events API server.

Usage:
  monasca-events

  monasca-events help

  monasca-events help <command>

  monasca-events -j <command>

    This outputs the results in json format.  Normally output is in table format.


Environmental Variables
----------------

Environmental variables can be sourced, or optionally passed in as CLI arguments.
It is easiest to source them first and then use the CLI.

When token and endpoint are known::

  ``export OS_AUTH_TOKEN=XXX``

When using Keystone to obtain the token and endpoint::
  ```
  export OS_USERNAME=
  export OS_PASSWORD=
  export OS_PROJECT_NAME=
  export OS_AUTH_URL=
  export OS_REGION_NAME=
  ```

When using Vagrant Environment with middleware disabled::
  ```
  export OS_AUTH_TOKEN=82510970543135
  export OS_NO_CLIENT_AUTH=1
  ```
The Monasca Events API will treat the auth token as the tenant ID when Keystone is not enabled.

You'll find complete documentation on the shell by running
``monasca-events help``::


  ```
  usage: monasca-events [-j] [--version] [-d] [-v] [-k] [--cert-file CERT_FILE]
               [--key-file KEY_FILE] [--os-cacert OS_CACERT]
               [--timeout TIMEOUT] [--os-username OS_USERNAME]
               [--os-password OS_PASSWORD] [--os-project-id OS_PROJECT_ID]
               [--os-project-name OS_PROJECT_NAME]
               [--os-domain-id OS_DOMAIN_ID] [--os-domain-name OS_DOMAIN_NAME]
               [--os-auth-url OS_AUTH_URL] [--os-region-name OS_REGION_NAME]
               [--os-auth-token OS_AUTH_TOKEN] [--os-no-client-auth]
               [--monasca-api-url MONASCA_API_URL]
               [--monasca-api-version MONASCA_API_VERSION]
               [--os-service-type OS_SERVICE_TYPE]
               [--os-endpoint-type OS_ENDPOINT_TYPE]
               <subcommand> ...
  ```

  Command-line interface to the monasca-events API.
  ```
  positional arguments:
    <subcommand>
      help                     Display help about this program or one of its
                               subcommands.

  optional arguments:
    -j, --json                 output raw json response
    --version                  Shows the client version and exits.
    -d, --debug                Defaults to env[MONASCA_DEBUG].
    -v, --verbose              Print more verbose output.
    -k, --insecure             Explicitly allow the client to perform "insecure" SSL
                               (https) requests. The server's certificate will not
                               be verified against any certificate authorities. This
                               option should be used with caution.
    --cert-file CERT_FILE      Path of certificate file to use in SSL connection.
                               This file can optionally be prepended with the
                               private key.
    --key-file KEY_FILE        Path of client key to use in SSL connection.This
                               option is not necessary if your key is prepended to
                               your cert file.
    --os-cacert OS_CACERT      Specify a CA bundle file to use in verifying a
                               TLS (https) server certificate. Defaults to
                               env[OS_CACERT]. Without either of these, the
                               client looks for the default system CA
                               certificates.
    --timeout TIMEOUT          Number of seconds to wait for a response.
    --os-username OS_USERNAME  Defaults to env[OS_USERNAME].
    --os-password OS_PASSWORD  Defaults to env[OS_PASSWORD].
    --os-project-id OS_PROJECT_ID
                               Defaults to env[OS_PROJECT_ID].
    --os-project-name OS_PROJECT_NAME
                               Defaults to env[OS_PROJECT_NAME].
    --os-domain-id OS_DOMAIN_ID
                               Defaults to env[OS_DOMAIN_ID].
    --os-domain-name OS_DOMAIN_NAME
                               Defaults to env[OS_DOMAIN_NAME].
    --os-auth-url OS_AUTH_URL  Defaults to env[OS_AUTH_URL].
    --os-region-name OS_REGION_NAME
                               Defaults to env[OS_REGION_NAME].
    --os-auth-token OS_AUTH_TOKEN
                               Defaults to env[OS_AUTH_TOKEN].
    --os-no-client-auth        Do not contact keystone for a token. Defaults to
                               env[OS_NO_CLIENT_AUTH].
    --monasca-api-url MONASCA_API_URL
                               Defaults to env[MONASCA_API_URL].
    --monasca-api-version MONASCA_API_VERSION
                               Defaults to env[MONASCA_API_VERSION] or 2_0
    --os-service-type OS_SERVICE_TYPE
                               Defaults to env[OS_SERVICE_TYPE].
    --os-endpoint-type OS_ENDPOINT_TYPE
                               Defaults to env[OS_ENDPOINT_TYPE].
  ```




License
-------

Copyright (c) 2015 Hewlett-Packard Development Company, L.P.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied.
See the License for the specific language governing permissions and
limitations under the License.
