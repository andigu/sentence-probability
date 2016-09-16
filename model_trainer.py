import gensim
from nltk.corpus import stopwords


#  logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def sentence_preprocess(sentence):
    return remove_stop_words(remove_grammar(sentence))


def remove_stop_words(sentence):
    return [word for word in sentence.split(" ") if word not in stopwords.words('english')]


def remove_grammar(sentence):
    return sentence.lower().replace("\n", "").replace(".", "").replace(",", "").replace("?", "").replace("!", ""). \
        replace("'", "").replace('"', "")


documents = open("documents/documents.txt", "r")
training_documents = open("documents/training_text.txt", "r")
processed_documents = [sentence_preprocess(sentence) for sentence in documents]
processed_training = [sentence_preprocess(sentence) for sentence in training_documents]
all_documents = processed_documents + processed_training
training_documents.close()
documents.close()
try:
    model = gensim.models.Word2Vec.load("model/model_1")
except FileNotFoundError:
    model = gensim.models.Word2Vec(all_documents, min_count=1, batch_words=3)
for i in range(500):
    model.train(all_documents)
model.save("model/model_1")
