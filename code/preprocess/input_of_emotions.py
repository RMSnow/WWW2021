import os
import json
from tqdm import tqdm
import time
import numpy as np
import sys
sys.path.append('../emotion')
import extract_emotion_ch
import extract_emotion_en


save_dir = './data'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

datasets_ch = ['Weibo-16', 'Weibo-16-original',
               'Weibo-20', 'Weibo-20-temporal']
datasets_en = ['RumourEval-19']

for dataset in datasets_ch + datasets_en:
    print('\n\n{} [{}]\tProcessing the dataset: {} {}\n'.format(
        '-'*20, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), dataset, '-'*20))

    if dataset in datasets_ch:
        extract_pkg = extract_emotion_ch
    else:
        extract_pkg = extract_emotion_en

    data_dir = os.path.join('../../dataset', dataset)
    output_dir = os.path.join(save_dir, dataset)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    split_datasets = [json.load(open(os.path.join(
        data_dir, '{}.json'.format(t)), 'r')) for t in ['train', 'val', 'test']]
    split_datasets = dict(zip(['train', 'val', 'test'], split_datasets))

    for t, pieces in split_datasets.items():
        arr_is_saved = False
        json_is_saved = False
        for f in os.listdir(output_dir):
            if '.npy' in f and t in f:
                arr_is_saved = True
            if t in f:
                json_is_saved = True

        if arr_is_saved:
            continue

        if json_is_saved:
            pieces = json.load(
                open(os.path.join(output_dir, '{}.json'.format(t)), 'r'))

        # words cutting
        if 'content_words' not in pieces[0].keys():
            print('[{}]\tWords Cutting...'.format(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            for p in tqdm(pieces):
                p['content_words'] = extract_pkg.cut_words_from_text(
                    p['content'])
                p['comments_words'] = [extract_pkg.cut_words_from_text(
                    com) for com in p['comments']]
            with open(os.path.join(output_dir, '{}.json'.format(t)), 'w') as f:
                json.dump(pieces, f, indent=4, ensure_ascii=False)

        emotion_arr = [extract_pkg.extract_dual_emotion(
            p) for p in tqdm(pieces)]
        emotion_arr = np.array(emotion_arr)
        print('{} dataset: got a {} emotion arr'.format(t, emotion_arr.shape))
        np.save(os.path.join(output_dir, '{}_{}.npy'.format(
            t, emotion_arr.shape)), emotion_arr)
