# CONTRIBUTING

New contributors are always welcome! This document will guide you through the
process of setting up a development environment.

[LyricWiki](http://api.wikia.com/wiki/LyricWiki_API/REST) is currently the
only supported API.

[LYRICSnMUSIC](http://www.lyricsnmusic.com/api) used to be an option but it
appears to have been shut down. However, contributions for new API integrations
are especially welcome.


### Instructions

1. Fork the project and clone it on your computer.

1. Make a virtualenv, activate it, and then install the pip dependencies:

        $ pip install -r requirements-dev.txt

1. Run tests: 

        $ make test
        pytest tests/
        ============================= test session starts ==============================
        platform darwin -- Python 2.7.10, pytest-3.0.1, py-1.4.31, pluggy-0.3.1
        rootdir: /path/to/songtext, inifile: 
        collected 16 items

        tests/test_api_integrations.py ..............
        tests/test_local_options.py ..

        ========================== 16 passed in 6.42 seconds ===========================

1. Follow the [MuseScore Git workflow](http://musescore.org/en/developers-handbook/git-workflow)
as a guide to setting remotes, branching, committing, making pull requests,
etc.


### Writing your own integration

* Add your package to `libsongtext/` and then the package name to
`libsongtext/songtext.py`, in the `AVAILABLE_APIS` variable.

* To query your new API, use the `--api` option:

        $ songtext --api my-spiffy-api ...

* To query your new API by default, set the `SONGTEXT_DEFAULT_API`
environment variable and add this line somewhere sensible (e.g. `.bashrc` or
`.bash_profile` or some other shell startup file):

        export SONGTEXT_DEFAULT_API=my-spiffy-api

*Params:*

Other than the ones already used in LyricWiki (artist, song title), it is
also possible to make use of other params already defined in click:

* `all_fields` - this is for generic search (e.g. on artist name, song name, and lyrics). Search like so:

        $ songtext spice girls stop

* `words` - for searching on lyric text. Search using the `-w` or `--words`
flag:

        $ songtext -w 'sleeping is giving in'

* `list` - to return a list of results in order to refine your search (e.g.
if the lyrics returned were for the wrong song, or the requested lyrics
weren't available or some reason). Search using the`-l`/`--show-list` option:

        $ songtext -t colors -l

        40 track(s) matched your search query.


        Displaying the top 10 matches:
        ...

* `index` - for specifying the song that you want to select when searching
using a list. Search using the `-i`/`--index` option:

        $ songtext -t colors -i 7

        40 track(s) matched your search query.

        Halsey: Colors
        --------------
        Your little brother never tells you but he loves you so
        You said your mother only smiled on her TV show
        You're only happy when your sorry head is filled with dope
        I hope you make it to the day you're 28 years old

* `limit` - limit the number of matches returned in a list. Search using
the `--limit` option:

        $ songtext zayn befour -l --limit 5

        13 track(s) matched your search query.


        Displaying the top 5 matches:
        ...


### Tips

* Modify `README.md` and then run `make readme` to convert it to `README.rst`
for PyPI.

* Copy the git hook from `git-hooks/pre-commit` to `.git/hooks/pre-commit`,
which makes sure that you commit *both* `README.md` and `README.rst` whenever
a change is made to `README.md`.
