from nlp_tools import tokenize_corpus, get_semantic_model, get_all_rhymes
from markovchain import markov_chain
from markovchain.suffix_tree import get_suffix_tree
from datetime import datetime
from random import shuffle
import json
import os
from dylan_popularity import get_most_popular_songs
import operator


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

        self._words = None
        self._rhymes = None

    @property
    def words(self):
        if self._words is None:
            self._words = list(set(w for sentence in self.sentences for w in sentence))
        return self._words

    @property
    def rhymes(self):
        if self._rhymes is None:
            self._rhymes = get_all_rhymes(self.words)
        return self._rhymes

    def generate_sentences(self, constraints, n=10):
        # t = datetime.now()
        mp = markov_chain.get_markov_process(self.matrices, constraints)
        # print 'time to compute the markov process', datetime.now() - t
        sentences = []
        for _ in xrange(n):
            sequence = markov_chain.generate(mp)
            orders = self.suffix_tree.get_all_orders(sequence)
            sentences.append(Sentence(sequence, orders))
        return sentences

    def generate_semantic_sentence(self, sense, length, n, rhyme=None):
        words = [w[0] for w in self.get_similar_words(sense)]
        rhymes = self.rhymes.get(rhyme, None)
        indices = range(length)
        shuffle(indices)
        for i in indices:
            try:
                cts = ['<s>'] + [None] * i + [words] + [None] * (length - i - 1) + [rhymes] +['</s>']
                return self.generate_sentences(cts, n)
            except RuntimeError:
                pass

    def to_json(self, output):
        with open(output, 'w') as f:
            json.dump({'sentences': self.sentences}, f)

    def get_similar_words(self, sense, n=10):
        similarities = {}
        for w in self.words:
            try:
                similarities[w] = get_semantic_model().similarity(sense, w)
            except KeyError:
                pass
        return [k for k, _ in sorted(similarities.items(), key=operator.itemgetter(1), reverse=True)[:n]]

    def save_all_rhymes(self, destination_path):
        with open(destination_path, 'w') as f:
            json.dump(self.rhymes, f)


def recompute_redylan_similarities():
    corpus = Corpus(get_most_popular_songs(40), order=2)
    import json
    p = '/Users/gabriele/Workspace/misc/redylan/src/core/word_similarities.json'
    with open(p) as f:
        words = json.load(f).keys()

    from tqdm import tqdm
    sims = {w: corpus.get_similar_words(w) for w in tqdm(words)}
    with open(p, 'w') as f:
        json.dump(sims, f)


if __name__ == '__main__':
    sources = get_most_popular_songs(40)
    dylan = Corpus(sources, order=2)

    # dylan.save_all_rhymes('/Users/gabriele/Workspace/misc/redylan/src/core/rhymes.json')
    # out = '/Users/gabriele/Workspace/misc/redylan/src/core/dylan_matrices.json'
    # markov_chain.serialize_process(dylan.matrices, out)
    song = [dylan.generate_semantic_sentence(s, 10, 10, 'say')
            for s in ['god', 'save', 'queen', 'love', 'peace', 'war']]
    for i in xrange(10):
        print
        for s in song:
            if s:
                print s[i]
