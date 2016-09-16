import os
import pickle

from nltk.stem import porter

phrase_count_file = open("documents/phrase_count_memo.txt", "rb+")
maximum_likelihood_file = open("documents/maximum_likelihood_memo.txt", "rb+")
phrase_count_memo = pickle.load(phrase_count_file)
maximum_likelihood_memo = pickle.load(maximum_likelihood_file)


def tokenize(words, pre_stemmed=False):
    if pre_stemmed:
        return words.lower().replace(',', '').replace('.', '').replace('"', '').replace('\'', '').split()
    else:
        stemmer = porter.PorterStemmer()
        tokenized = []
        append = tokenized.append
        for word in words.lower().replace(',', '').replace('.', '').replace('"', '').replace('\'', '').split():
            append(stemmer.stem(word))
        return tokenized


class CorpusReader:
    def __init__(self, dir_name, pre_stemmed=False):
        self.file_names = [dir_name + "/" + file_name for file_name in os.listdir(dir_name)]
        self.pre_stemmed = pre_stemmed

    def count(self, string):
        if string in phrase_count_memo:
            return phrase_count_memo[string]
        else:
            original_string = string
            count = 0
            string = tokenize(string)
            string_len = len(string)
            for file_name in self.file_names:
                file = open(file_name, 'r')
                for line in file:
                    line = tokenize(line, self.pre_stemmed)
                    count += sum([1 if line[i: i + string_len] == string else 0 for i in range(len(line))])
                file.close()
            phrase_count_memo[original_string] = count
            return count

    def close(self):
        # TODO keep track of only the update key value pairs and dump those in as updates to improve speed
        pickle.dump(maximum_likelihood_memo, maximum_likelihood_file)
        pickle.dump(phrase_count_memo, phrase_count_file)

        maximum_likelihood_file.close()
        phrase_count_file.close()
