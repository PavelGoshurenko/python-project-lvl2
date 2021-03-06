from gendiff.constants import SAME, ADDED, REMOVED, CHANGED, NESTED


def dict2string(dictionary_or_str):
    string = ''
    if isinstance(dictionary_or_str, dict):
        for index, value in dictionary_or_str.items():
            string += "        {}: {}\n".format(index, value)
        return "{{\n{}    }}".format(string)
    return dictionary_or_str


def text_prerender(diff):
    list_of_str = []
    for key, (status, value) in diff.items():
        if status == NESTED:
            list_of_str.append("  {}: {{\n{}\n  }}".format(key, text_prerender(value))) # noqa E501
        elif status == SAME:
            list_of_str.append("    {}: {}".format(key, dict2string(value)))
        elif status == CHANGED:
            old, new = value
            list_of_str.append("  + {}: {}".format(key, dict2string(new)))
            list_of_str.append("  - {}: {}".format(key, dict2string(old)))
        elif status == REMOVED:
            list_of_str.append("  - {}: {}".format(key, dict2string(value)))
        elif status == ADDED:
            list_of_str.append("  + {}: {}".format(key, dict2string(value)))
    return '\n'.join(list_of_str)


def format(diff):
    return "{{\n{}\n}}".format(text_prerender(diff))
