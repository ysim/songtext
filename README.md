# songtext

A command-line song lyric fetcher.

Inspired by [@gleitz](https://twitter.com/gleitz)'s
[howdoi](https://github.com/gleitz/howdoi). Name from the [German word for
"lyrics"](http://www.dict.cc/deutsch-englisch/Songtext.html).


## Usage

**Note:** Not all the APIs support all of these options.

* Search **all fields** (artist name, song name, lyrics):

        $ ./songtext.py johnny flynn tickle me pink

        9 track(s) matched your search query.


        Johnny Flynn: Tickle Me Pink
        -----------------------------

        Tickle me pink
        I'm rosy as a flushed red apple skin
        Except I've never been as sweet
        I've rolled around the orchard
        And found myself too awkward
        And tickle me green I'm too naive

        ...

* Optionally, search by **artist name** (`-a, --artist`), **song title**
(`-t, --title`), and/or the **words in the lyrics** (`-w, --words`): 

        $ ./songtext.py -a wir sind helden -t ein elefant für dich

        9 track(s) matched your search query.


        Wir Sind Helden: Ein Elefant für Dich
        --------------------------------------

        Ich seh uns beide, do bist längst zu schwer
        Für meine Arme, aber ich geb dich nicht her
        Ich weiß, deine Monster sind genau wie meine
        und mit denen bleibt man besser nicht alleine
        Ich weiß, ich weiß, ich weiß und frage nicht
        Halt dich bei mir fest, steig auf, ich trage dich

        ...

* To refine your search (e.g. if the lyrics returned were for the wrong song,
or the requested lyrics weren't viewable for some other reason), use the list
option (`-l, --list`), which will return the top ten matches by default:

        $ ./songtext.py -t firework

        48 track(s) matched your search query.


        Alabama: Fireworks
        -------------------

        There are people in this country who work hard every day
        Not for fame or fortune do they strive
        But the fruits of their labor are worth more than their pay
        And it's time a few of them were recognized

        ...

    WRONG! I wanted the Katy Perry version. Let's see the list of matches that
    is returned from searching for the song title "firework":

        $ ./songtext.py -t firework -l

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

        $ ./songtext.py -t firework -i 6

        48 track(s) matched your search query.


        Katy Perry: Firework
        ---------------------

        Do you ever feel like a plastic bag
        Drifting thought the wind
        Wanting to start again

        ...

    That looks more correct.

* You can also pass one integer argument to the **list** option to limit the
  number of matches returned in the list:

        $ ./songtext.py laura marling rambling man -l 5

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

        $ ./songtext.py -l josh ritter snow is gone
        usage: songtext.py [-h] [-l [NUM_MATCHES]] [-i INDEX]
        [-a ARTIST_NAME [ARTIST_NAME ...]]
        [-t SONG_TITLE [SONG_TITLE ...]] [-w LYRICS [LYRICS ...]]
        [--api API_MODULE]
        [QUERY [QUERY ...]]
        songtext.py: error: argument -l/--list: invalid int value: 'josh'
        $ ./songtext.py -l -- josh ritter snow is gone

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

* Select a different API with the `--api` option, e.g.

        $ ./songtext.py --api lyricwiki -a andrew bird -t armchairs

        Andrew Bird: Armchairs
        ------------------------

        I dreamed you were a cosmonaut
        of the space between our chairs
        and I was a cartographer
        of the tangles in your hair

        ...


## Supported arguments options by API

| argument         | `--api lyricsnmusic` | `--api lyricwiki` |
| ---------------- | --------------------:| -----------------:|
| positional       | Yes                  | No                |
| `-a`, `--artist` | Yes                  | Yes (Mandatory)   |
| `-t`, `--title`  | Yes                  | Yes (Mandatory)   |
| `-w`, `--words`  | Yes                  | No                |
| `-l`, `--list`   | Yes                  | No                |
| `-i`, `--index`  | Yes                  | No                |


## Supported APIs

* [LYRICSnMUSIC](http://www.lyricsnmusic.com/api)
* [LyricWiki](http://api.wikia.com/wiki/LyricWiki_API/REST)
* Coming soon: [ChartLyrics](http://www.chartlyrics.com/api.aspx)


## Author

Yi Qing Sim ([@yiqingsim](https://twitter.com/yiqingsim/))
