from math import log2

from corpus_reader import *


def n_gram(sentence, weights=None):
    if weights is None:
        weights = [1 / 3, 1 / 3, 1 / 3]
    sentence = tokenize(sentence)
    probability = 0
    for n in range(1, len(weights) + 1):
        temp_probability = 1
        word_count = len(sentence)
        for i in range(n - 1, word_count):
            word = sentence[i]
            given = sentence[i - n + 1: i]
            temp_probability *= maximum_likelihood(word, given)
        probability += temp_probability * weights[n - 1]
    return probability


def maximum_likelihood(word, given):
    given = " ".join(given)
    if (given + " " + word) not in maximum_likelihood_memo:
        maximum_likelihood_memo[given + " " + word] = reader.count(given + " " + word)
    if given not in maximum_likelihood_memo:
        maximum_likelihood_memo[given] = reader.count(given)

    numerator = maximum_likelihood_memo[given + " " + word]
    denominator = maximum_likelihood_memo[given]
    if denominator == 0:
        return 0
    else:
        return numerator / denominator


def create_stemmed_files(in_dir, out_dir):
    for file_name in os.listdir(in_dir):
        file = open(in_dir + "/" + file_name, 'r')
        new_file = open(out_dir + "/" + file_name, 'w+')
        new_file.write("\n".join([" ".join(tokenize(line)) for line in file]))
        new_file.close()
        file.close()


# Purpose is to rate the model
# Goodman: perplexity figures of 74 for a trigram model, 137 for a bigram model, and 955 for a unigram model.
# Note - this function is quite slow, and should ALSO have more test sentences
def perplexity():
    sentences = ["I saw a man at the store.", "There was a big tree beside him.", "He saw a woman parking her car."]
    total = 0
    word_total = 0
    for sentence in sentences:
        total += log2(n_gram(sentence))
        word_total += len(sentence.split())
    return 2 ** (-total / word_total)

if not os.path.exists("stemmed_corpora"):
    print("Creating stemmed corpora")
    create_stemmed_files("corpora", "stemmed_corpora")
reader = CorpusReader("stemmed_corpora", True)
print(n_gram("The man walked his dog."))
