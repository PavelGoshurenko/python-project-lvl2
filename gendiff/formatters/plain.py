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
        text1 = 'complex value' if isinstance(value[0], dict) else value[0]
        text2 = 'complex value' if isinstance(value[1], dict) else value[1]
        string += "Property '{}' was changed. From '{}' to '{}'\n".format(index, text1, text2) # noqa E501
    for index in diff['minus'].keys():
        string += "Property '{}' was removed\n".format(index)
    for index, value in diff['plus'].items():
        text = 'complex value' if isinstance(value, dict) else value
        string += "Property '{}' was added with value: '{}'\n".format(index, text) # noqa E501
    return string
