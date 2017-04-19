# -*- coding: utf-8 -*-

import re
from subprocess import Popen, PIPE
import urllib2
import wikitionary
import json
import codecs


class PosTagger():

    def __init__(self):
        self.args = ['bin/tree-tagger', '-token', '-lemma', '-sgml', '-no-unknown', 'models/italian-utf8.par']
        pass

    def tag(self, sentence):
        to_tag = '\n'.join(re.findall(r"[\wàèéìòù]+|[^\w\s]", sentence))
        p = Popen(self.args, stdout=PIPE, stdin=PIPE)
        tags = []
        for line in p.communicate(to_tag)[0].split('\r\n'):
            if line:
                s = line.split('\t')
                tags.append({'word': s[0], 'POS': s[1], 'lemma': s[2]})
        return tags


class Syllabator():

    def __init__(self):
        self.process = Popen(['node', 'bin/sillabatore.js'])
        self.prefix = "http://127.0.0.1:8000/"

    def get_syllables(self, word):
        s = wikitionary.get_syllables(word)
        if s:
            return s[0]
        for i in xrange(10):
            try:
                return urllib2.urlopen(self.prefix + word).read().split('-')
            except urllib2.HTTPError:
                pass

    def __del__(self):
        self.process.terminate()


def tag_file(input_file, output_file):
    tagger = PosTagger()
    with open(input_file) as f_in:
        with open(output_file, 'w') as f_out:
            lines = f_in.readlines()
            tot = len(lines)
            for i, sentence in enumerate(lines):
                print "{:}/{:}".format(i, tot)
                d = sentence
                if sentence.strip():
                    tagged = {'sentence': sentence.strip(),
                              'tags': tagger.tag(sentence.replace('ó', 'o').replace('È', 'è').replace('î', 'i'))}

                    d = json.dumps(tagged) + '\n'
                f_out.write(d)


def get_syllables_from_file(input_file):
    words = set()
    syl = Syllabator()
    with open(input_file) as f:
        for l in f.readlines():
            if l.strip():
                tags = json.loads(l.strip())['tags']
                for tag in tags:
                    words.add(tag['word'].lower())
    tot = len(words)
    syllables_dict = {}
    for i, w in enumerate(words):
        print "{:}/{:}".format(i, tot)
        syllables_dict[w] = syl.get_syllables(codecs.encode(w, 'utf8'))

    return syllables_dict
