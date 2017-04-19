import os
import json
from collections import defaultdict, Counter

grammar = defaultdict(list)
pos_dict = defaultdict(list)
rhyme_dict = defaultdict(set)


def parse_tags():
    for file_name in os.listdir('corpus/Tagged_lyrics'):
        with open('corpus/Dylan/' + file_name) as f_in:
            for line in f_in.readlines():
                if line.strip():
                    pattern = []
                    data = json.loads(line)
                    for tag in data['tags']:
                        pos = tag['POS']
                        word = tag['word']
                        pattern.append(pos)
                        # pos_dict[pos][word] += 1
                        pos_dict[pos].append(word)
                    grammar[len(pattern)].append(pattern)


def get_transcription():
    from nltk.corpus import cmudict
    transcriptions = cmudict.dict()
    return transcriptions


if __name__ == '__main__':
    parse_tags()
    # for k, v in pos_dict.items():
    #     print k, v
    from random import choice
    n = 10
    pattern = choice(grammar[n])
    for pos in pattern:
        print pos, choice(pos_dict[pos])