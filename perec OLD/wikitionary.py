__author__ = 'Gabriele'

import urllib2
import re
import string

BETWEEN_PARENTHESIS_RE = re.compile('\(.*\)')
BETWEEN_BRACKETS_RE = re.compile('\[\[[\w]*\]\]')
FIND_SIN_RE = re.compile('\{\{-sin-\}\}[^{]*\{\{')

_table = string.maketrans("", "")
_cached_pages = {}


def _clean_syllables(s):
    return BETWEEN_PARENTHESIS_RE.sub('', s).translate(_table, string.punctuation).strip()


def get_page(word):
    try:
        return _cached_pages[word]
    except KeyError:
        try:
            data = urllib2.urlopen('http://it.wiktionary.org/w/index.php?title=' + word + '&action=raw').read()
        except urllib2.HTTPError:
            data = None
        _cached_pages[word] = data
        return data


def get_syllables(word):
    data = get_page(word)
    if data:
        return [[_clean_syllables(s) for s in line.split(' | ')] for line in data.split('\n') if " | " in line]


def get_synonyms(word):
    data = get_page(word)
    if data:
        m = FIND_SIN_RE.search(data)
        if m:
            return [s.replace('[', '').replace(']', '') for s in BETWEEN_BRACKETS_RE.findall(m.group())]

