# songtext

Get song lyrics in the command line.


## Usage

* Search all fields (artist name, song name, lyrics):

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
option (`-l, --list`) to return the top ten matches:

        $ ./songtext.py -t firework

        48 track(s) matched your search query.


        Alabama: Fireworks  # WRONG! I want the Katy Perry version.
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

    Looks like hit #6 is correct, so let's specify that with the index
    (`-i, --index`) option:

        $ ./songtext.py -t firework -i 6

        48 track(s) matched your search query.


        Katy Perry: Firework
        ---------------------

        Do you ever feel like a plastic bag
        Drifting thought the wind
        Wanting to start again

        ...

    That looks more correct.

