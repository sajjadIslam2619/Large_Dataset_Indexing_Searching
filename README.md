# Large_Dataset_Indexing_Searching

1. Inverted Index
2. Bi-word index
3. Positional index

Example: 
- File_1 : A duplicate word list. Duplicate words testing. My late night snacks is grape.
- File_2 : A duplicate word list. Duplicate words testing. Python project in progress.
- File_3 : A duplicate word list testing. Duplicate words exists. Wearing jacket but no sandal. Feeling cold.

Inverted Index 
- Tokenized
- Stemming, punctuation remove
- Stop word remove
- Posting [With word frequency]
- Index : 

{'duplic': {'file_1.txt': 2, 'file_2.txt': 2, 'file_3.txt': 2}, 'word': {'file_1.txt': 2, 'file_2.txt': 2, 'file_3.txt': 2}, 'list': {'file_1.txt': 1, 'file_2.txt': 1, 'file_3.txt': 1}, 'test': {'file_1.txt': 1, 'file_2.txt': 1, 'file_3.txt': 1}, 'late': {'file_1.txt': 1}, 'night': {'file_1.txt': 1}, 'snack': {'file_1.txt': 1}, 'grape': {'file_1.txt': 1}, 'python': {'file_2.txt': 1}, 'project': {'file_2.txt': 1}, 'progress': {'file_2.txt': 1}, 'exist': {'file_3.txt': 1}, 'wear': {'file_3.txt': 1}, 'jacket': {'file_3.txt': 1}, 'sandal': {'file_3.txt': 1}, 'feel': {'file_3.txt': 1}, 'cold': {'file_3.txt': 1}}

Bi-word Index
- Tokenized
- Stemming, punctuation remove
- Index 

{'a duplic': ['file_1.txt', 'file_2.txt', 'file_3.txt'], 'duplic word': ['file_1.txt', 'file_2.txt', 'file_3.txt'], 'word list': ['file_1.txt', 'file_2.txt', 'file_3.txt'], 'list duplic': ['file_1.txt', 'file_2.txt'], 'word test': ['file_1.txt', 'file_2.txt'], 'test my': ['file_1.txt'], 'my late': ['file_1.txt'], 'late night': ['file_1.txt'], 'night snack': ['file_1.txt'], 'snack is': ['file_1.txt'], 'is grape': ['file_1.txt'], 'test python': ['file_2.txt'], 'python project': ['file_2.txt'], 'project in': ['file_2.txt'], 'in progress': ['file_2.txt'], 'list test': ['file_3.txt'], 'test duplic': ['file_3.txt'], 'word exist': ['file_3.txt'], 'exist wear': ['file_3.txt'], 'wear jacket': ['file_3.txt'], 'jacket but': ['file_3.txt'], 'but no': ['file_3.txt'], 'no sandal': ['file_3.txt'], 'sandal feel': ['file_3.txt'], 'feel cold': ['file_3.txt']}

Positional Index
- Tokenized
- Stemming, punctuation remove
- Posting [with word position]
- Index

{'a': {'file_1.txt': [0], 'file_2.txt': [0], 'file_3.txt': [0]}, 'duplic': {'file_1.txt': [1, 4], 'file_2.txt': [1, 4], 'file_3.txt': [1, 5]}, 'word': {'file_1.txt': [2, 5], 'file_2.txt': [2, 5], 'file_3.txt': [2, 6]}, 'list': {'file_1.txt': [3], 'file_2.txt': [3], 'file_3.txt': [3]}, 'test': {'file_1.txt': [6], 'file_2.txt': [6], 'file_3.txt': [4]}, 'my': {'file_1.txt': [7]}, 'late': {'file_1.txt': [8]}, 'night': {'file_1.txt': [9]}, 'snack': {'file_1.txt': [10]}, 'is': {'file_1.txt': [11]}, 'grape': {'file_1.txt': [12]}, 'python': {'file_2.txt': [7]}, 'project': {'file_2.txt': [8]}, 'in': {'file_2.txt': [9]}, 'progress': {'file_2.txt': [10]}, 'exist': {'file_3.txt': [7]}, 'wear': {'file_3.txt': [8]}, 'jacket': {'file_3.txt': [9]}, 'but': {'file_3.txt': [10]}, 'no': {'file_3.txt': [11]}, 'sandal': {'file_3.txt': [12]}, 'feel': {'file_3.txt': [13]}, 'cold': {'file_3.txt': [14]}}
