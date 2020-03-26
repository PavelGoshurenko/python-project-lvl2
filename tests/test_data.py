JSON_TEST = 'json_test'
YAML_TEST = 'yaml_test'
NESTED_JSON_TEST = 'nested_json_test'
NESTED_YAML_TEST = 'nested_yaml_test'
JSON_PLAIN_TEST = 'json_plain_test'
YAML_PLAIN_TEST = 'yaml_plain_test'
JSON2JSON_TEST = 'json2json_test'
YAML2JSON_TEST = 'yaml2json_test'


BEFORE = 'before_adsress'
AFTER = 'after_address'
FORMAT = 'format'
ANSWER = 'answer'


TEST_DATA = {
    JSON_TEST:{
        BEFORE: './tests/fixtures/before.json',
        AFTER: './tests/fixtures/after.json',
        ANSWER: './tests/fixtures/test_result.txt',
        FORMAT: 'default'
    },
    YAML_TEST:{
        BEFORE: './tests/fixtures/before.yml',
        AFTER: './tests/fixtures/after.yml',
        ANSWER: './tests/fixtures/test_result.txt',
        FORMAT: 'default'
    },
    NESTED_JSON_TEST:{
        BEFORE: './tests/fixtures/before_nested.json',
        AFTER: './tests/fixtures/after_nested.json',
        ANSWER: './tests/fixtures/test_result_nested.txt',
        FORMAT: 'default'
    },
    NESTED_YAML_TEST:{
        BEFORE: './tests/fixtures/before_nested.yml',
        AFTER: './tests/fixtures/after_nested.yml',
        ANSWER: './tests/fixtures/test_result_nested.txt',
        FORMAT: 'default'
    },
    JSON_PLAIN_TEST:{
        BEFORE: './tests/fixtures/before_nested.json',
        AFTER: './tests/fixtures/after_nested.json',
        ANSWER: './tests/fixtures/test_result_plain.txt',
        FORMAT: 'plain'
    },
    YAML_PLAIN_TEST:{
        BEFORE: './tests/fixtures/before_nested.yml',
        AFTER: './tests/fixtures/after_nested.yml',
        ANSWER: './tests/fixtures/test_result_plain.txt',
        FORMAT: 'plain'
    },
    JSON2JSON_TEST:{
        BEFORE: './tests/fixtures/before_nested.json',
        AFTER: './tests/fixtures/after_nested.json',
        ANSWER: './tests/fixtures/test_result_json.txt',
        FORMAT: 'json'
    },
    YAML2JSON_TEST:{
        BEFORE: './tests/fixtures/before_nested.yml',
        AFTER: './tests/fixtures/after_nested.yml',
        ANSWER: './tests/fixtures/test_result_json.txt',
        FORMAT: 'json'
    }
}