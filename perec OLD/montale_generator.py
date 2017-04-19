__author__ = 'Gabriele'

import json
from markovchain.markov import MarkovTree
from markovchain.csp import ConstraintChain
from collections import defaultdict
import logging
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


START_SYMBOL = '<s>'
END_SYMBOL = '</s>'

grammar = defaultdict(list)
pos_dict = defaultdict(list)
alphabet = defaultdict(int)

mt = MarkovTree(5)
with open('mont_tag.txt') as f:
    for l in f.readlines():
        try:
            sentence = [START_SYMBOL]
            pattern = []
            for w in json.loads(l)['tags']:
                word = w['word']
                sentence.append(word)
                pos = w['POS']
                pattern.append(pos)
                pos_dict[pos].append(word)
                alphabet[word] += 1

            grammar[len(pattern)].append(pattern)
            sentence.append(END_SYMBOL)
            mt.parse(sentence)
        except ValueError:
            pass

seqs = []
l = 10
variables = [[START_SYMBOL]]
for i in xrange(5):
    variables.append(alphabet.keys())
variables.append([END_SYMBOL])

c = ConstraintChain(variables, mt)
c.achieve_dac()
print c.get_sequence_and_order()
