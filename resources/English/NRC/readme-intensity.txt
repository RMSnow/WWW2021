
THE NRC EMOTION INTENSITY LEXICON (NRC-EIL) aka THE NRC AFFECT INTENSITY LEXICON (NRC-AIL)
------------------------------------------------------------------------------------------

Version: 1
Released: March 2020
www.saifmohammad.com/WebPages/AffectIntensity.htm


CONTACT 
-------


Technical enquiries

Saif M. Mohammad (Senior Research Officer at NRC and creator of these lexicons)
Saif.Mohammad@nrc-cnrc.gc.ca 

Business enquiries

Pierre Charron (Client Relationship Leader at NRC)
Pierre.Charron@nrc-cnrc.gc.ca



Information on various lexicons is available here:
http://saifmohammad.com/WebPages/lexicons.html

You may also be interested in some of the other resources and work we have done on the analysis of emotions in text:
http://saifmohammad.com/WebPages/ResearchAreas.html
http://saifmohammad.com/WebPages/ResearchInterests.html#EmotionAnalysis



TERMS OF USE 
------------

1. The lexicons mentioned in this page can be used freely for non-commercial research and educational purposes.

2. Cite the papers associated with the lexicons in your research papers and articles that make use of them. (The papers associated with each lexicon are listed below, and also in the READMEs for individual lexicons.) 

3. In news articles and online posts on work using these lexicons, cite the appropriate lexicons. For example:
"This application/product/tool makes use of the <resource name>, created by <author(s)> at the National Research Council Canada." (The creators of each lexicon are listed below. Also, if you send us an email, we will be thrilled to know about how you have used the lexicon.) If possible hyperlink to this page: http://saifmohammad.com/WebPages/lexicons.html

4. If you use a lexicon in a product or application, then acknowledge this in the 'About' page and other relevant documentation of the application by stating the name of the resource, the authors, and NRC. For example:
"This application/product/tool makes use of the <resource name>, created by <author(s)> at the National Research Council Canada." (The creators of each lexicon are listed below. Also, if you send us an email, we will be thrilled to know about how you have used the lexicon.) If possible hyperlink to this page: http://saifmohammad.com/WebPages/lexicons.html

5. Do not redistribute the data. Direct interested parties to this page: http://saifmohammad.com/WebPages/AccessResource.htm

6. If interested in commercial use of any of these lexicons, see information here: https://shop-magasin.nrc-cnrc.gc.ca/nrcb2c/app/displayApp/(cpgnum=1&layout=7.01-7_1_71_63_73_6_9_3&uiarea=3&carea=0000000104&cpgsize=0)/.do?rf=y.

7. National Research Council Canada (NRC) disclaims any responsibility for the use of the lexicons listed here and does not provide technical support. However, the contact listed above will be happy to respond to queries and clarifications.


GENERAL DESCRIPTION
-------------------

The NRC Emotion Intensity Lexicon (version 1) is a list of English words with real-valued
scores of intensity for eight basic emotions (anger, anticipation, disgust, fear, joy,
sadness, surprise, and trust). (Note that an earlier version of the lexicon (v0.5)
included intensity scores for four basic emotions: anger, fear, sadness, joy.)

Words can be associated with different intensities (or degrees) of an emotion.  For
example, most people will agree that the word condemn is associated with a greater degree
of anger (or more anger) than the word irritate. However, annotating instances for
fine-grained degrees of affect is a substantially more difficult undertaking than
categorical annotation: respondents are presented with greater cognitive load and it is
particularly hard to ensure consistency (both across responses by different annotators and
within the responses produced by the same annotator). Here, for the first time, we create
an affect intensity lexicon with real-valued scores of association using best--worst
scaling.

For a given word and emotion X, the scores range from 0 to 1. A score of 1 means that the
word conveys the highest amount of emotion X.  A score of 0 means that the word conveys
the lowest amount of emotion X.

The lexicon has close to 10,000 entries for eight emotions that Robert Plutchik argued to
be basic or universal.  It includes common English terms as well as terms that are more
prominent in social media platforms, such as Twitter. It includes terms that are
associated with emotions to various degrees. For a given emotion, this even includes some
terms that may not predominantly convey that emotion (or that convey an antonymous
emotion), and yet tend to co-occur with terms that do.  (Antonymous terms tend to co-occur
with each other more often than chance, and are particularly problematic when one uses
automatic co-occurrence-based statistical methods to capture word--emotion connotations.)

This study was approved by the NRC Research Ethics Board (NRC-REB) under protocol number
2017-98. REB review seeks to ensure that research projects involving humans as
participants meet Canadian standards of ethics.


PAPER
-----

Details of the lexicon are in this paper.
Word Affect Intensities. Saif M. Mohammad. In Proceedings of the 11th Edition of the
Language Resources and Evaluation Conference (LREC-2018), May 2018, Miyazaki, Japan.

Please cite the paper if you use it or when referring to the lexicon. A copy of the paper
is included in this package (Paper_NRC_Emotion_Intensity_Lexicon.pdf).


NRC-EIL IN VARIOUS LANGUAGES
----------------------------

Despite some cultural differences, it has been shown that a majority of affective norms
are stable across languages. Thus we provide versions of the emotion intensity lexicon in
over one hundred languages by translating the English terms using Google Translate (July
2018).


