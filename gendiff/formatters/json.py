import json


def json_pre_render(diff):
    json_diff = {}
    if len(diff['complex']) > 0:
        for index, value in diff['complex'].items():
            json_diff[index] = json_pre_render(value)
    for index, value in diff['same'].items():
        json_diff[index] = ('same', value)
    for index, value in diff['change'].items():
        json_diff[index] = ('changed_from_to', value[0], value[1])
    for index, value in diff['minus'].items():
        json_diff[index] = ('removed', value)
    for index, value in diff['plus'].items():
        json_diff[index] = ('added', value)
    return json_diff


def json_render(diff):
    json_diff = json_pre_render(diff)
    return json.dumps(json_diff)
