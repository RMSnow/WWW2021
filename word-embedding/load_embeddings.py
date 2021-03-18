import numpy as np


def load_embeddings(language, embeddings_file):
    assert language in ['Chinese', 'English']

    embeddings_index = {}
    with open(embeddings_file, 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        lines = lines if language == 'English' else lines[1:]

        for line in lines:
            word, coefs = line.split(maxsplit=1)
            coefs = np.fromstring(coefs, 'f', sep=' ')
            embeddings_index[word] = coefs

    print('File: {}, there are {} vectors'.format(
        embeddings_file, len(embeddings_index)))
    return embeddings_index
