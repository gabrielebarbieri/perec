from nlp_tools import tokenize_corpus, get_semantic_model
from markovchain import markov_chain
from markovchain.suffix_tree import get_suffix_tree
from datetime import datetime
from random import shuffle


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

        pass
if __name__ == '__main__':
    dylan = Corpus('data/Dylan')

    song = [dylan.generate_semantic_sentence(s, 10, 10) for s in ['god', 'save', 'queen', 'love', 'peace', 'war']]
    for i in xrange(10):
        print
        for s in song:
            print s[i]
