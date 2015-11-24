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
    """Get specific event."""
    fields = {'event_id': args.id}
    try:
        event = mc.events.get(**fields)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(event))
        return
    cols = ['id', 'description', 'generated', 'data']
    formatters = {
        'id': lambda x: x['id'],
        'description': lambda x: x['description'],
        'generated': lambda x: x['generated'],
        'data': lambda x: utils.format_dict(x['data'])
    }
    utils.print_list(event, cols, formatters=formatters)


@utils.arg('--limit', metavar='<RETURN LIMIT>',
           help='The amount of data to be returned up to the maximum limit.')
@utils.arg('--offset', metavar='<OFFSET BY ID>',
           help='Offset returned data by ID')
def do_event_list(mc, args):
    """Show list of events."""
    fields = {}
    if args.limit:
        fields['limit'] = args.limit
    if args.offset:
        fields['offset'] = args.offset
    try:
        events = mc.events.list(**fields)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(events))
        return
    cols = ['id', 'description', 'generated', 'data']
    formatters = {
        'id': lambda x: x['id'],
        'description': lambda x: x['description'],
        'generated': lambda x: x['generated'],
        'data': lambda x: utils.format_dict(x['data'])
    }
    utils.print_list(events, cols, formatters=formatters)


@utils.arg('id', metavar='<TRANSFORM_ID>',
           help='The ID of the transform.')
def do_transform_get(mc, args):
    """Get specific transform."""
    fields = {'transform_id': args.id}
    try:
        transform = mc.transforms.get(**fields)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(transform))
        return
    cols = ['id', 'tenant_id', 'name', 'description']
    formatters = {
        'id': lambda x: x['id'],
        'tenant_id': lambda x: x['tenant_id'],
        'name': lambda x: x['name'],
        'description': lambda x: x['description'],
    }
    # add to list so print_list will work
    transform_list = list()
    transform_list.append(transform)
    utils.print_list(transform_list, cols, formatters=formatters)
    specification = yaml.load(transform['specification'])
    print (yaml.dump(specification))


@utils.arg('--limit', metavar='<RETURN LIMIT>',
           help='The amount of data to be returned up to the maximum limit.')
@utils.arg('--offset', metavar='<OFFSET BY ID>',
           help='Offset returned data by ID')
def do_transform_list(mc, args):
    """Show list of transforms."""
    fields = {}
    if args.limit:
        fields['limit'] = args.limit
    if args.offset:
        fields['offset'] = args.offset
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
    """Create a transform."""
    fields = {'transform': utils.format_parameters(args.transform)}
    try:
        resp = mc.transforms.create(**fields)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


@utils.arg('id', metavar='<TRANSFORM_ID>',
           help='The ID of the transform.')
def do_transform_delete(mc, args):
    """Delete a transform."""
    fields = {'transform_id': args.id}
    try:
        resp = mc.transforms.delete(**fields)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


@utils.arg('id', metavar='<STREAM_DEFINITION_ID>',
           help='The ID of the stream definition.')
def do_stream_definition_get(mc, args):
    """Get specific stream definition."""
    fields = {'definition_id': args.id}
    try:
        definition = mc.stream_definitions.get(**fields)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(definition))
        return
    cols = ['id', 'name', 'description', 'select', 'group_by',
            'fire_criteria', 'expiration', 'fire_actions', 'expire_actions']
    formatters = {
        'id': lambda x: x['id'],
        'name': lambda x: x['name'],
        'description': lambda x: x['description'],
        'select': lambda x: utils.format_dictlist(x['select']),
        'group_by': lambda x: x['group_by'],
        'fire_criteria': lambda x: utils.format_dictlist(x['fire_criteria']),
        'expiration': lambda x: x['expiration'],
        'fire_actions': lambda x: x['fire_actions'],
        'expire_actions': lambda x: x['expire_actions'],
    }
    # add to list so print_list will work
    definition_list = list()
    definition_list.append(definition)
    utils.print_list(definition_list, cols, formatters=formatters)


@utils.arg('--limit', metavar='<RETURN LIMIT>',
           help='The amount of data to be returned up to the maximum limit.')
@utils.arg('--offset', metavar='<OFFSET BY ID>',
           help='Offset returned data by ID')
