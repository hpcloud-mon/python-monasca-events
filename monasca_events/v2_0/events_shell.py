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

import yaml

from monasca_events.common import utils
import monasca_events.exc as exc



@utils.arg('id', metavar='<EVENT_ID>',
           help='The ID of the event.')
def do_event_get(mc, args):
    """Get specific event"""
    fields = {'event_id': args.id}
    try:
        event = mc.events.get(**fields)
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(event))
        return
    cols = ['name']
    formatters = {
        'name': lambda x: x['name']
    }
    utils.print_list(event, cols, formatters=formatters)


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
    if args.json:
        print(utils.json_formatter(events))
        return
    cols = ['name']
    formatters = {
        'name': lambda x: x['name']
    }
    utils.print_list(events, cols, formatters=formatters)


@utils.arg('id', metavar='<TRANSFORM_ID>',
           help='The ID of the transform.')
def do_transform_get(mc, args):
    """Get specific transform"""
    fields = {'transform_id': args.id}
    try:
        transform = mc.transforms.get(**fields)
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(transform))
        return
    cols = ['id', 'tenant_id', 'name', 'description']
    # add the dictionary to a list, so print_list works
    transform_list = list()
    transform_list.append(transform)
    formatters = {
        'id': lambda x: x['id'],
        'tenant_id': lambda x: x['tenant_id'],
        'name': lambda x: x['name'],
        'description': lambda x: x['description'],
    }
    utils.print_list(transform, cols, formatters=formatters)
    specification = yaml.load(transform[0]['specification'])
    print yaml.dump(specification)


def do_transform_list(mc, args):
    """Show list of transforms"""
    fields = {}
    try:
        transforms = mc.transforms.list(**fields)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(transforms))
        return
    cols = ['id', 'tenant_id', 'name', 'description']
    formatters = {
        'id': lambda x: x['id'],
        'tenant_id': lambda x: x['tenant_id'],
        'name': lambda x: x['name'],
        'description': lambda x: x['description'],
    }
    utils.print_list(transforms, cols, formatters=formatters)


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
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(definition))
        return
    cols = ['id', 'tenant_id', 'name', 'description', 'select', 'group by',
            'fire criteria', 'expiration', 'fire actions', 'expire actions']
    formatters = {
        'id': lambda x: x['id'],
        'tenant_id': lambda x: x['tenant_id'],
        'name': lambda x: x['name'],
        'description': lambda x: x['description'],
        'select': lambda x: utils.format_dict(x['select']),
        'group_by': lambda x: x['group_by'],
        'fire_criteria': lambda x: utils.format_dict(x['fire_criteria']),
        'expiration': lambda x: x['expiration'],
        'fire_actions': lambda x: x['fire_actions'],
        'expire_actions': lambda x: x['expire_actions']
    }
    utils.print_list(definition, cols, formatters=formatters)


def do_stream_definition_list(mc, args):
    """Show list of stream definitions"""
    fields = {}
    try:
        definitions = mc.stream_definitions.list(**fields)
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(definitions))
        return
    cols = ['id', 'tenant_id', 'name', 'description', 'select', 'group by',
            'fire criteria', 'expiration', 'fire actions', 'expire actions']
    formatters = {
        'id': lambda x: x['id'],
        'tenant_id': lambda x: x['tenant_id'],
        'name': lambda x: x['name'],
        'description': lambda x: x['description'],
        'select': lambda x: utils.format_dict(x['select']),
        'group_by': lambda x: x['group_by'],
        'fire_criteria': lambda x: utils.format_dict(x['fire_criteria']),
        'expiration': lambda x: x['expiration'],
        'fire_actions': lambda x: x['fire_actions'],
        'expire_actions': lambda x: x['expire_actions']
    }
    utils.print_list(definitions, cols, formatters=formatters)


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