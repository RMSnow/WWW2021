import nltk
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import joblib
import pandas as pd
import numpy as np

# ============================== Category ==============================
nvidia_emotions = ['anger', 'anticipation', 'disgust',
                   'fear', 'joy', 'sadness', 'surprise', 'trust']
nvidia_emotions.sort()


def nvidia_arr(emotions_labels_dict=None, emotions_probs_dict=None):
    arr = np.zeros(len(nvidia_emotions)*2)

    if emotions_labels_dict is None or emotions_probs_dict is None:
        return arr

    for i, e in enumerate(nvidia_emotions):
        arr[i] = emotions_labels_dict[e]
        arr[i+len(nvidia_emotions)] = emotions_probs_dict[e]

    return arr

# ============================== Lexicon and Intensity ==============================


# load negation words
negation_words = []
with open('../../resources/English/others/negative/negationWords.txt', 'r') as src:
    lines = src.readlines()
    for line in lines:
        negation_words.append(line.strip())

print('\nThe num of negation words: ', len(negation_words))

# load degree words
how_words_dict = dict()
with open('../../resources/English/HowNet/intensifierWords.txt', 'r') as src:
    lines = src.readlines()
    for line in lines:
        how_word = line.strip().split()
        how_words_dict[' '.join(how_word[:-1])] = float(how_word[-1])

print('The num of degree words: ', len(how_words_dict),
      '. eg: ', list(how_words_dict.items())[0])


# negation value and degree value
def get_not_and_how_value(cut_words, i, windows):
    not_cnt = 0
    how_v = 1

    left = 0 if (i - windows) < 0 else (i - windows)
    window_text = ' '.join(cut_words[left:i])

    for w in negation_words:
        if w in window_text:
            not_cnt += 1
    for w in how_words_dict.keys():
        if w in window_text:
            how_v *= how_words_dict[w]

    return (-1) ** not_cnt, how_v


lexicon_categories, lexicon_terms2arr = joblib.load(
    '../../resources/English/NRC/preprocess/preprocess-lexicon.pkl')
print('[NRC Lexicon]\tThere are {} words, including {} categories, every term\'s dimension is {}'.format(
    len(lexicon_terms2arr), len(lexicon_categories), lexicon_terms2arr['happy'].shape))

intensity_categories, intensity_terms2arr = joblib.load(
    '../../resources/English/NRC/preprocess/preprocess-intensity.pkl')
print('[NRC Intensity]\tThere are {} words, including {} categories, every term\'s dimension is {}'.format(
    len(intensity_terms2arr), len(intensity_categories), intensity_terms2arr['happy'].shape))

nrc_emotion_words = set(lexicon_terms2arr.keys()).union(
    set(intensity_terms2arr.keys()))


def nrc_arr(cut_words, windows=4):
    arr = np.zeros(len(lexicon_categories) + len(intensity_categories))

    for i, word in enumerate(cut_words):
        if word in nrc_emotion_words:
            not_v, how_v = get_not_and_how_value(cut_words, i, windows)

            if word in lexicon_terms2arr:
                arr[:len(lexicon_categories)] += not_v * \
                    how_v * lexicon_terms2arr[word]
            if word in intensity_terms2arr:
                arr[len(lexicon_categories):] += not_v * \
                    how_v * intensity_terms2arr[word]

    return arr

# ============================== Sentiment Scores ==============================


sentiment_analyzer = SentimentIntensityAnalyzer()


def sentiment_score(text):
    scores = sentiment_analyzer.polarity_scores(text)
    return scores['pos'], scores['neg'], scores['neu'], scores['compound']

# ============================== Auxilary Features ==============================


# Emoticon
def isEmoji(content):
    if not content:
        return False
    if u"\U0001F600" <= content and content <= u"\U0001F64F":
        return True
    elif u"\U0001F300" <= content and content <= u"\U0001F5FF":
        return True
    elif u"\U0001F680" <= content and content <= u"\U0001F6FF":
        return True
    elif u"\U0001F1E0" <= content and content <= u"\U0001F1FF":
        return True
    else:
        return False


def emoji_count(text):
    emoji = 0
    for c in text:
        if isEmoji(c):
            emoji += 1
    return emoji / len(text)


smiling_emoticons = [':-)', ':)', ':o)', ':],' ':3',
                     ':c)', ':>' '=]', '8)', '=)', ':}', ':^)', ':っ)']
frowning_emoticons = [
    '>:[', ':-(', ':(', ':-c', ':c', ':-<', ':っC', ':<', ':-[', ':[', ':{']


def emoticon_arr(text):
    smiling = 0
    frowning = 0
    for s in smiling_emoticons:
        smiling += text.count(s)
    for f in frowning_emoticons:
        frowning += text.count(f)
    return smiling / len(text), frowning / len(text), emoji_count(text)


# Punctuation
def symbols_count(text):
    excl = (text.count('!') + text.count('！')) / len(text)
    ques = (text.count('?') + text.count('？')) / len(text)
    comma = (text.count(',') + text.count('，')) / len(text)
    dot = (text.count('.') + text.count('。')) / len(text)
    ellip = (text.count('..') + text.count('。。')) / len(text)

    return excl, ques, comma, dot, ellip


# Sentimental Words
def init_words(file):
    with open(file, 'r', encoding='utf-8') as src:
        words = src.readlines()
        words = [l.strip() for l in words]
    print('File: {}, Words_sz = {}'.format(file.split('/')[-1], len(words)))
    return list(set(words))


