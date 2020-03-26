from gendiff.parsers import parse_file
from gendiff import formatters
from gendiff.constants import SAME, ADDED, REMOVED, CHANGED


def gen_diff_between_dict(before, after):
    before_keys = before.keys()
    after_keys = after.keys()
    diff = {}
    for key in sorted(before_keys & after_keys):
        if before[key] == after[key]:
            diff[key] = (SAME, before[key])
        elif isinstance(after[key], dict) and isinstance(before[key], dict):
            diff[key] = gen_diff_between_dict(before[key], after[key])
        else:
            diff[key] = (CHANGED, before[key], after[key])
    for key in sorted(before_keys - after_keys):
        diff[key] = (REMOVED, before[key])
    for key in sorted(after_keys - before_keys):
        diff[key] = (ADDED, after[key])
    return diff


def format(diff, format_type=formatters.DEFAULT):
    if format_type == formatters.PLAIN:
        return formatters.plain(diff)
    elif format_type == formatters.JSON:
        return formatters.json(diff)
    return formatters.default(diff)


def generate_diff(path_to_file1, path_to_file2):
    before = parse_file(path_to_file1)
    after = parse_file(path_to_file2)
    diff = gen_diff_between_dict(before, after)
    return diff
