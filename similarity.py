import operator

import gensim
import numpy as np
from nltk.corpus import stopwords


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def sentence_to_vector(sentence, model):
    return sum([model[word] for word in sentence]) / len(sentence)


def sentence_preprocess(sentence):
    return remove_stop_words(remove_grammar(sentence))


def remove_stop_words(sentence):
    return [word for word in sentence.split(" ") if word not in stopwords.words('english')]


def remove_grammar(sentence):
    return sentence.lower().replace("\n", "").replace(".", "").replace(",", "").replace("?", "").replace("!", ""). \
        replace("'", "").replace('"', "")


model = gensim.models.Word2Vec.load("model/model_1")
query = sentence_preprocess("what is the cancellation cost")
document = open("documents/documents.txt", "r")
lines = document.readlines()
print([sentence_preprocess(sentence) for sentence in lines])
document_vectors = [sentence_to_vector(sentence_preprocess(sentence), model) for sentence in lines]
query_vector = sentence_to_vector(query, model)
document_map = {}

for i in range(len(document_vectors)):
    document_map[lines[i].replace("\n", "")] = angle_between(query_vector, document_vectors[i])
sorted_map = sorted(document_map.items(), key=operator.itemgetter(1))

for i in sorted_map:
    print(i)
