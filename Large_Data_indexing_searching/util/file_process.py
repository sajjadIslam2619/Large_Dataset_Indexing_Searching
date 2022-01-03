import os
from util.log_util import logger, spent_time_measure
import nltk as tk
import re

tk.download('punkt')
tk.download('stopwords')

# cleanDataDict = {}
file_data_dict = {}


# Read text File and clean up data.
@logger
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        file_name = file.name
        file_name = file_name.split('/')[-1]

        # print('File name : {}'.format(file_name))
        file_data = file.read()
        file_data_dict[file_name] = file_data


@logger
def read_directory():
    # Folder Path
    current_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(current_path, '..', 'Large_Dataset_test')

    # path = os.path.join(os.getcwd(), 'Large_Dataset_test')
    # Change the directory
    os.chdir(path)

    # iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
            # call read text file function
            read_text_file(file_path)


'''
@logger
def read_from_directory():
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(current_path, "../Large_Dataset")
    # child dir
    os.chdir(file_dir)
    # iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{file_dir}/{file}"
            # call read text file function
            read_text_file(file_path)

'''
'''
@spent_time_measure
@logger
def get_clean_data():
    read_directory()
    return cleanDataDict
'''


def get_file_data():
    read_directory()
    # print(file_data_dict)
    return file_data_dict
