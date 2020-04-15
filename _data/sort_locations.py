#!/usr/bin/python3

import sys

import yaml

infile = 'locations.yml'
outfile = 'gen/locations.yml'


def read_yaml(filename):
    with open(filename, 'r') as stream:
        try:
            return(yaml.load(stream, yaml.SafeLoader))
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit(1)


def write_yaml(data, filename):
    with open(filename, 'w') as outfile:
        yaml.dump(
            data, outfile,
            default_flow_style=False,
            encoding='utf-8',
            indent=4
        )


if __name__ == '__main__':
    data = read_yaml(infile)
    data = sorted(data, key=lambda k: k['name'])
    write_yaml(data, outfile)
