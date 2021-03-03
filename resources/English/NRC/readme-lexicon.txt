NRC Word-Emotion Association Lexicon (NRC Emotion Lexicon)
Version 0.92
10 July 2011
Copyright (C) 2011 National Research Council Canada (NRC)
************************************************************


************************************************************
Contact: 
************************************************************


Technical enquiries

Saif M. Mohammad (Senior Research Officer at NRC and creator of these lexicons)Saif.Mohammad@nrc-cnrc.gc.ca 

Business enquiries

Pierre Charron (Client Relationship Leader at NRC)
Pierre.Charron@nrc-cnrc.gc.ca



Information on various lexicons is available here:
http://saifmohammad.com/WebPages/lexicons.html

You may also be interested in some of the other resources and work we have done on the analysis of emotions in text:
http://saifmohammad.com/WebPages/ResearchAreas.html
http://saifmohammad.com/WebPages/ResearchInterests.html#EmotionAnalysis



************************************************************
Terms of Use: 
************************************************************

1. The lexicons mentioned in this page can be used freely for non-commercial research and educational purposes.

2. Cite the papers associated with the lexicons in your research papers and articles that make use of them. (The papers associated with each lexicon are listed below, and also in the READMEs for individual lexicons.) 

3. In news articles and online posts on work using these lexicons, cite the appropriate lexicons. For example:
"This application/product/tool makes use of the <resource name>, created by <author(s)> at the National Research Council Canada." (The creators of each lexicon are listed below. Also, if you send us an email, we will be thrilled to know about how you have used the lexicon.) If possible hyperlink to this page: http://saifmohammad.com/WebPages/lexicons.html

4. If you use a lexicon in a product or application, then acknowledge this in the 'About' page and other relevant documentation of the application by stating the name of the resource, the authors, and NRC. For example:
"This application/product/tool makes use of the <resource name>, created by <author(s)> at the National Research Council Canada." (The creators of each lexicon are listed below. Also, if you send us an email, we will be thrilled to know about how you have used the lexicon.) If possible hyperlink to this page: http://saifmohammad.com/WebPages/lexicons.html

5. Do not redistribute the data. Direct interested parties to this page: http://saifmohammad.com/WebPages/AccessResource.htm

6. If interested in commercial use of any of these lexicons, see information here: https://shop-magasin.nrc-cnrc.gc.ca/nrcb2c/app/displayApp/(cpgnum=1&layout=7.01-7_1_71_63_73_6_9_3&uiarea=3&carea=0000000104&cpgsize=0)/.do?rf=y.

7. National Research Council Canada (NRC) disclaims any responsibility for the use of the lexicons listed here and does not provide technical support. However, the contact listed above will be happy to respond to queries and clarifications.



We will be happy to hear from you, especially if:
- you give us feedback regarding these lexicons;
- you tell us how you have (or plan to) use the lexicons;
- you are interested in having us analyze your data for sentiment, emotion, and other affectual information;
- you are interested in a collaborative research project. We also regularly hire graduate students for research internships.





Creators: Saif M. Mohammad and Peter D. Turney

Papers associated with this lexicon:

Saif Mohammad and Peter Turney. Crowdsourcing a Word-Emotion Association Lexicon. Computational Intelligence, 29(3): 436-465, 2013. Wiley Blackwell Publishing Ltd.
 	 
Saif Mohammad and Peter Turney. Emotions Evoked by Common Words and Phrases: Using Mechanical Turk to Create an Emotion Lexicon. In Proceedings of the NAACL-HLT 2010 Workshop on Computational Approaches to Analysis and Generation of Emotion in Text, June 2010, LA, California.





************************************************************
GENERAL DESCRIPTION
************************************************************

The NRC Emotion Lexicon is a list of words and their associations with eight emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) and two sentiments (negative and positive). The annotations were manually done through Amazon's Mechanical Turk. 



************************************************************
FORMS OF THE LEXICON
************************************************************

1. Annotations at word-sense level (file: NRC-Emotion-Lexicon-Senselevel-v0.92.txt)

The original lexicon has annotations at word-sense level. Each word-sense pair was annotated by at least three annotators (most are annotated by at least five). 

2. Annotations at word level (file: NRC-Emotion-Lexicon-Wordlevel-v0.92.txt)

The word-level lexicon was created by taking the union of emotions associated with all the senses of a word. 

3. Translation into 105 languages (file: NRC-Emotion-Lexicon-v0.92-In105Languages-Nov2017Translations.xlsx)

The NRC Emotion Lexicon has affect annotations for English words. Despite some cultural differences, it has been shown that a majority of affective norms are stable across languages. Thus, we provide versions of the lexicon in 105 languages by translating the English terms using Google Translate (November 2017).  

Note that some translations by Google Translate may be incorrect or they may simply be transliterations of the original English terms. 



************************************************************
FILE FORMAT 
************************************************************

Annotations at WORD-SENSE LEVEL (file: NRC-Emotion-Lexicon-Senselevel-v0.92.txt)

Each line has the following format:
<term>--<NearSynonyms><tab><AffectCategory><tab><AssociationFlag>

<term> is a word for which emotion associations are provided;

<NearSynonyms> is a set of one to three comma-separated words that indicate the sense of the <term>. The affect annotations are for this sense of the term.

<AffectCategory> is one of eight emotions (anger, fear, anticipation, trust, surprise, sadness, joy, or disgust) or one of two polarities (negative or positive);

<AssociationFlag> has one of two possible values: 0 or 1. 0 indicates that the target word has no association with affect category, whereas 1 indicates an association.



Annotations at WORD LEVEL (file: NRC-Emotion-Lexicon-Wordlevel-v0.92.txt)

Each line has the following format:
<term><tab><AffectCategory><tab><AssociationFlag>

<term> is a word for which emotion associations are provided;

<AffectCategory> is one of eight emotions (anger, fear, anticipation, trust, surprise, sadness, joy, or disgust) or one of two polarities (negative or positive);

<AssociationFlag> has one of two possible values: 0 or 1. 0 indicates that the target word has no association with affect category, whereas 1 indicates an association.



************************************************************
VERSION INFORMATION
************************************************************

Version 0.92 is the latest version as of 10 July 2011. This version has annotations for more than twice as many terms as in Version 0.5.



************************************************************
More Information
************************************************************

Details on the process of creating the lexicon can be found in the associated papers (see above).

 
