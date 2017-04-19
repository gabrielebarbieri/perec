__author__ = 'gabrielebarbieri'

import nltk
from nltk.corpus import cmudict
import json
from sql_interface import sql_session, Verse
import os
from datetime import datetime
from markovchain.markov import MarkovTree
from markovchain.csp import ConstraintChain
from collections import defaultdict
import logging

START_SYMBOL = '<s>'
END_SYMBOL = '</s>'


class Word:
    """
    Implement a word and all his metadata, like the POS tag and his pronunciation
    """
    pronunciations = None

    def __init__(self, word, pos, pronunciation=None):
        """
        Create a new word
        :param word: The actual word
        :param pos: the word's part of speech tag
        :param pronunciation: the word's pronunciation
        """
        self.content = word
        self.pos = pos
        self.pronunciation = pronunciation
        if not self.pronunciation:
            self._init_pronunciations()

    def _init_pronunciations(self):
        """
        Initialize the word pronunciation if is not done yet
        """
        if not Word.pronunciations:
            Word.pronunciations = cmudict.dict()
        try:
            self.pronunciation = Word.pronunciations[self.content.lower()][0]
        except KeyError:
            pass

    def __repr__(self):
        return '{:}/{:}'.format(self.content, self.pos)


def tag_sentence(sentence):
    """
    Do a part of speech tagging on the input sentence
    :param sentence: The sentence to tag
    :return: The tagged sentence as a list of Word
    """
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return [Word(tag[0], tag[1]) for tag in tagged]


def dump_sentence(sentence):
    """
    Dump a sentence (i.e. a list of Word) to a json representation
    :param sentence: The sentence to dump
    :return: the json representation
    """
    to_dump = [word.__dict__ for word in sentence]
    return json.dumps(to_dump)


def load_song_from_file(song_path):
    """
    Load a song from a file and pos tag all the verses
    :param song_path: the path of the file containing the song
    :return: the song as a list of list of Word
    """
    content = []
    with open(song_path) as song:
        for verse in song.readlines():
            verse = verse.strip()
            if verse:
                content.append(tag_sentence(verse))
    return content


def store_song(author, title, content):
    """
    Store a song on the corpus database
    :param author: the song author
    :param title: the song name
    :param content: the song content, as a list of list of Word
    """
    for i, verse in enumerate(content):
        sql_session.add(Verse(author=author, song=title, line=i, content=dump_sentence(verse)))
    sql_session.commit()


def store_corpus(author, corpus_path):
    """
    Store a whole corpus (i.e. a list of songs) on the corpus database
    :param author: the author of the corpus
    :param corpus_path: the path of the folder containing the corpus
    """
    t = datetime.now()
    files = os.listdir(corpus_path)
    tot = len(files)
    for i, f in enumerate(files):
        if f.endswith('.txt'):
            title = f[:-4]
            print '{:>4}/{:} {:}'.format(i+1, tot, title)
            song_path = os.path.join(corpus_path, f)
            try:
                content = load_song_from_file(song_path)
                store_song(author, title, content)
            except:
                print 'Error loading song {:} from {:}'.format(title, song_path)
    print 'Time to load {:} corpus: {:}'.format(author, datetime.now() - t)


class Corpus:

    def __init__(self, author):
        self.author = author
        self.pos_patterns = defaultdict(list)
        self.pos_map = defaultdict(set)
        self.markov_tree = MarkovTree(5)
        self._logger = logging.getLogger(__name__)
        self._fill_corpus()

    def _fill_corpus(self):
        t = datetime.now()

        for verse in sql_session.query(Verse).filter_by(author=self.author):
            pos_tags = []
            content = [START_SYMBOL]
            for w in json.loads(verse.content):
                word = w['content']
                pos = w['pos']
                pos_tags.append(pos)
                self.pos_map[pos].add(word)
                content.append(word)
            content.append(END_SYMBOL)
            self.markov_tree.parse(content)
            self.pos_patterns[len(pos_tags)].append(pos_tags)
        self._logger.info('time to create {:} corpus: {:}'.format(self.author, datetime.now() - t))


if __name__ == '__main__':


    import sys
    FORMAT = '[%(levelname).1s] %(asctime)s.%(msecs)d %(name)s: %(message)s'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(level=logging.INFO, format=FORMAT, stream=sys.stdout, datefmt=DATE_FORMAT)


    import random
    c = Corpus('Dylan')

    outs = []
    for i in xrange(10):

        try:
            pattern = random.choice(c.pos_patterns[10])
            vs = [[START_SYMBOL]]
            for pos in pattern:
                vs.append(c.pos_map[pos])
            vs.append([END_SYMBOL])

            csp = ConstraintChain(vs, c.markov_tree)
            seq, orders = csp.get_sequence_and_order()
            outs.append(' '.join(seq[1:-1]))
        except:
            pass

    for o in outs:
        logging.info(o)
