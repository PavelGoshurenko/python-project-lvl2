from gendiff.formatters.json import format as json # noqa F401
from gendiff.formatters.plain import format as plain # noqa F401
from gendiff.formatters.text import format as default # noqa F401


FORMATTERS = (JSON, PLAIN, DEFAULT) = (
    'json', 'plain', 'default'
)
