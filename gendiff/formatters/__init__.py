from gendiff.formatters.json import format as json # noqa F401
from gendiff.formatters.plain import format as plain # noqa F401
from gendiff.formatters.text import format as default # noqa F401


FORMATTERS = (JSON, PLAIN, DEFAULT) = (
    'json', 'plain', 'default'
)


def format(diff, format_type=DEFAULT):
    if format_type == PLAIN:
        return plain(diff)
    elif format_type == JSON:
        return json(diff)
    elif format_type == DEFAULT:
        return default(diff)
    print('The format {} is not supported. Normal text output will be used.'.format(format_type))  # noqa E501
    return default(diff)
