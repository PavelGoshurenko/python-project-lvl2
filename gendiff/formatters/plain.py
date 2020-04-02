from gendiff.constants import ADDED, REMOVED, CHANGED, NESTED


def add_parent_name(child, parent_name):
    result = {}
    for index, value in child.items():
        result['{}.{}'.format(parent_name, index)] = value
    return result


def format(diff):
    list_of_strings = []
    for key, (status, value) in diff.items():
        if status == NESTED:
            list_of_strings.append(format(add_parent_name(value, key)))
        elif status == CHANGED:
            old, new = value
            from_ = 'complex value' if isinstance(old, dict) else old
            to_ = 'complex value' if isinstance(new, dict) else new
            list_of_strings.append("Property '{}' was changed. From '{}' to '{}'".format(key, from_, to_)) # noqa E501
        elif status == REMOVED:
            list_of_strings.append("Property '{}' was removed".format(key))
        elif status == ADDED:
            text = 'complex value' if isinstance(value, dict) else value
            list_of_strings.append("Property '{}' was added with value: '{}'".format(key, text)) # noqa E501
    return '\n'.join(list_of_strings)
