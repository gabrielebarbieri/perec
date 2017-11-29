import pandas as pd
import editdistance
import os


DYLAN_DATA = 'data/Dylan'
DYLAN_POPULARITY = 'data/dylan_popularity.csv'


class Closer(object):

    def __init__(self, folder):
        self.folder = folder
        self._short_names = None

    @property
    def short_song_names(self):
        if self._short_names is None:
            self._short_names =[f[:-4] for f in os.listdir(DYLAN_DATA)]
        return self._short_names

    def closest(self, full_name):
        d = {n: editdistance.eval(n, clean_name(full_name)) for n in self.short_song_names}
        return '{}.txt'.format(min(d, key=d.get))


def clean_name(name):
    return name.split('-')[0].strip().lower()


def get_most_popular_songs(n=5):
    df = pd.read_csv(DYLAN_POPULARITY)
    return [os.path.join(DYLAN_DATA, f) for f in df.file.head(n)]
