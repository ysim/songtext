[![Build Status](https://travis-ci.org/ysim/songtext.svg?branch=master)](https://travis-ci.org/ysim/songtext)

# songtext

A command-line song lyric fetcher.

Inspired by [@gleitz](https://twitter.com/gleitz)'s
[howdoi](https://github.com/gleitz/howdoi). Name from the [German word for
"lyrics"](http://www.dict.cc/deutsch-englisch/Songtext.html).


## Installation

With pip:

    $ pip install songtext

With distutils:

    $ python setup.py install


## Usage

Search by both **artist name** (`-a, --artist`) *and* **song title**
(`-t, --title`):

        $ songtext -a pvris -t fire

        PVRIS: Fire
        -----------
        Don't blame your death on the shit in your head
        That you claimed ate you like a virus for days on end
        I watched you decay, watched you waste away
        Who'd you think you'd fool, baby, diggin' your own grave?

Option values that consist of more than one word need to be quoted:

        $ songtext -a 'nina simone' -t sinnerman

        Nina Simone: Sinnerman
        ----------------------
        Oh sinnerman, where you gonna run to?
        Sinnerman, where you gonna run to?
        Where you gonna run to?
        All along dem day

Punctuation is important too:

        $ songtext -a "shawn mendes" -t "theres nothing holdin me back"

        Your query did not match any tracks.


        $ songtext -a "shawn mendes" -t "there's nothing holdin' me back"

        Shawn Mendes: There's Nothing Holdin' Me Back
        ---------------------------------------------
        I wanna follow her where she goes
        I think about her and she knows it
        I wanna let it take control
        'Cause every time that she gets closer

Note that paging is turned on by default. Use the `--no-pager` flag to turn
it off.


| argument/API                | `lyricwiki` |
| --------------------------  | -----------:|
| positional (generic search) | No          |
| `-a`, `--artist`            | Yes         |
| `-t`, `--title`             | Yes         |
| `-w`, `--words`             | No          |
| `-l`, `--show-list`         | No          |
| `--limit`                   | No          |
| `--no-pager`                | Yes         |
| `-i`, `--index`             | No          |


## Author

* ([@ysim](https://github.com/ysim/))
