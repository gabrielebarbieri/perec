__author__ = 'Gabriele'

import os


def decode_file(input_file, output_file):
    with open(input_file) as f_in:
        with open(output_file, 'w') as f_out:
            for l in f_in.readlines():
                f_out.write(l.decode('cp1252').encode('utf8'))


def main():
    for root, dirs, files in os.walk('data/Corpus_Poesie/Corpus_fullNames'):
        for f in files:
            input_file = os.path.join(root, f)
            output_file = os.path.join(root + '_decoded', f)
            decode_file(input_file, output_file)

if __name__ == '__main__':
    main()