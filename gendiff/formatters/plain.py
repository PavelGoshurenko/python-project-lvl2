def add_parent_name(child, parent_name):
    result = {}
    for index, value in child.items():
        result[index] = {}
        for i, v in value.items():
            result[index]['{}.{}'.format(parent_name, i)] = v
    return result


def plain_render(diff):
    string = ''
    if len(diff['complex']) > 0:
        for index, value in diff['complex'].items():
            string += plain_render(add_parent_name(value, index))
    for index, value in diff['change'].items():
        if isinstance(value[0], dict):
            text1 = 'complex value'
        else:
            text1 = value[0]
        if isinstance(value[1], dict):
            text2 = 'complex value'
        else:
            text2 = value[1]
        string += "Property '{}' was changed. From '{}' to '{}'\n".format(index, text1, text2) # noqa E501
    for index in diff['minus'].keys():
        string += "Property '{}' was removed\n".format(index)
    for index, value in diff['plus'].items():
        if isinstance(value, dict):
            text = 'complex value'
        else:
            text = value
        string += "Property '{}' was added with value: '{}'\n".format(index, text) # noqa E501
    return string
