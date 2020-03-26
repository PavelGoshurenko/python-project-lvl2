from gendiff.constants import ADDED, REMOVED, CHANGED


def add_parent_name(child, parent_name):
    result = {}
    for index, value in child.items():
        result['{}.{}'.format(parent_name, index)] = value
    return result


def format(diff):
    string = ''
    for key, value in diff.items():
        if isinstance(value, dict):
            string += format(add_parent_name(value, key))
        elif value[0] == CHANGED:
            text1 = 'complex value' if isinstance(value[1], dict) else value[1]
            text2 = 'complex value' if isinstance(value[2], dict) else value[2]
            string += "Property '{}' was changed. From '{}' to '{}'\n".format(key, text1, text2) # noqa E501
        elif value[0] == REMOVED:
            string += "Property '{}' was removed\n".format(key)
        elif value[0] == ADDED:
            text = 'complex value' if isinstance(value[1], dict) else value[1]
            string += "Property '{}' was added with value: '{}'\n".format(key, text) # noqa E501
    return string
