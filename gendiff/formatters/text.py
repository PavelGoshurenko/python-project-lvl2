def dict2string(dictionary_or_str):
    string = ''
    if isinstance(dictionary_or_str, dict):
        for index, value in dictionary_or_str.items():
            string += "        {}: {}\n".format(index, value)
        return "{{\n{}    }}".format(string)
    return dictionary_or_str


def text_prerender(diff):
    string = ''
    if len(diff['complex']) > 0:
        for index, value in diff['complex'].items():
            string += "  {}: {{\n{}  }}\n".format(index, text_prerender(value))
    for index, value in diff['same'].items():
        string += "    {}: {}\n".format(index, dict2string(value))
    for index, value in diff['change'].items():
        string += "  + {}: {}\n".format(index, dict2string(value[1]))
        string += "  - {}: {}\n".format(index, dict2string(value[0]))
    for index, value in diff['minus'].items():
        string += "  - {}: {}\n".format(index, dict2string(value))
    for index, value in diff['plus'].items():
        string += "  + {}: {}\n".format(index, dict2string(value))
    return string


def text_render(diff):
    return "{{\n{}}}".format(text_prerender(diff))
