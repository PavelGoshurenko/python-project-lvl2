import pytest
from gendiff.functions import generate_diff


def test_plain_json_test():
    f = open('./tests/fixtures/test_result.txt', 'r')
    correct_result = f.read()
    f.close()
    assert correct_result == generate_diff('before.json', 'after.json')