import os
import json
from tqdm import tqdm
import time
import numpy as np
from keras.utils import to_categorical


save_dir = './data'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

datasets_ch = ['Weibo-16', 'Weibo-16-original',
               'Weibo-20', 'Weibo-20-temporal']
datasets_en = ['RumourEval-19']

label2idx = {'fake': 0, 'real': 1, 'unverified': 2}


def get_labels_arr(pieces):
    labels = np.array([label2idx[p['label']] for p in pieces])
    return to_categorical(labels)


for dataset in datasets_ch + datasets_en:
    print('\n\n{} [{}]\tProcessing the dataset: {} {}\n'.format(
        '-'*20, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), dataset, '-'*20))

    data_dir = os.path.join('../../dataset', dataset)
    output_dir = os.path.join(save_dir, dataset)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    split_datasets = [json.load(open(os.path.join(
        data_dir, '{}.json'.format(t)), 'r')) for t in ['train', 'val', 'test']]
    split_datasets = dict(zip(['train', 'val', 'test'], split_datasets))

    for t, pieces in split_datasets.items():
        arr_is_saved = False
        for f in os.listdir(output_dir):
            if '.npy' in f and t in f and 'label' in f:
                arr_is_saved = True

        if arr_is_saved:
            continue

        labels_arr = get_labels_arr(pieces)
        print('{} dataset: got a {} label arr'.format(t, labels_arr.shape))
        np.save(os.path.join(output_dir, '{}_label_{}.npy'.format(
            t, labels_arr.shape)), labels_arr)
