import pytest
from gendiff.functions import generate_diff


def test_json():
    f = open('./tests/fixtures/test_result.txt', 'r')
    correct_result = f.read()
    f.close()
    assert correct_result == generate_diff('./tests/fixtures/before.json', './tests/fixtures/after.json', '')


def test_yml():
    f = open('./tests/fixtures/test_result.txt', 'r')
    correct_result = f.read()
    f.close()
    assert correct_result == generate_diff('./tests/fixtures/before.yml', './tests/fixtures/after.yml', '')


def test_nested_json():
    f = open('./tests/fixtures/test_result_nested.txt', 'r')
    correct_result = f.read()
    f.close()
    assert correct_result == generate_diff('./tests/fixtures/before_nested.json', './tests/fixtures/after_nested.json', '')


def test_nested_yml():
    f = open('./tests/fixtures/test_result_nested.txt', 'r')
    correct_result = f.read()
    f.close()
    assert correct_result == generate_diff('./tests/fixtures/before_nested.yml', './tests/fixtures/after_nested.yml', '')


def test_json_plane_format():
    f = open('./tests/fixtures/test_result_plain.txt', 'r')
    correct_result = f.read()
    f.close()
    assert correct_result == generate_diff('./tests/fixtures/before_nested.json', './tests/fixtures/after_nested.json', 'plain')


def test_yml_plain_format():
    f = open('./tests/fixtures/test_result_plain.txt', 'r')
    correct_result = f.read()
    f.close()
    assert correct_result == generate_diff('./tests/fixtures/before_nested.yml', './tests/fixtures/after_nested.yml', 'plain')