print()
pos_words = init_words('../../resources/English/HowNet/正面情感词语（英文）.txt')
pos_words += init_words('../../resources/English/HowNet/正面评价词语（英文）.txt')
neg_words = init_words('../../resources/English/HowNet/负面情感词语（英文）.txt')
neg_words += init_words('../../resources/English/HowNet/负面评价词语（英文）.txt')

pos_words = set(pos_words)
neg_words = set(neg_words)
print('[HowNet]\tThere are {} positive words and {} negative words'.format(
    len(pos_words), len(neg_words)))


def sentiment_words_count(cut_words):
    if len(cut_words) == 0:
        return [0, 0, 0, 0]

    # positive and negative words
    sentiment = []
    for words in [pos_words, neg_words]:
        c = 0
        for word in words:
            if word in cut_words:
                # print(word)
                c += 1
        sentiment.append(c)
    sentiment = [c / len(cut_words) for c in sentiment]

    # degree words
    degree = 0
    for word in how_words_dict:
        if word in cut_words:
            # print(word)
            degree += how_words_dict[word]

    # negation words
    negation = 0
    for word in negation_words:
        negation += cut_words.count(word)
    negation /= len(cut_words)

    sentiment += [degree, negation]

    return sentiment


# Personal Pronoun
first_pronoun = init_words(
    '../../resources/English/others/pronoun/1-personal-pronoun.txt')
second_pronoun = init_words(
    '../../resources/English/others/pronoun/2-personal-pronoun.txt')
third_pronoun = init_words(
    '../../resources/English/others/pronoun/3-personal-pronoun.txt')
pronoun_words = [first_pronoun, second_pronoun, third_pronoun]


def pronoun_count(cut_words):
    if len(cut_words) == 0:
        return [0, 0, 0]

    pronoun = []
    for words in pronoun_words:
        c = 0
        for word in words:
            c += cut_words.count(word)
        pronoun.append(c)

    return [c / len(cut_words) for c in pronoun]

# others


def upper_letter_count(text):
    upper = 0
    for c in text:
        if c.isupper():
            upper += 1
    return upper / len(text)


# Auxilary Features
def auxilary_features(text, cut_words):
    arr = np.zeros(16)

    arr[:3] = emoticon_arr(text)
    arr[3:8] = symbols_count(text)
    arr[8:12] = sentiment_words_count(cut_words)
    arr[12:15] = pronoun_count(cut_words)
    arr[15:16] = upper_letter_count(text)

    return arr


# ============================== Main ==============================


def del_url_at(text):
    pattern = re.compile(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(pattern, text)
    for url in urls:
        text = text.replace(url, '')

    pattern = re.compile(
        '@(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    ats = re.findall(pattern, text)
    for at in ats:
        text = text.replace(at, '')

    text = text.replace('', '').replace('\r', '').replace('\t', '')
    return text


def cut_words_from_text(text):
    pattern = r"""(?x)                   # set flag to allow verbose regexps 
                  (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A. 
                  |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages 
                  |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe 
                  |\.\.\.                # ellipsis 
                  |(?:[.,;"'?():-_`!])    # special characters with meanings 
                """

    return nltk.regexp_tokenize(del_url_at(text), pattern)


def extract_publisher_emotion(content, content_words, emotions_labels_dict, emotions_probs_dict):
    text, cut_words = content, content_words

    arr = np.zeros(54)

    arr[:16] = nvidia_arr(emotions_labels_dict, emotions_probs_dict)
    arr[16:34] = nrc_arr(cut_words)
    arr[34:38] = sentiment_score(text)
    arr[38:54] = auxilary_features(text, cut_words)

    return arr


def extract_social_emotion(comments, comments_words, mean_emotions_labels_dict, max_emotions_labels_dict, mean_emotions_probs_dict, max_emotions_probs_dict):
    if len(comments) == 0:
        arr = np.zeros(54)
        mean_arr, max_arr = arr, arr
        return mean_arr, max_arr, np.concatenate([mean_arr, max_arr])

    arr = np.zeros((len(comments), 54))

    for i in range(len(comments)):
        arr[i] = extract_publisher_emotion(
            comments[i], comments_words[i], None, None)

    mean_arr = np.mean(arr, axis=0)
    max_arr = np.max(arr, axis=0)

    mean_arr[:16] = nvidia_arr(
        mean_emotions_labels_dict, mean_emotions_probs_dict)
    max_arr[:16] = nvidia_arr(
        max_emotions_labels_dict, max_emotions_probs_dict)

    return mean_arr, max_arr, np.concatenate([mean_arr, max_arr])


def extract_dual_emotion(piece, COMMENTS=100):
    for k in ['content_emotions_labels', 'content_emotions_probs', 'comments100_emotions_labels_mean_pooling', 'comments100_emotions_labels_max_pooling', 'comments100_emotions_probs_mean_pooling', 'comments100_emotions_probs_max_pooling']:
        if k not in piece:
            piece[k] = None

    publisher_emotion = extract_publisher_emotion(
        piece['content'], piece['content_words'], piece['content_emotions_labels'], piece['content_emotions_probs'])
    mean_arr, max_arr, social_emotion = extract_social_emotion(
        piece['comments'][:COMMENTS], piece['comments_words'][:COMMENTS], piece['comments100_emotions_labels_mean_pooling'], piece['comments100_emotions_labels_max_pooling'], piece['comments100_emotions_probs_mean_pooling'], piece['comments100_emotions_probs_max_pooling'])
    emotion_gap = np.concatenate(
        [publisher_emotion - mean_arr, publisher_emotion - max_arr])

    dual_emotion = np.concatenate(
        [publisher_emotion, social_emotion, emotion_gap])
    return dual_emotion
