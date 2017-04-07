|Build Status|

songtext
========

A command-line song lyric fetcher.

Inspired by `@gleitz <https://twitter.com/gleitz>`__'s
`howdoi <https://github.com/gleitz/howdoi>`__. Name from the `German
word for
"lyrics" <http://www.dict.cc/deutsch-englisch/Songtext.html>`__.

**APIs:**

`LyricWiki <http://api.wikia.com/wiki/LyricWiki_API/REST>`__ is
currently the only supported API.

`LYRICSnMUSIC <http://www.lyricsnmusic.com/api>`__ used to be an option
but it appears to have been shut down. However,
`contributions <CONTRIBUTING.md>`__ are always welcome, especially for
new API integrations.

Installation
------------

With pip:

::

    $ pip install songtext

With distutils:

::

    $ python setup.py install

Usage
-----

Search by both **artist name** (``-a, --artist``) *and* **song title**
(``-t, --title``):

::

        $ songtext -a pvris -t fire

        PVRIS: Fire
        -----------
        Don't blame your death on the shit in your head
        That you claimed ate you like a virus for days on end
        I watched you decay, watched you waste away
        Who'd you think you'd fool, baby, diggin' your own grave?

Note that option values that consist of more than one word need to be
quoted:

::

        $ ./songtext -a 'nina simone' -t sinnerman

        Nina Simone: Sinnerman
        ----------------------
        Oh sinnerman, where you gonna run to?
        Sinnerman, where you gonna run to?
        Where you gonna run to?
        All along dem day

Note that paging is turned on by default. Use the ``--no-pager`` flag to
turn it off.

+-------------------------------+-----------------+
| argument/API                  | ``lyricwiki``   |
+===============================+=================+
| positional (generic search)   | No              |
+-------------------------------+-----------------+
| ``-a``, ``--artist``          | Yes             |
+-------------------------------+-----------------+
| ``-t``, ``--title``           | Yes             |
+-------------------------------+-----------------+
| ``-w``, ``--words``           | No              |
+-------------------------------+-----------------+
| ``-l``, ``--show-list``       | No              |
+-------------------------------+-----------------+
| ``--limit``                   | No              |
+-------------------------------+-----------------+
| ``--no-pager``                | Yes             |
+-------------------------------+-----------------+
| ``-i``, ``--index``           | No              |
+-------------------------------+-----------------+

Author
------

-  Yi Qing Sim (`@ysim <https://github.com/ysim/>`__)

.. |Build Status| image:: https://travis-ci.org/ysim/songtext.svg?branch=master
   :target: https://travis-ci.org/ysim/songtext
