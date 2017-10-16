from nlp_tools import tokenize_corpus, get_semantic_model
from markovchain import markov_chain
from markovchain.suffix_tree import get_suffix_tree
from datetime import datetime
from random import shuffle
import json
import os
from dylan_popularity import get_most_popular_songs


class Sentence(object):

    def __init__(self, words, orders):
        self.words = words
        self.orders = orders

    def __repr__(self):
        return ' '.join([w for w in self.words if w not in {'<s>', '</s>'}])


class Corpus(object):

    def __init__(self, corpus, order=3, replace_dict=None):
        t = datetime.now()

        if isinstance(corpus, str):
            corpus = [os.path.join(corpus, f) for f in os.listdir(corpus)]

        self.sentences = tokenize_corpus(corpus, replace_dict)
        print 'time to tokenize {} sentences {}'.format(len(self.sentences), datetime.now() - t)

        t = datetime.now()
        self.matrices = markov_chain.parse_sequences(self.sentences, order)
        print 'time to estimate the matrices', datetime.now() - t

        t = datetime.now()
        self.suffix_tree = get_suffix_tree(self.sentences)
        print 'time to compute the suffix tree', datetime.now() - t

    def generate_sentences(self, constraints, n=10):
        t = datetime.now()
        mp = markov_chain.get_markov_process(self.matrices, constraints)
        print 'time to compute the markov process', datetime.now() - t
        sentences = []
        for _ in xrange(n):
            sequence = markov_chain.generate(mp)
            orders = self.suffix_tree.get_all_orders(sequence)
            sentences.append(Sentence(sequence, orders))
        return sentences

    def generate_semantic_sentence(self, sense, length, n):
        words = [w[0] for w in get_semantic_model().most_similar(sense)]
        indices = range(length)
        shuffle(indices)
        for i in indices:
            try:
                cts = ['<s>'] + [None] * i + [words] + [None] * (length - i - 1) + ['</s>']
                return self.generate_sentences(cts, n)
            except RuntimeError:
                pass

    def to_json(self, output):
        with open(output, 'w') as f:
            json.dump({'sentences': self.sentences}, f)

if __name__ == '__main__':
    sources = get_most_popular_songs(40)
    dylan = Corpus(sources, order=2)
    out = '/Users/gabriele/Workspace/misc/redylan/src/core/dylan_matrices.json'
    markov_chain.serialize_process(dylan.matrices, out)
    song = [dylan.generate_semantic_sentence(s, 10, 10) for s in ['god', 'save', 'queen', 'love', 'peace', 'war']]
    for i in xrange(10):
        print
        for s in song:
            if s:
                print s[i]
