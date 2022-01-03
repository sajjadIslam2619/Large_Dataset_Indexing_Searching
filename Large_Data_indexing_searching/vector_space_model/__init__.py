from util import file_process, data_clean_up
from util.log_util import logger, spent_time_measure
import math
from numpy import dot
from numpy.linalg import norm

file_data_dict = file_process.get_file_data()
# print('file_data_dict -> ', file_data_dict)
clean_data_dict = data_clean_up.get_clean_data('vector_space_model', file_data_dict)
# print('clean_data_dict -> ', clean_data_dict)
unique_word_dict = {}


@logger
@spent_time_measure
def get_unique_word_frequency():
    for file_name in clean_data_dict:
        file_data = clean_data_dict[file_name]
        for word in file_data:
            if word in unique_word_dict:
                freq = unique_word_dict[word]
                freq = freq + 1
                unique_word_dict[word] = freq
            else:
                unique_word_dict[word] = 1


@logger
@spent_time_measure
def calculate_term_frequency():
    term_freq_dict = {}
    for file_name in clean_data_dict:
        file_data = clean_data_dict[file_name]
        word_freq_dict = {}
        for word in file_data:
            if word not in word_freq_dict:
                word_freq_dict[word] = 1
            else:
                freq = word_freq_dict[word]
                freq = freq + 1
                word_freq_dict[word] = freq
        term_freq_dict[file_name] = word_freq_dict

    return term_freq_dict


@logger
@spent_time_measure
def calculate_document_frequency_term():
    document_freq_dict = {}
    for unique_word in unique_word_dict:
        for file_name in clean_data_dict:
            file_data = clean_data_dict[file_name]
            if unique_word in file_data:
                if unique_word in document_freq_dict:
                    doc_freq = document_freq_dict[unique_word]
                    doc_freq = doc_freq + 1
                    document_freq_dict[unique_word] = doc_freq
                else:
                    document_freq_dict[unique_word] = 1

    return document_freq_dict


@logger
@spent_time_measure
def calculate_inverse_document_frequency_term():
    total_no_doc = len(clean_data_dict)
    # print('total_no_doc -> ', total_no_doc)
    inverse_document_frequency_dict = {}
    document_freq_dict = calculate_document_frequency_term()
    # print('document_freq_dict -> ',document_freq_dict)
    for word in document_freq_dict:
        doc_freq = document_freq_dict[word]
        # print('doc_freq -> ', doc_freq)
        inverse_document_frequency_dict[word] = math.log(total_no_doc / doc_freq)

    return inverse_document_frequency_dict


@logger
@spent_time_measure
def calculate_TF_IDF():
    TF_IDF_dict = {}
    term_freq_dict = calculate_term_frequency()
    inverse_document_frequency_dict = calculate_inverse_document_frequency_term()
    # print('inverse_document_frequency_dict -> ',inverse_document_frequency_dict)
    for file_name in term_freq_dict:
        word_freq_dict = term_freq_dict[file_name]
        word_TF_IDF_dict = {}
        for word in unique_word_dict:
            TF_IDF = 0
            if word in word_freq_dict:
                # print('word -> ', word)
                TF = word_freq_dict[word]
                # print('TF -> ',TF)
                IDF = inverse_document_frequency_dict[word]
                # print('IDF -> ',IDF)
                TF_IDF = TF * IDF
            word_TF_IDF_dict[word] = TF_IDF
        TF_IDF_dict[file_name] = word_TF_IDF_dict
    return TF_IDF_dict


@logger
@spent_time_measure
def calculate_similarity_TF_IDF():
    TF_IDF_dict = calculate_TF_IDF()
    file_similarity_dict = {}
    for i, file_name_1 in enumerate(TF_IDF_dict):
        file_tf_idf_dict_1 = TF_IDF_dict[file_name_1]
        file_tf_idf_list_1 = list(file_tf_idf_dict_1.values())
        for j, file_name_2 in enumerate(TF_IDF_dict):
            if j > i:
                file_tf_idf_dict_2 = TF_IDF_dict[file_name_2]
                file_tf_idf_list_2 = list(file_tf_idf_dict_2.values())
                cos_sim = dot(file_tf_idf_list_1, file_tf_idf_list_2) / (
                            norm(file_tf_idf_list_1) * norm(file_tf_idf_list_2))
                file_similarity_dict[file_name_1 + '-' + file_name_2] = cos_sim

    return file_similarity_dict


# Create unique data dictionary
get_unique_word_frequency()

####################################
# Working with unique words
# 1. Total number of unique words
# 2. Top k most frequent words
####################################

total_unique_word = len(unique_word_dict)
print('Total number of unique words :: ', total_unique_word)

no_top_freq_word = 5

sort_unique_word_dict = dict(
    sorted(unique_word_dict.items(), key=lambda item: item[1], reverse=True)[:no_top_freq_word])
print('Top {} most frequent words :: {}'.format(no_top_freq_word, sort_unique_word_dict))
'''
import operator
sort_unique_word_dict = dict(sorted(unique_word_dict.items(), key=operator.itemgetter(1), reverse=True)[:no_top_freq_word])
print('Top {} most frequent words :: {}'.format(no_top_freq_word, sort_unique_word_dict))
'''


####################################
# Working with documents similarity
# Findings k closest documents
####################################
file_similarity_dict = calculate_similarity_TF_IDF()
no_closest_similar_doc = 10
sort_file_similarity_dict = dict(
    sorted(file_similarity_dict.items(), key=lambda item: item[1], reverse=True)[:no_closest_similar_doc])
print('Top {} similar documents :: {}'.format(no_closest_similar_doc, sort_file_similarity_dict))
