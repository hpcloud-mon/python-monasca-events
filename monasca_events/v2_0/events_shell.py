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


from monasca_events.common import utils
import monasca_events.exc as exc


@utils.arg('id', metavar='<EVENT_ID>',
           help='The ID of the event.')
def do_event_get(mc, args):
    """Get specific event"""
    fields = {'event_id': args.id}
    try:
        event = mc.events.get(**fields)
        print(event)
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


def do_event_list(mc, args):
    """Show list of events"""
    fields = {}
    try:
        events = mc.events.list(**fields)
        print(events)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


@utils.arg('id', metavar='<TRANSFORM_ID>',
           help='The ID of the transform.')
def do_transform_get(mc, args):
    """Get specific transform"""
    fields = {'transform_id': args.id}
    try:
        transform = mc.transforms.get(**fields)
        print(transform)
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


def do_transform_list(mc, args):
    """Show list of transforms"""
    fields = {}
    try:
        transforms = mc.transforms.list(**fields)
        # print(transforms)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


@utils.arg('transform',
           metavar='<name=VALUE1,description=VALUE2...>',
           help='The transform dict.',
           action='append')
def do_transform_create(mc, args):
    """Create a transform"""
    fields = {'transform': utils.format_parameters(args.transform)}
    try:
        resp = mc.transforms.create(**fields)
        print(resp.status_code)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


@utils.arg('id', metavar='<TRANSFORM_ID>',
           help='The ID of the transform.')
def do_transform_delete(mc, args):
    """Delete a transform"""
    fields = {'transform_id': args.id}
    try:
        resp = mc.transforms.delete(**fields)
        print(resp.status_code)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


@utils.arg('id', metavar='<STREAM_DEFINITION_ID>',
           help='The ID of the stream definition.')
def do_stream_definition_get(mc, args):
    """Get specific stream definition"""
    fields = {'definition_id': args.id}
    try:
        definition = mc.stream_definitions.get(**fields)
        print(definition)
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    return definition


def do_stream_definition_list(mc, args):
    """Show list of stream definitions"""
    fields = {}
    try:
        definitions = mc.stream_definitions.list(**fields)
        print(definitions)
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    return definitions


@utils.arg('definition',
           metavar='<fire_criteria=VALUE1,description=VALUE2,name=VALUE3...',
           help='The stream definition dict.')
def do_stream_definition_create(mc, args):
    """Create a stream definition"""
    fields = {'definition': utils.format_parameters(args.definition)}
    try:
        resp = mc.stream_definitions.get(**fields)
        print(resp.status_code)
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


@utils.arg('id', metavar='<STREAM_DEFINITION_ID>',
           help='The stream definition id.')
def do_stream_definition_delete(mc, args):
    """Delete a stream definition"""
    fields = {'definition_id': args.id}
    try:
        resp = mc.stream_definitions.get(**fields)
        print(resp.status_code)
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))