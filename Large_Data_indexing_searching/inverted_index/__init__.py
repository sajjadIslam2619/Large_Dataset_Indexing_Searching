import nltk as tk
from util import file_process, data_clean_up
from util.log_util import logger, spent_time_measure


@logger
@spent_time_measure
def create_inverted_index():
    file_data_dict = file_process.get_file_data()
    # print('file data dict -> ', file_data_dict)
    clean_data = data_clean_up.get_clean_data('inverted index', file_data_dict)
    # print('clean data -> ', clean_data)

    inverted_indexed_data_dict = {}

    for file_name in clean_data:
        # tokenized_data_list = clean_data[file_name]
        for word in clean_data[file_name]:
            if word in inverted_indexed_data_dict:
                posting_dict = inverted_indexed_data_dict.get(word)
                if file_name in posting_dict:
                    posting_dict[file_name] = posting_dict[file_name] + 1
                    inverted_indexed_data_dict[word] = posting_dict
                else:
                    inverted_indexed_data_dict[word][file_name] = 1
            else:
                posting_dict = {}
                posting_dict[file_name] = 1
                inverted_indexed_data_dict[word] = posting_dict

    return inverted_indexed_data_dict


#############################################
# Search query preparation and execution
#############################################

index_dict = create_inverted_index()
print('Inverted index -> ',index_dict)

# query list
# query 1 : duplicate and word or night and late
# query 2 : duplicate or word and grape
# query 3 : duplicate and grape
# query 4 : duplicate or grape
# query 5 : glass or ugly
# query 6 : tall and sajjad
# query 7 : duplicate and word or night

# operator_list = ['and', 'or', 'not']
operator_list = ['and', 'or']
query = 'duplicate and word or night and late'
# query = 'tall and sajjad'
# query = 'duplicate and sandal and grape'
tokenize_query = tk.word_tokenize(query)
# print(tokenize_query)
stemmer = tk.stem.PorterStemmer()
tokenize_query = [stemmer.stem(word) for word in tokenize_query]
# print(tokenize_query)
list1 = []
list2 = []
operation = ''
runQuery = False

for index, query_word in enumerate(tokenize_query):
    # if query_word == 'not': continue

    if query_word in operator_list:
        # if tokenize_query[index + 1] == 'not':
        # operation = query_word + ' not'
        # else:
        operation = query_word
    else:
        if len(operation) > 0:
            runQuery = True
            if query_word in index_dict:
                list2 = list(index_dict[query_word].keys())
            else:
                list2 = []
        else:
            if query_word in index_dict:
                list1 = list(index_dict[query_word].keys())
            else:
                list1 = []

    if runQuery:
        if operation == 'and':
            list1 = list(set(list1) & set(list2))
        elif operation == 'or':
            list1 = list(set(list1) | set(list2))

        operation = ''
        runQuery = False
        # list1 = []
        list2 = []

print('Result file list -> ', list1)
