# WWW 2021

This is the official repository of the paper:

> **Mining Dual Emotion for Fake News Detection.** [[PDF]](https://www.zhangxueyao.com/assets/www2021-dual-emotion-paper.pdf) [[Code]](https://github.com/RMSnow/WWW2021) [[Slides]](https://www.zhangxueyao.com/assets/www2021-dual-emotion-slides.pdf) [[Video]](https://www.zhangxueyao.com/assets/www2021-dual-emotion-video.mp4) [[中文讲解视频]](https://www.bilibili.com/video/BV13o4y1m7c3)
>
> Xueyao Zhang, Juan Cao, Xirong Li, Qiang Sheng, Lei Zhong, and Kai Shu. Proceedings of 30th The Web Conference (**WWW 2021**)

## An Overall Framework

![1](https://github.com/RMSnow/WWW2021/blob/master/framework.png)

An overall framework of using Dual Emotion Features for fake news detection. Dual Emotion Features consist of three components: 

**a)** Publisher Emotion extracted from the content; 

**b)** Social Emotion extracted from the comments; 

**c)** Emotion Gap representing the similarity and difference between publisher emotion and social emotion.

Dual Emotion Features are concatenated with the features from **d)** Fake News Detector (here, BiGRU as an example) for the final prediction of veracity.

## Datasets

The datasets are available at https://drive.google.com/drive/folders/1pjK0BYiiJt0Ya2nRIrOLCVo-o53sYRBV?usp=sharing.

### RumourEval-19

The raw dataset is released by [SemEval-2019 Task 7](https://competitions.codalab.org/competitions/19938#learn_the_details-overview):

> Genevieve Gorrell, Ahmet Aker, Kalina Bontcheva, Elena Kochkina, Maria Liakata, Arkaitz Zubiaga, Leon Derczynski (2019). SemEval-2019 Task 7: RumourEval, Determining Rumour Veracity and Support for Rumours. Proceedings of the 13th International Workshop on Semantic Evaluation, ACL.

After preprocessing, our experimental dataset is in the folder `dataset/RumourEval-19`.

### Weibo-16

The original dataset is firstly proposed in:

> Jing Ma, Wei Gao, Prasenjit Mitra, Sejeong Kwon, Bernard J Jansen, Kam-Fai Wong, and Meeyoung Cha. 2016. Detecting rumors from microblogs with recurrent neural networks. In IJCAI 2016. 3818–3824.

In *Section 4.1.2* and *Appendix A* of our paper, we described that there are many fake news duplications in the original dataset. The original version of Weibo-16 is in the folder `dataset/Weibo-16-original`, and our experimental dataset (a deduplicated version) of Weibo-16 is in the folder `dataset/Weibo-16`.

### Weibo-20

Weibo-20 is our newly proposed dataset, and it is in the folder `dataset/Weibo-20`. Besides, in *Section 4.4.3* of the paper, we conducted the experiments under the real-world scenario simulation. This temporal version of Weibo-20 is in the folder `dataset/Weibo-20-temporal`.

## Emotion Resources

| Type                    | Language | Resources                                                    |
| ----------------------- | -------- | ------------------------------------------------------------ |
| Emotion Category        | English  | https://github.com/NVIDIA/sentiment-discovery                |
<<<<<<< HEAD
|                         | Chinese  | https://ai.baidu.com/tech/nlp_apply/emotion_detection        |
=======
|                         | Chinese  | https://ai.baidu.com/tech/nlp_apply/emotion_detection              |
>>>>>>> 02998a03e6fbe20ae0614a0532161d035506f287
| Emotion Lexicon         | English  | `resources/English/NRC`                                      |
|                         | Chinese  | `/resources/Chinese/大连理工大学情感词汇本体库`              |
| Emotional Intensity     | English  | `resources/English/NRC`                                      |
|                         | Chinese  | `/resources/Chinese/大连理工大学情感词汇本体库`              |
| Sentiment Score         | English  | [nltk.sentiment.vader.SentimentIntensityAnalyzer](https://www.nltk.org/api/nltk.sentiment.html#nltk.sentiment.vader.SentimentIntensityAnalyzer) |
|                         | Chinese  | `resources/Chinese/BosonNLP`                                 |
| Other Auxilary Features | English  | [Wiki: List of emoticons](https://en.wikipedia.org/wiki/List_of_emoticons), `resources/English/HowNet`, `resources/English/others` |
|                         | Chinese  | `resources/Chinese/HowNet`, `resources/English/others`       |

## Code

### Requirements

```
Python==3.6.10
Keras==2.1.2
Tensorflow==1.13.1
Tensorflow-GPU==1.14.0
```

### Usage

#### Step1: Preprocess

##### Step1.1: Get the `labels`

```
cd code/preprocess
python output_of_labels.py
```

##### Step1.2: Get the `emotion features`

```
cd code/preprocess
python input_of_emotions.py
```

Note that the *Emotion Category* features are depended on the external resources ([NVIDIA-sentiment-discovery](https://github.com/NVIDIA/sentiment-discovery) for English, and [Baidu AI](https://ai.baidu.com/tech/nlp_apply/emotion_detection) for Chinese). And they have been saved in the dataset files (e.g.: `content_emotions`, `comments100_emotions_mean_pooling`, `content_emotions_probs`, `comments100_emotions_labels_max_pooling`, etc.). 

If you want to extract emotion features for your custom datasets, you need to access these external resources and prepare *Emotion Category* features. Of course,  you can also leave *Emotion Category* unused and extract other features by `input_of_emotion.py`.

##### Step1.3: Get the `semantic features`

In this repo, we consider the semantic features as word embeddings. You need to download the preprained word embeddings ([see here](https://github.com/RMSnow/WWW2021/blob/master/word-embedding/readme.md) for more details) before running the following code:

```
cd code/preprocess
python input_of_semantics.py
```

Now, the preprocessed data are stored in `preprocess/data`.

#### Step 2: Configuration

Config the experimental dataset, the model and other hyperparameters in `code/train/config.py`.

#### Step3: Training and Testing

```
cd code/train
python master.py
```

Now, the results are stored in `train/results`.

# Citation

```
@inproceedings{10.1145/3442381.3450004,
    author = {Zhang, Xueyao and Cao, Juan and Li, Xirong and Sheng, Qiang and Zhong, Lei and Shu, Kai},
    title = {Mining Dual Emotion for Fake News Detection},
    year = {2021},
    url = {https://doi.org/10.1145/3442381.3450004},
    doi = {10.1145/3442381.3450004},
    booktitle = {Proceedings of the Web Conference 2021},
    pages = {3465–3476},
    series = {WWW '21}
}
```