THE RELATIONSHIP OF NRC-EIL WITH THE NRC EMOTION LEXICON 
--------------------------------------------------------

The NRC Emotion Lexicon provides binary scores (0 or 1) indicating whether a word is
associated with a basic emotion or not. The NRC-EIL includes all the words that are marked
as associated with an emotion in the NRC Emotion Lexicon. Notably, NRC-EIL provides for
these words a score indicative of the intensity of emotion. Note that the NRC-EIL also
includes some words that do not occur in the NRC Emotion Lexicon.


APPLICATIONS
------------

The NRC EIL Lexicon has a broad range of applications in Computational Linguistics, Psychology,
Digital Humanities, Computational Social Sciences, and beyond. Notably it can be used to:
- study how people use words to convey emotions.
- study how different genders and personality traits impact how we view the world around us.
- study how emotions are conveyed through literature, stories, and characters.
- obtain features for machine learning systems in sentiment, emotion, and other affect-related tasks and 
  to create emotion-aware word embeddings and emotion-aware sentence representations.
- evaluate automatic methods of determining emotion intensity.
- study the interplay between the basic emotion model and the VAD model of emotions.
- study the role of high emotion intensity words in high emotion intensity sentences, tweets, snippets from literature.


FILES AND FORMAT
----------------

1. NRC-Emotion-Intensity-Lexicon-v1.txt: This is the main lexicon file with entries for ~10K English words. 
It has three columns (separated by tabs):
- word: The English word for which emotion intensity scores is provided. 
(For each emotion, the words are listed in decreasing order of intensity.)
- emotion: The emotion for which the intensity score is provided.
- emotion-intensity-score: The emotion intensity score of the word.

2. The directory 'OneFilePerEmotion' has the same information as in
NRC-Emotion-Intensity-Lexicon-v1.txt, but in multiple files -- one for each emotion: for
e.g., anger-scores.txt includes anger intensity scores.  The words are listed in
decreasing order of intensity.

3. NRC-Emotion-Intensity-Lexicon-v1-ForVariousLanguages.txt: This files has the same first
three columns as the NRC-Emotion-Intensity-Lexicon-v1.txt.  Additionally, it has columns
pertaining to over 100 languages. Each of these columns lists the translations of the
English words into the corresponding language. For example, the column Japanese-ja
contains the Japanese translations of the English words. ('ja' is the ISO-639-1 Code for
Japanese.) The translations were obtained using Google Translate in July 2018.
Occasionally, Google Translate fails to provide a translation. In such cases, the file
shows "NO TRANSLATION" instead of the translation.

4. The directory 'OneFilePerLanguage' has the same information as in
NRC-Emotion-Intensity-Lexicon-v1-ForVariousLanguages.txt, but in multiple files -- one for each
language.  Each of these files has four columns. The first column is for the English words. The
second column is the translation of the English words to a different language -- the language
corresponding to the file name. The third column is the emotion for which the intensity score is
provided.  The fourth column is the  emotion intensity score of the word.  So if one is interested
only in the Japanese version of the NRC-EIL, then they can simply use
Japanese-ja-NRC-Emotion-Intensity-Lexicon-v1.txt.

5. Paper_NRC_Emotion_Intensity_Lexicon.pdf: The research paper describing the NRC-EIL.

You can view the lexicon files using most text editors, Microsoft Excel, etc. You might
have to make sure that the viewer supports characters from various languages, i.e., set
the encoding option in the viewer to UTF-8, etc.  For example, to view in excel, follow
these steps:
- open excel
- click on File -> Import
- select file type as 'Text file' 
- select the lexicon file to import in the dialog box that opens up
- select 'File Origin' type as 'Unicode (UTF-8)'
- click 'Finish'


YOU MAY ALSO BE INTERESTED IN 
-----------------------------

- The NRC Valence, Arousal, and Dominance (VAD) Lexicon includes a list of more than 20,000 English words and
their valence, arousal, and dominance scores.  For a given word and a dimension (V/A/D), the scores range from
0 (lowest V/A/D) to 1 (highest V/A/D).  

	Obtaining Reliable Human Ratings of Valence, Arousal, and Dominance for 20,000 English Words.  Saif M.
	Mohammad. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics,
	Melbourne, Australia, July 2018.

http://saifmohammad.com/WebPages/nrc-vad.html

- The NRC Emotion Lexicon is a list of English words and their associations with eight basic emotions
(anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) and two sentiments (negative
and positive). The annotations were manually done by crowdsourcing.

	Crowdsourcing a Word-Emotion Association Lexicon, Saif Mohammad and Peter Turney, Computational
	Intelligence, 29 (3), 436-465, 2013.

http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm


FUTURE WORK
-----------

- Create an interactive visualizer to explore the NRC-EIL. 


FEEDBACK
-------- 
We will be happy to hear from you, especially if:
- you give us feedback regarding these lexicons.
- you tell us how you have (or plan to) use the lexicons.
- you are interested in having us analyze your data for sentiment, emotion, and other affectual information.
- you are interested in a collaborative research project. 

Email Saif M. Mohammad: saif.mohammad@nrc-cnrc.gc.ca

