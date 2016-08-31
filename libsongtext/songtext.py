import argparse
from importlib import import_module  # __import__ does not resolve dotted paths
import os
import sys

import click

from .properties import __version__


DEFAULT_API = os.environ.get('SONGTEXT_DEFAULT_API', 'lyricwiki')


@click.command()
@click.option('--api', default=DEFAULT_API, type=click.Choice(['lyricwiki',
'lyricsnmusic']))
@click.option('-V', '--version', is_flag=True)
@click.option('-a', '--artist')
@click.option('-t', '--title')
@click.option('-w', '--words')
@click.option('-l', '--limit')
@click.option('-i', '--index')
@click.argument('all_fields', required=False)
def cli(api, version, artist, title, words, limit, index, all_fields):
    if version:
        click.echo('{}.{}.{}'.format(*__version__))
        return 0

    api_module = import_module(__package__ + '.' + ''.join(api))
    params = {
        'artist': artist,
        'title': title,
        'words': words,
        'limit': limit,
        'index': index
    }
    return getattr(api_module, 'get_result')(params)


def main():
    return cli()
