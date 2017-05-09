from nlp_tools import tokenize_corpus
from markovchain import markov_chain
from markovchain.suffix_tree import get_suffix_tree
from datetime import datetime


class Sentence(object):

    def __init__(self, words, orders):
        self.words = words
        self.orders = orders

    def __repr__(self):
        return ' '.join(self.words[1:-1])


class Corpus(object):

    def __init__(self, corpus_folder, order=3):
        self.corpus_folder = corpus_folder
        t = datetime.now()
        self.sentences = tokenize_corpus(corpus_folder)
        print 'time to tokenize the corpus', datetime.now() - t

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

if __name__ == '__main__':
    dylan = Corpus('data/Dylan')
    cts = ['<s>'] + [None] * 5 + [
        ['loved', 'adore', 'loves', 'passion', 'hate', 'loving', 'affection']] + [None] * 5 + ['</s>']
    for seq in dylan.generate_sentences(cts):
        print str(seq) + ' (ord:{})'.format(seq.orders)