def do_stream_definition_list(mc, args):
    """Show list of stream definitions."""
    fields = {}
    if args.limit:
        fields['limit'] = args.limit
    if args.offset:
        fields['offset'] = args.offset
    try:
        definitions = mc.stream_definitions.list(**fields)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(definitions))
        return
    cols = ['id', 'name', 'description', 'select', 'group_by',
            'fire_criteria', 'expiration', 'fire_actions', 'expire_actions']
    formatters = {
        'id': lambda x: x['id'],
        'name': lambda x: x['name'],
        'description': lambda x: x['description'],
        'select': lambda x: utils.format_dictlist(x['select']),
        'group_by': lambda x: x['group_by'],
        'fire_criteria': lambda x: utils.format_dictlist(x['fire_criteria']),
        'expiration': lambda x: x['expiration'],
        'fire_actions': lambda x: x['fire_actions'],
        'expire_actions': lambda x: x['expire_actions'],
    }
    utils.print_list(definitions, cols, formatters=formatters)


@utils.arg('definition',
           metavar='<fire_criteria=VALUE1,description=VALUE2,name=VALUE3...',
           help='The stream definition dict.')
def do_stream_definition_create(mc, args):
    """Create a stream definition."""
    fields = {'definition': utils.format_parameters(args.definition)}
    try:
        resp = mc.stream_definitions.get(**fields)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


@utils.arg('id', metavar='<STREAM_DEFINITION_ID>',
           help='The stream definition id.')
def do_stream_definition_delete(mc, args):
    """Delete a stream definition."""
    fields = {'definition_id': args.id}
    try:
        resp = mc.stream_definitions.get(**fields)
    except exc.HTTPException as he:
        raise  exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))


@utils.arg('id', metavar='<STREAM_DEFINITION_ID>',
           help='The ID of the stream definition.')
@utils.arg('--name', metavar='<STREAM_DEFINITION_NAME>',
           help='Name of the stream definition.')
@utils.arg('--description', metavar='<DESCRIPTION>',
           help='Description of the stream.')
@utils.arg('--expiration', metavar='<EXPIRATION>',
           help='The expiration of the stream.', type=int)
@utils.arg('--fire-criteria', metavar='<KEY1=VALUE1,KEY2=VALUE2...>',
           help='kev value pair used to specify a fire criteria. '
           'This can be specified multiple times, or once with parameters '
           'separated by a comma. ',
           action='append')
@utils.arg('--fire-actions', metavar='<NOTIFICATION-ID>',
           help='The notification method to use when the fire criteria is met for the stream. '
           'This param may be specified multiple times.',
           action='append')
@utils.arg('--expire-actions', metavar='<NOTIFICATION-ID>',
           help='The notification method to use when the expiration for the stream is met. '
           'This param may be specified multiple times.',
           action='append')
def do_stream_definition_patch(mc, args):
    """Patch a stream definition."""
    fields = {'definition_id': args.id}
    if args.name:
        fields['name'] = args.name
    if args.description:
        fields['description'] = args.description
    if args.expiration:
        fields['expiration'] = args.expiration
    if args.fire_actions:
        fields['fire_actions'] = args.fire_actions
    if args.expire_actions:
        fields['expire_actions'] = args.expire_actions
    if args.fire_criteria:
        fields['fire_criteria'] = utils.format_parameters(args.fire_criteria)
    try:
        new_definition = mc.stream_definitions.patch(**fields)
    except exc.HTTPException as he:
        raise exc.CommandError(
            'HTTPException code=%s message=%s' %
            (he.code, he.message))
    if args.json:
        print(utils.json_formatter(new_definition))
        return
    cols = ['id', 'name', 'description', 'select', 'group_by',
            'fire_criteria', 'expiration', 'fire_actions', 'expire_actions']
    formatters = {
        'id': lambda x: x['id'],
        'name': lambda x: x['name'],
        'description': lambda x: x['description'],
        'select': lambda x: utils.format_dictlist(x['select']),
        'group_by': lambda x: x['group_by'],
        'fire_criteria': lambda x: utils.format_dict(x['fire_criteria']),
        'expiration': lambda x: x['expiration'],
        'fire_actions': lambda x: x['fire_actions'],
        'expire_actions': lambda x: x['expire_actions'],
    }
    # append to list so print list works
    new_definition_list = list()
    new_definition_list.append(new_definition)
    utils.print_list(new_definition_list, cols, formatters=formatters)
