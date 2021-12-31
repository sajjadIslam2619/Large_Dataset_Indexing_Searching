import nltk as tk
from util import file_process, data_clean_up
from util.log_util import logger, spent_time_measure


@logger
@spent_time_measure
def create_bi_word_index():
    file_data_dict = file_process.get_file_data()
    # print('file data dict -> ', file_data_dict)
    clean_data = data_clean_up.get_clean_data('biword index', file_data_dict)
    # print('clean data -> ', clean_data)
    biword_indexed_data_dict = {}
    for file_name in clean_data:
        word_list = clean_data[file_name]
        for index, word in enumerate(word_list):
            if len(word_list) > index + 1:
                biword_key = word_list[index] + ' ' + word_list[index + 1]
                if biword_key in biword_indexed_data_dict:
                    file_list = biword_indexed_data_dict[biword_key]
                    if file_name not in file_list:
                        file_list.append(file_name)
                    biword_indexed_data_dict[biword_key] = file_list
                else:
                    file_list = [file_name]
                    biword_indexed_data_dict[biword_key] = file_list

    return biword_indexed_data_dict


#############################################
# Search query preparation and execution
#############################################

index_dict = create_bi_word_index()
# print(index_dict)

query = 'a duplicate word list'
tokenize_query = tk.word_tokenize(query)
# print(tokenize_query)
stemmer = tk.stem.PorterStemmer()
tokenize_query = [stemmer.stem(word) for word in tokenize_query]
# print(tokenize_query)

result_file_list = []
for index, query_word in enumerate(tokenize_query):
    if len(tokenize_query) > index + 1:
        biword = tokenize_query[index] + ' ' + tokenize_query[index + 1]
        if biword in index_dict:
            if index_dict[biword] not in result_file_list:
                result_file_list.append(index_dict[biword])
        else:
            result_file_list = []
            break

print('Result list ', result_file_list)
