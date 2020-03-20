from gendiff.parsers import parse_file
from gendiff.formatters.plain import plain_render
from gendiff.formatters.json import json_render
from gendiff.formatters.text import text_render


def generate_diff(path_to_file1, path_to_file2, format_):
    before = parse_file(path_to_file1)
    after = parse_file(path_to_file2)
    diff = gen_diff_between_dictionaries(before, after)
    if format_ == 'plain':
        render = plain_render(diff)
    elif format_ == 'json':
        render = json_render(diff)
    else:
        render = text_render(diff)
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
        elif  isinstance(after.get(index, None), dict) and isinstance(before.get(index, None), dict): # noqa E501
            diff['complex'][index] = gen_diff_between_dictionaries(before[index], after[index]) # noqa E501
        else:
            diff['change'][index] = (before[index], after[index])
    for index, value in after.items():
        if before.get(index, None) is None:
            diff['plus'][index] = value
    return diff
