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

    $ songtext --api lyricsnmusic taylor swift bad blood

    48 track(s) matched your search query.


    Taylor Swift: Bad Blood
    ------------------------

    'Cause baby now we got bad blood
    You know it used to be mad love
    So take a look at what you've done
    'Cause baby now we got bad blood


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
| `-l`, `--list`              | No          | Yes            |
| `-i`, `--index`             | No          | Yes            |

(See the section below for more [usage notes on the
APIs](https://github.com/ysim/songtext#notes-on-the-apis).)


### LyricWiki & LYRICSnMUSIC

* Search by **artist name** (`-a, --artist`) and **song title**
(`-t, --title`) -- optional for LYRICSnMUSIC, both mandatory for LyricWiki.

        $ songtext -a wir sind helden -t ein elefant für dich

        9 track(s) matched your search query.


        Wir Sind Helden: Ein Elefant für Dich
        --------------------------------------

        Ich seh uns beide, do bist längst zu schwer
        Für meine Arme, aber ich geb dich nicht her
        Ich weiß, deine Monster sind genau wie meine
        und mit denen bleibt man besser nicht alleine
        Ich weiß, ich weiß, ich weiß und frage nicht
        Halt dich bei mir fest, steig auf, ich trage dich


### LYRICSnMUSIC *only*

All examples assume LYRICSnMUSIC as the default API.


* Search **all fields** (artist name, song name, lyrics):

        $ songtext johnny flynn tickle me pink

        9 track(s) matched your search query.


        Johnny Flynn: Tickle Me Pink
        -----------------------------

        Tickle me pink
        I'm rosy as a flushed red apple skin
        Except I've never been as sweet
        I've rolled around the orchard
        And found myself too awkward
        And tickle me green I'm too naive

* Search by **lyric text**  (`-w, --words`): 

        $ songtext -w sleeping is giving in

        23 track(s) matched your search query.


        Arcade Fire: Rebellion (Lies)
        ------------------------------

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

        $ songtext -t firework

        48 track(s) matched your search query.


        Alabama: Fireworks
        -------------------

        There are people in this country who work hard every day
        Not for fame or fortune do they strive
        But the fruits of their labor are worth more than their pay
        And it's time a few of them were recognized

    WRONG! I wanted the Katy Perry version. Let's see the list of matches that
    is returned from searching for the song title "firework":

        $ songtext -t firework -l

        48 track(s) matched your search query.


        Displaying the top 10 matches:

        0. Alabama: Fireworks
           ("There are people in this country who work hard every day"...)
        1. Siouxsie and the Banshees: Fireworks
           ("The body is wrapped in shadow"...)
        2. Alicia Keys and Drake: Fireworks
           ("Money just changed everything, I wonder how life without it would go"...)
        3. Alicia Keys and Drake: Fireworks
           ("Oh, all I see is fireworks"...)
        4. Alicia Keys and Drake: Fireworks
           ("Oh, all I see is fireworks"...)
        5. Blue Öyster Cult: Fireworks
           ("She went down to her house by the water"...)
        6. Katy Perry: Firework
           ("Do you ever feel like a plastic bag"...)
        7. Katy Perry: Firework
           ("Do you ever feel like a plastic bag"...)
        8. Kidz Bop Kids: Firework
           ("Do you ever feel like a plastic bag"...)
        9. Lea Michele: Firework
           ("Do you ever feel like a plastic bag"...)

    Looks like hit #6 is correct, so let's specify that with the **index
    option** (`-i, --index`):

        $ songtext -t firework -i 6

        48 track(s) matched your search query.


        Katy Perry: Firework
        ---------------------

        Do you ever feel like a plastic bag
        Drifting thought the wind
        Wanting to start again

    That's better.

* Optionally, pass one integer argument to the **list** option to limit the
number of matches returned in the list:

        $ songtext laura marling rambling man -l 5

        24 track(s) matched your search query.


        Displaying the top 5 matches:

        0. Laura Marling: Rambling Man
           ("Oh naive little me"...)
        1. Laura Marling: Blackberry Stone
           ("Well I, own this field"...)
        2. Laura Marling: Darkness Descends
           ("You're holding bits of styrofoam"...)
        3. Laura Marling: Hope in the Air
           ("There is a man that I know"...)
        4. Laura Marling: Alpha Shallows
           ("He could fall and she could weep"...)

    Note that because it is optional and *may* take one argument, if you're
    using this option without an argument before any position arguments
    (QUERY), you will have to separate them with two dashes (`--`) to indicate
    the end of the optional arguments so the shell will not consume the first
    word of the positional argument[s] as the argument for the list option.
    For example:

        $ songtext -l josh ritter snow is gone
        usage: songtext.py [-h] [-l [NUM_MATCHES]] [-i INDEX]
        [-a ARTIST_NAME [ARTIST_NAME ...]]
        [-t SONG_TITLE [SONG_TITLE ...]] [-w LYRICS [LYRICS ...]]
        [--api API_MODULE]
        [QUERY [QUERY ...]]
        songtext.py: error: argument -l/--list: invalid int value: 'josh'
        $ songtext -l -- josh ritter snow is gone

        34 track(s) matched your search query.


        Displaying the top 10 matches:

        0. Josh Ritter: Snow Is Gone
           ("Birds beneath my window dusting their wings upon the lawn"...)
        1. Josh Ritter: Snow Is Gone [Live][*]
           ("Birds beneath my window dusting their wings upon the lawn"...)
        2. Josh Ritter: Morning Is a Long Way Down
           ("Wrap your arms around me"...)
        3. Josh Ritter: Horrible Qualities/Stuck to You
           ("There's one thing, mama,"...)
        4. Josh Ritter: Last Ditch Effort
           (""...)
        5. Josh Ritter: Paths Will Cross
           ("This is it my dear old friend"...)
        6. Josh Ritter: Hotel Song
           ("Sunday night, its supper time, the hotel?s full and all is fine."...)
        7. Josh Ritter: Potters Wheel
           ("I close my eyes and it all returns like the spinning of a potter's wheel"...)
        8. Josh Ritter: Love Is Making Its Way Back Home
           ("Dot paths the moonly road"...)
        9. Josh Ritter: Last Ditch Effort (See You Try)
          ("You have chosen dawn to leave"...)


## Notes on the APIs

* **LyricWiki** seems to return more accurate single-track matches when you
know exactly what you're looking for. The only downside is that you need to be
able to spell out the artist name and track title accurately and in full.

    For example:

        $ songtext --api lyricwiki -a interpol -t stella was a diver

        Your query did not match any tracks.


        $ songtext --api lyricwiki -a interpol -t stella was a diver and she was always down

        Interpol: Stella Was A Diver And She Was Always Down
        ------------------------------------------------------

        (This one's called Stella Was A Diver And She Was Always Down)

        When she walks down the street
        She knows there's people watching
        The building fronts are just fronts
        To hide the people watching her

* **LYRICSnMUSIC** is more forgiving if you don't know the full track name or
you don't know either the artist or the track title, since it supports generic
searches (i.e. on all fields). However, it sometimes returns the unobvious
match for a search query, e.g.

        $ songtext --api lyricsnmusic stairway to heaven

        48 track(s) matched your search query.


        Neil Sedaka: Stairway to Heaven
        --------------------------------

        Climb up, way up high
        Climb up, way up high
        Climb up, way up high


## Author

* Yi Qing Sim ([@yiqingsim](https://twitter.com/yiqingsim/))
