import nltk as tk
from util import file_process, data_clean_up
from util.log_util import logger, spent_time_measure
import sys

all_file_list = []
# clean_data_dict = {}


@logger
@spent_time_measure
def create_positional_index():
    file_data_dict = file_process.get_file_data()
    # print('file data dict -> ', file_data_dict)
    global clean_data_dict
    clean_data_dict = data_clean_up.get_clean_data('positional index', file_data_dict)
    # print('clean data -> ', clean_data_dict)

    positional_indexed_data_dict = {}

    for file_name in clean_data_dict:
        # tokenized_data_list = clean_data[file_name]
        clean_data_list = clean_data_dict[file_name]
        all_file_list.append(file_name)

        for index, word in enumerate(clean_data_list):
            if word in positional_indexed_data_dict:
                posting_dict = positional_indexed_data_dict.get(word)
                if file_name in posting_dict:
                    posting_dict[file_name].append(index)
                    positional_indexed_data_dict[word] = posting_dict
                else:
                    word_index_list = []
                    word_index_list.append(index)
                    posting_dict[file_name] = word_index_list
                    positional_indexed_data_dict[word] = posting_dict
            else:
                posting_dict = {}
                word_index_list = []
                word_index_list.append(index)
                posting_dict[file_name] = word_index_list
                positional_indexed_data_dict[word] = posting_dict

    return positional_indexed_data_dict


#############################################
# Search query preparation and execution
#############################################
index_dict = create_positional_index()
print('positional index -> ', index_dict)
# print('Clean data dict -> ', clean_data_dict)

query = 'a duplicate word list testing'
query = 'Ugly face'
query = 'Duplicate words'
query = 'late night grape'

tokenize_query = tk.word_tokenize(query)
# print(tokenize_query)
stemmer = tk.stem.PorterStemmer()
tokenize_query = [stemmer.stem(word) for word in tokenize_query]

# print('All file list -> ',all_file_list)
query_file_list = all_file_list
result_file_list = []
for index, query_word in enumerate(tokenize_query):
    if query_word in index_dict:
        temp_file_list = list(index_dict[query_word].keys())
        query_file_list = list(set(query_file_list) & set(temp_file_list))
    else:
        query_file_list = []
        break

if len(query_file_list) == 0:
    print('Query does not match.')
    sys.exit()

# print('Query File list -> ', query_file_list)
# print('Clean data dict -> ', clean_data_dict)

for query_word in tokenize_query:
    file_word_position_dict = index_dict[query_word]
    for file_name in file_word_position_dict:
        if file_name in query_file_list:
            position_index_list = file_word_position_dict[file_name]
            for index in position_index_list:
                file_data = clean_data_dict[file_name]
                queryExist = True
                consecutiveIndex = index
                for word in tokenize_query:
                    if file_data[consecutiveIndex] == word:
                        consecutiveIndex = consecutiveIndex + 1
                    else:
                        queryExist = False
                        break
                if queryExist:
                    result_file_list.append(file_name)
        else:
            continue

print('Result file list -> ', set(result_file_list))
