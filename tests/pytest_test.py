import pytest
from gendiff.generate_diff import generate_diff, format
from tests.test_data import TEST_DATA, BEFORE, AFTER, FORMAT, ANSWER


def test():
    for test_data in TEST_DATA.values():
        with open(test_data[ANSWER], 'r') as file:
            correct_result = file.read()
        assert correct_result == format(
            generate_diff(test_data[BEFORE],
            test_data[AFTER]),
            test_data[FORMAT]
            )
