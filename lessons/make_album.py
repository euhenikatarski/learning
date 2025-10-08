def make_albums(author, song, time='', **kwargs):
    kwargs['author'] = author
    kwargs['song'] = song
    kwargs['time'] = time
    return kwargs

