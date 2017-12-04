import nltk
import gensim
import os
from datetime import datetime


NLTK_PACKAGES = ['punkt', 'word2vec_sample', 'cmudict']
START_SYMBOL = '<s>'
END_SYMBOL = '</s>'

_WORD2VEC = None

BLACKLIST = ['"', '``', "''"]


def download_nltk_data():
    for package in NLTK_PACKAGES:
        nltk.download(package)


def process_word(word, replace_dict=None):
    processed_word = word.lower()
    if replace_dict is not None:
        for k, v in replace_dict.items():
            if k in processed_word:
                processed_word = processed_word.replace(k, v)
    return processed_word


def tokenize(string, replace_dict=None):
    words = [process_word(w, replace_dict) for token in nltk.word_tokenize(string) if token not in BLACKLIST]
    return [START_SYMBOL] + words + [END_SYMBOL]


def tokenize_corpus(sources, replace_dict=None):
    sentences = []
    for file_name in sources:
        try:
            with open(file_name) as f:
                sentences += [tokenize(line, replace_dict) for line in f if line.strip()]
        except IOError:
            pass
    return sentences


def get_semantic_model():
    global _WORD2VEC
    if _WORD2VEC is None:
        t = datetime.now()
        path = os.path.join(nltk.data.find('models/word2vec_sample'), 'pruned.word2vec.txt')
        _WORD2VEC = gensim.models.KeyedVectors.load_word2vec_format(path)
        print 'time to load the semantic model', datetime.now() - t
    return _WORD2VEC


if __name__ == '__main__':

    model = get_semantic_model()
    print [w[0] for w in model.most_similar('love')]
    print [w[0] for w in model.most_similar(positive=['love'])]
    print [w[0] for w in model.most_similar('god')]
    print [w[0] for w in model.most_similar(positive=['god', 'money'], negative=['love'])]
    print [w[0] for w in model.most_similar(positive=['love', 'money'], negative=['god'])]
    print [w[0] for w in model.most_similar(positive=['love'], negative=['god'])]
