import json
import yaml


def parse_file(path_to_file):
    path_separated = path_to_file.split(".")
    if path_separated[-1] == 'json':
        data = json.load(open(path_to_file))
        return data
    if path_separated[-1] == 'yml':
        data = yaml.safe_load(open(path_to_file))
        return data
    return None
