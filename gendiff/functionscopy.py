from gendiff.parsers import parse_file
from gendiff.formatters.plain import plain_render


def dictionary2str(dictionary, mark):
    string = ''
    for index, value in dictionary.items():
        if isinstance(value, dict):
            string += '  ' + mark + ' ' + index+ ': {\n' + dictionary2str(value, '   ') + '   }\n'
            continue
        if len(mark) == 2:
            string += "  {} {}: {}\n  {} {}: {}\n".format(
                mark[0], index, value[0], mark[1], index, value[1]
                )
        else:
            string += "  {} {}: {}\n".format(mark, index, value)
    return string



def generate_diff(path_to_file1, path_to_file2, format_):
    before = parse_file(path_to_file1)
    after = parse_file(path_to_file2)
    diff = gen_diff_between_dictionaries(before, after)
    if format_ == 'plain':
        render = plain_render(diff)
    else:
        render = render_diff(diff)
    return render

def gen_diff_between_dictionaries(before, after):
    
    diff = {
        'same': {},
        'plus': {},
        'minus': {},
        'change': {},
        'complex': {}
    }
    for index, value in before.items():
        if after.get(index, None) is None:
            diff['minus'][index] = value
            continue
        if after.get(index, None) == value:
            diff['same'][index] = value
        elif  isinstance(after.get(index, None), dict) and isinstance(before.get(index, None), dict):
            diff['complex'][index] = gen_diff_between_dictionaries(before[index], after[index])
        else:
            diff['change'][index] = (after[index], before[index])
    for index, value in after.items():
        if before.get(index, None) is None:
            diff['plus'][index] = value
    return diff
    

def render_diff(diff):
    string = ''
    if len(diff['complex']) > 0:
        for index, value in diff['complex'].items():
            string += '  ' + index + ': '
            string += render_diff(value) + ' \n'
    string += "{}{}{}{}".format(
    dictionary2str(diff['same'], ' '),
    dictionary2str(diff['change'], '+-'),
    dictionary2str(diff['minus'], '-'),
    dictionary2str(diff['plus'], '+')
    )
    string = "{\n" + string + "}"
    return string

