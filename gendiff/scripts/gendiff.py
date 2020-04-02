#!/usr/bin/env python3


import argparse
from gendiff.generate_diff import generate_diff
from gendiff import formatters


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    format_type = formatters.DEFAULT if args.format is None else args.format
    print(formatters.format(
        generate_diff(args.first_file, args.second_file),
        format_type))


if __name__ == '__main__':
    main()
