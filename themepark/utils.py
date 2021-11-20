import json

import click


def pretty_print(data):
    click.echo(json.dumps(data, ensure_ascii=False, sort_keys=False, indent=2))
