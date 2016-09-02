# CONTRIBUTING

New contributors are always welcome! This document will guide you through the
process of setting up a development environment.


### Instructions

1. Fork the project and clone it on your computer.

1. Make a virtualenv, activate it, and then install the pip dependencies:

        $ pip install -r requirements.txt

1. If you don't already have a LYRICSnMUSIC API key, get one here: 
<http://www.lyricsnmusic.com/api_keys/new>

    And then add it to one of your bash startup scripts, e.g. 

        $ echo 'export LYRICSNMUSIC_API_KEY=my_thirty_character_alphanumeric_api_key' >> ~/.bashrc.local

    Make sure to source it before continuing, e.g. `source ~/.bashrc.local`

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


### Tips

* You may want to grab this [git pre-commit hook](https://gist.github.com/ysim/9195375)
which makes sure that you commit *both* `README.md` and `README.rst` whenever
a change is made to `README.md`.
