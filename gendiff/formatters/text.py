from gendiff.constants import SAME, ADDED, REMOVED, CHANGED


def dict2string(dictionary_or_str):
    string = ''
    if isinstance(dictionary_or_str, dict):
        for index, value in dictionary_or_str.items():
            string += "        {}: {}\n".format(index, value)
        return "{{\n{}    }}".format(string)
    return dictionary_or_str


def text_prerender(diff):
    string = ''
    for key, value in diff.items():
        if isinstance(value, dict):
            string += "  {}: {{\n{}  }}\n".format(key, text_prerender(value))
        elif value[0] == SAME:
            string += "    {}: {}\n".format(key, dict2string(value[1]))
        elif value[0] == CHANGED:
            string += "  + {}: {}\n".format(key, dict2string(value[2]))
            string += "  - {}: {}\n".format(key, dict2string(value[1]))
        elif value[0] == REMOVED:
            string += "  - {}: {}\n".format(key, dict2string(value[1]))
        elif value[0] == ADDED:
            string += "  + {}: {}\n".format(key, dict2string(value[1]))
    return string


def format(diff):
    return "{{\n{}}}".format(text_prerender(diff))
