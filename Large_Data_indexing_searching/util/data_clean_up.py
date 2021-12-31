import os
from util.log_util import logger, spent_time_measure
import nltk as tk
import re

tk.download('punkt')
tk.download('stopwords')

clean_data_dict = {}


@spent_time_measure
@logger
def get_clean_data(indexing_type, file_data_dict):
    for file_name in file_data_dict:
        file_data = file_data_dict[file_name]
        # remove digits
        pattern = r'[0-9]'
        file_data = re.sub(pattern, '', file_data)

        # remove punctuation and tokenize
        tokenizer = tk.RegexpTokenizer(r'\w+')
        tokenize_words = tokenizer.tokenize(file_data)
        # only tokenize
        # tokenize_words = tk.word_tokenize(file_data)
        # print('word token :: ', tokenize_words)

        # stemming
        stemmer = tk.stem.PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in tokenize_words]
        # print(stemmed_words)

        if indexing_type == 'inverted index':
            # remove stop words
            stop_words = tk.corpus.stopwords.words("english")
            clean_words = [word for word in stemmed_words if not word.lower() in stop_words]
            # print("Clean word list: ", clean_words)
        else:
            clean_words = stemmed_words

        clean_data_dict[file_name] = clean_words

    return clean_data_dict
