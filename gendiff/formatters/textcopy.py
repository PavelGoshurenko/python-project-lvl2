def dictionary2str(dictionary, mark):
    string = ''
    for index, value in dictionary.items():
        if isinstance(value, dict):
            string += '  ' + mark + ' ' + index + ': {\n' + dictionary2str(value, '   ') + '   }\n' # noqa E501
            continue
        if len(mark) == 2:
            string += "  {} {}: {}\n  {} {}: {}\n".format(
                mark[1], index, value[1], mark[0], index, value[0]
                )
        else:
            string += "  {} {}: {}\n".format(mark, index, value)
    return string


def text_render(diff):
    string = ''
    if len(diff['complex']) > 0:
        for index, value in diff['complex'].items():
            string += '  ' + index + ': '
            string += text_render(value) + ' \n'
    string += "{}{}{}{}".format(
        dictionary2str(diff['same'], ' '),
        dictionary2str(diff['change'], '-+'),
        dictionary2str(diff['minus'], '-'),
        dictionary2str(diff['plus'], '+')
        )
    string = "{\n" + string + "}"
    return string
