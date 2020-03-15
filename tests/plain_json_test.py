import pytest
from gendiff.functions import generate_diff


def test_plain_json_test():
    f = open('./tests/fixtures/test_result.txt', 'r')
    correct_result = f.read()
    f.close()
    assert correct_result == generate_diff('./tests/fixtures/before.json', './tests/fixtures/after.json')

def test_plain_yml_test():
    f = open('./tests/fixtures/test_result.txt', 'r')
    correct_result = f.read()
    f.close()
    assert correct_result == generate_diff('./tests/fixtures/before.yml', './tests/fixtures/after.yml')
