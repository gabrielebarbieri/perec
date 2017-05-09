import nltk
import os


NLTK_PACKAGES = ['punkt']  # 'cmudict', 'word2vec_sample']
START_SYMBOL = '<s>'
END_SYMBOL = '</s>'


_TOKENIZER = None
_DETOKENIZER = None


def download_nltk_data():
    for package in NLTK_PACKAGES:
        nltk.download(package)


def tokenize(string):
    return [START_SYMBOL] + [w.lower() for w in nltk.word_tokenize(string)] + [END_SYMBOL]


def tokenize_corpus(corpus_folder):
    sentences = []
    for file_name in os.listdir(corpus_folder):
        try:
            with open(os.path.join(corpus_folder, file_name)) as f:
                sentences += [tokenize(line) for line in f if line]
        except IOError:
            pass
    return sentences


# import json
# import os
# import gensim

# corpus = get_corpus('/Users/gabriele/Workspace/misc/perec/perec OLD/corpus/Dylan')
# alphabet = set(w.lower() for sent in corpus for w in sent)
#
# p = '/Users/gabriele/nltk_data/models/word2vec_sample/pruned.word2vec.txt'
# model = gensim.models.KeyedVectors.load_word2vec_format(p)
#
#
# print [w[0] for w in model.most_similar('love') if w[0] in alphabet]
# print [w[0] for w in model.most_similar(positive=['love']) if w[0] in alphabet]
# print [w[0] for w in model.most_similar('god') if w[0] in alphabet]
# print [w[0] for w in model.most_similar(positive=['god', 'money'], negative=['love']) if w[0] in alphabet]
# print [w[0] for w in model.most_similar(positive=['love', 'money'], negative=['god']) if w[0] in alphabet]
# print [w[0] for w in model.most_similar(positive=['love'], negative=['god']) if w[0] in alphabet]



