import argparse
from importlib import import_module  # __import__ does not resolve dotted paths
import os
import sys

import click

from errors import ArgumentError, TrackIndexError, SearchError
from properties import __version__


DEFAULT_API = os.environ.get('SONGTEXT_DEFAULT_API', 'lyricwiki')
AVAILABLE_APIS = ['lyricwiki', 'lyricsnmusic']


@click.command()
@click.option('--api', default=DEFAULT_API, type=click.Choice(AVAILABLE_APIS))
@click.option('-V', '--version', is_flag=True)
@click.option('-a', '--artist')
@click.option('-t', '--title')
@click.option('-w', '--words')
@click.option('-l', '--show-list', default=False, is_flag=True)
@click.option('--limit', type=int)
@click.option('-i', '--index', type=int)
@click.option('--no-pager', default=False, is_flag=True)
@click.argument('all_fields', required=False, nargs=-1)
def cli(api, version, artist, title, words, show_list, limit, index, no_pager, all_fields):
    if version:
        click.echo('{}.{}.{}'.format(*__version__))
        return 0

    api_module = import_module(__package__ + '.' + ''.join(api))
    params = {
        'artist': artist,
        'title': title,
        'words': words,
        'list': show_list,
        'limit': limit,
        'index': index,
        'no_pager': no_pager,
        'all_fields': all_fields
    }
    return getattr(api_module, 'get_result')(params)


def main():
    try:
        cli()
    except (ArgumentError, TrackIndexError, SearchError):
        return 1
    return 0
