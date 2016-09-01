def format_song_info(artist, song_title):
    output = ""
    line1 = u'\n{0}: {1}\n'.format(artist, song_title)
    line2 = '{0}\n'.format('-' * (len(line1) - 2))
    output += line1
    output += line2
    return output
