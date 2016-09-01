[![Build Status](https://travis-ci.org/ysim/songtext.svg?branch=master)](https://travis-ci.org/ysim/songtext)

# songtext

A command-line song lyric fetcher.

Inspired by [@gleitz](https://twitter.com/gleitz)'s
[howdoi](https://github.com/gleitz/howdoi). Name from the [German word for
"lyrics"](http://www.dict.cc/deutsch-englisch/Songtext.html).

**Supported APIs:**

* [LyricWiki](http://api.wikia.com/wiki/LyricWiki_API/REST) (default)
* [LYRICSnMUSIC](http://www.lyricsnmusic.com/api)

**Note:** Where the lyrics have been returned below in examples, the body of
the lyric text has been truncated after the first paragraph.


## Installation

With pip:

    $ pip install songtext

With distutils:

    $ python setup.py install


## Configuration

The LyricWiki API is turned on by default. The LYRICSnMUSIC API is also
supported, however it requires an API key; you can generate one easily here: 

<http://www.lyricsnmusic.com/api_keys/new> 

You will need to export the `LYRICSNMUSIC_API_KEY` environment variable for
queries to this API to work, and probably want to add this line to one of
your shell startup files (e.g. `.bashrc` or `.bash_profile`), like so:

    export LYRICSNMUSIC_API_KEY=<your lyricsnmusic api key>

To query the LYRICSnMUSIC API just for the command you're running, use the
`--api` option, e.g. 

    $ songtext --api lyricsnmusic kashmir

    40 track(s) matched your search query.


    Led Zeppelin: Kashmir
    ---------------------
    Oh, let the sun beat down upon my face
    And stars fill my dream
    I'm a traveler of both time and space
    To be where I have been
    To sit with elders of the gentle race
    This world has seldom seen
    They talk of days for which they sit and wait
    All will be revealed

To query the LYRICSnMUSIC API by default, set the `SONGTEXT_DEFAULT_API`
environment variable and add this line somewhere sensible (like you did for the
`LYRICSNMUSIC_API_KEY` above):

    export SONGTEXT_DEFAULT_API=lyricsnmusic


## Usage

| argument/API                | `lyricwiki` | `lyricsnmusic` |
| --------------------------  | -----------:| --------------:|
| positional (generic search) | No          | Yes            |
| `-a`, `--artist`            | Yes         | Yes            |
| `-t`, `--title`             | Yes         | Yes            |
| `-w`, `--words`             | No          | Yes            |
| `-l`, `--show-list`         | No          | Yes            |
| `--limit`                   | No          | Yes            |
| `--no-pager`                | Yes         | Yes            |
| `-i`, `--index`             | No          | Yes            |

(See the section below for more [usage notes on the
APIs](https://github.com/ysim/songtext#notes-on-the-apis).)

Note that option values that consist of more than one word need to be quoted
as of v0.1.6.


### LyricWiki & LYRICSnMUSIC

* Search by both **artist name** (`-a, --artist`) *and* **song title**
(`-t, --title`) -- optional (but highly recommended) for LYRICSnMUSIC,
mandatory for LyricWiki:

        $ songtext -a pvris -t fire

        PVRIS: Fire
        -----------
        Don't blame your death on the shit in your head
        That you claimed ate you like a virus for days on end
        I watched you decay, watched you waste away
        Who'd you think you'd fool, baby, diggin' your own grave?

* Paging is turned on by default. Use the `--no-pager` flag to turn it off.


### LYRICSnMUSIC *only*

All the examples in this section assume LYRICSnMUSIC as the default API
(i.e. omit `--api lyricsnmusic`).


* Search **all fields** (artist name, song name, lyrics):

        $ songtext spice girls stop

        43 track(s) matched your search query.


        Spice Girls: Stop
        -----------------
        You just walk in, I make you smile
        It's cool but
        You don't even know me
        You take an inch, I run a mile
        Can't win you're
        Always right behind me
        And we know that you could go and find some other
        Take or leave it or just don't even bother
        Caught in a craze, it's just a phase
        Or will this be around forever
        Don't you know it's going too fast (ooh, to fast)
        Racing so heard you know it won't last (ooh, won't last)
        Don't you know why can't you see
        Slow it down, read the sign
        So you know just where you're going

* Search by **lyric text**  (`-w, --words`): 

        $ songtext -w 'sleeping is giving in'

        15 track(s) matched your search query.


        Arcade Fire: Rebellion (Lies)
        -----------------------------
        Sleeping is giving in, 
        No matter what the time is. 
        Sleeping is giving
        In, so lift those heavy eyelids.
        People say that you'll die faster than without water. 
        But we know it's just a lie, 
        Scare your son and scare your daughter.
        People say that your dreams are the only things that save ya.
        Come on baby in our dreams, 
        We can live our misbehavior.
        Every time you close your eyes lies, lies!
        People try and hide the night underneath the covers.
        People try and hide the light underneath the covers.

* Use the **list option** (`-l, --list`) to refine your search (e.g. if the
lyrics returned were for the wrong song, or the requested lyrics weren't
viewable for some other reason). It will return the top ten matches by default.

        $ songtext -t colors

        40 track(s) matched your search query.


        Ice-T: Colors
        -------------
        Yo Ease let's do this

        I am a nightmare walking, psychopath talking
        King of my jungle just a gangster stalking
        Living life like a firecracker quick is my fuse
        Then dead as a deathpack the colors I choose
        Red or Blue, 'cause or Blood, it just don't matter
        Sucker die for your life when my shotgun scatters
        We gangs of L.A. will never die - just multiply

    WRONG! I wanted the Halsey version. Let's see the list of matches that is
    returned from searching for the song title "colors":

        $ songtext -t colors -l

        40 track(s) matched your search query.


        Displaying the top 10 matches:

          0. Ice-T: Colors
             ("Yo Ease let's do this"...)
          1. Ice-T: Colors
             ("Yo Ease let's do this..."...)
          2. The Oak Ridge Boys: Colors
             ("Red as the bloodshed, blue as the wounded, white as the crosses on our soldier's graves. Through the rain, through the sun, these colors never run."...)
          3. Mary J. Blige: Color
             ("It took a long time to get to this place"...)
          4. Coheed and Cambria: Colors
             ("I walk so tired, so opaque"...)
          5. Gucci Mane: Colors (full lyrics unavailable)
          6. The Game and Sean Kingston: Colors
             ("[Chorus]"...)
          7. Halsey: Colors
             ("Your little brother never tells you but he loves you so"...)
          8. Amos Lee: Colors (full lyrics unavailable)
          9. Call & Response: Colors
             ("Sitting on the green green grass"...)

    Looks like hit #7 is correct, so let's specify that with the **index
    option** (`-i, --index`):

        $ songtext -t colors -i 7

        40 track(s) matched your search query.

        Halsey: Colors
        --------------
        Your little brother never tells you but he loves you so
        You said your mother only smiled on her TV show
        You're only happy when your sorry head is filled with dope
        I hope you make it to the day you're 28 years old

    That's better.

* Optionally, pass an integer argument to `--limit` option to limit the
number of matches returned in the list:

        $ songtext zayn befour -l --limit 5

        13 track(s) matched your search query.


        Displaying the top 5 matches:

          0. ZAYN: BeFoUr
             ("I've done this before"...)
          1. BeFour: All 4 One
             ("All 4 one and one 4 all"...)
          2. BeFour: Cosmic Ride
             ("Dum dam da di da di dai"...)
          3. BeFour: Zero Gravity
             ("I start the engine of my rocket"...)
          4. BeFour: A New Generation
             ("You're the voice of a new generation"...)


## Notes on the APIs

* **LyricWiki** seems to return more accurate single-track matches when you
know exactly what you're looking for. The only downside is that you need to be
able to spell out the artist name and track title accurately and in full.

    For example:

        $ songtext --api lyricwiki -a interpol -t stella was a diver

        Your query did not match any tracks.


        $ songtext --api lyricwiki -a interpol -t 'stella was a diver and she was always down'

        Interpol: Stella Was A Diver And She Was Always Down
        ----------------------------------------------------

        This one's called 'Stella was a diver and she is always down'

        When she walks down the street
        She knows there's people watching
        The building fronts are just fronts
        To hide the people watching her

* **LYRICSnMUSIC** might be the better option if you aren't completely sure
of your search terms, since it provides the option of listing the possible
hits. It is recommended that you use the individual search fields rather than
the generic search (on all fields), which is rather janky and often does not
return the obvious result:

        $ songtext --api lyricsnmusic britney spears baby one more time

        48 track(s) matched your search query.


        The Time: The Bird
        ------------------
        Hold on, hold on, why y'all beatin' on shit, what's that mean?
        Hold up, do y'all wanna learn a new dance?
        Are you qualified to learn one? That's what I thought
        Who can dance out there? Okay, we gonna try a new dance
        And if I don't see everybody doin' it, I don't wanna see you no more
        Jellybean, are we ready? y'all better do this one
        What time is it? Alright, y'all got 10 seconds
        To get to the dance floor and whawk


## Author

* Yi Qing Sim ([@yiqingsim](https://twitter.com/yiqingsim/))
