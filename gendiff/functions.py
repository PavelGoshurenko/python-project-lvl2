from gendiff.parsers import parse_file


def dictionary2str(dictionary, mark):
    string = ''
    for index, value in dictionary.items():
        if len(mark) == 2:
            string += "  {} {}: {}\n  {} {}: {}\n".format(
                mark[0], index, value[0], mark[1], index, value[1]
                )
        else:
            string += "  {} {}: {}\n".format(mark, index, value)
    return string


def generate_diff(path_to_file1, path_to_file2):
    before = parse_file(path_to_file1)
    after = parse_file(path_to_file2)
    same = {}
    plus = {}
    minus = {}
    change = {}
    for index, value in before.items():
        if after.get(index, None) is None:
            minus[index] = value
            continue
        if after.get(index, None) == value:
            same[index] = value
        else:
            change[index] = (after[index], before[index])
    for index, value in after.items():
        if before.get(index, None) is None:
            plus[index] = value
    string = "{}{}{}{}".format(
        dictionary2str(same, ' '),
        dictionary2str(change, '+-'),
        dictionary2str(minus, '-'),
        dictionary2str(plus, '+')
        )
    string = "{\n" + string + "}"
    return string
