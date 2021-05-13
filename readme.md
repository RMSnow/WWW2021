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
|                         | Chinese  | https://ai.baidu.com/tech/nlp/emotion_detection              |
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

```
cd code/preprocess
```

Get the `labels`:

```
python output_of_labels.py
```

Get the `emotion features`:

```
python input_of_emotions.py
```

Get the `semantic features`:

```
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
@inproceedings{web2021-fake-news-detection,
    title = {Mining Dual Emotion for Fake News Detection},
    author = {Xueyao Zhang and Juan Cao and Xirong Li and Qiang Sheng and Lei Zhong and Kai Shu},
    booktitle = {The Web Conference 2021 (WWW)},
    year = {2021}
}
```

