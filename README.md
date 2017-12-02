Sentence Probability
====================

This project holds the basic tools to calculate the probability of a sentence occuring in the English language, using
a trigram Hidden Markov Model. Pickled files were used in order to avoid redoing word counts, and a model is saved
in the model folder. The corpora being used in the main program (sentence_probability.py) are the stemmed_corpora,
which are derived from the texts in the corpora folder (they have just been automatically reformatted to make analysis
easier for the program).

Dependencies:
-------------
Python packages required include:
* gensim
* nltk
* numpy
Once you have installed nltk, you must run:
```
import nltk
nltk.download()
```
In the pop up, find "stopwords", and download that.
