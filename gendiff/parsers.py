import json
import yaml


FORMATS = (JSON, YML) = ('json', 'yml')


def parse_file(path_to_file):
    path_separated = path_to_file.split(".")
    format = path_separated[-1]
    if format == JSON:
        data = json.load(open(path_to_file))
        return data
    if format == YML:
        data = yaml.safe_load(open(path_to_file))
        return data
