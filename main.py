# <!-- // Code Author:-
# // Name: Shivam Gupta
# // Net ID:SXG190040
# // Information Retrieval (CS 6322.001) Assignment 1(Tokenization and Stemming) -->

import os
import sys
import glob
from datetime import datetime
from xml.dom import minidom
from collections import Counter
import string
import collections
from porter_stemmer import PorterStemmer

#----------------------Tokenization of Cranfield Documents--------------------------#


# function that loads all the data (Cranfield documents)
def load_doc_data(file):
   doc = minidom.parse(file)
    # Extract only the Text part which is inside the Text tag and removing all the other tags    
   document = doc.getElementsByTagName('TEXT')
   text_data = document[0].firstChild.data
   #print(text_data)
   return text_data    

# function that removes all sort of punctuations
def remove_punct_special_chars(doc_data):
    doc_data= doc_data.replace('\n', ' ')
    punc_trans = str.maketrans(({key: None for key in all_punctuations}))
    filtered_data = doc_data.translate(punc_trans)
    return filtered_data

start_time= datetime.now()
tokenizer=[]
all_punctuations = string.punctuation + '\n'
tokens=[]

# doc_paths ="/people/cs/s/sanda/cs6322/Cranfield/*"
doc_paths=r"Cranfield\*"

doc_pathname = os.path.join(doc_paths)
cranfield_files=glob.glob(doc_pathname)
count_tokens = 0
tokens = []

for i in range(0,len(cranfield_files)):
    text = load_doc_data(cranfield_files[i])
    # remove all the punctuations from the text
    removepunc_spec= remove_punct_special_chars(text)
    tokenizer_our_1 = removepunc_spec.split(" ")
    # remove all the extra spaces from the text
    tokenizer_our = [ai for ai in tokenizer_our_1 if ai != '']
    #print(tokenizer_our)
    # remove all the numbers from the text
    temp = [ i for i in tokenizer_our if not i.isnumeric()]
    tokens.extend(temp)
    count_tokens+=len(tokenizer_our)


# print(tokens)
count_unique_tokens=0
unique_dict=Counter(tokens)
# Calculating 30 most frequent tokens
most_common_tokens = unique_dict.most_common(30)
unique_words=set(tokens)
for i in tokens: 
    if unique_dict[i]==1:
        count_unique_tokens+=1
    
print("#----------------------------------Tokenization of Cranfield Documents-------------------------------- #")
print("The number of tokens in the Cranfield text collection are: \n", len(tokens)) 
print("The number of unique words in the Cranfield text collection are: \n", len(unique_words)) 
print("The number of words that occur only once in the Cranfield text collection are: \n", count_unique_tokens)
print("The 30 most frequent words in the Cranfield text collection and their respective frequency are: \n")
for i in most_common_tokens:
    print(i)
print("The average number of word tokens per document are: \n", len(tokens)/len(cranfield_files))



#-------------------------- Stemming of Cranfield Documents---------------------- #

# Porter stemmer class
porter_stemmer = PorterStemmer()
# Stemming every token
stemmer = [porter_stemmer.stem(token, 0, len(token)-1) for token in tokens]

unique_stem_count=0
stemlist=Counter(stemmer)
for j in stemmer:
    if stemlist[j]==1:
        unique_stem_count +=1

# Calculating 30 most frequent stems
most_frequent_stems =collections.Counter(stemmer).most_common(30)


dic_token_stem= dict()
for i, j in zip(tokens, stemmer):
    dic_token_stem[i]=j
# print(dic_token_stem)

end_time= datetime.now()


print("#---------------------------------- Stemming of Cranfield Documents------------------------------- #")
print('The number of distinct stems in the Cranfield text collection are: \n', len(set(stemmer)))
print('The number of stems that occur only once in the Cranfield text collection are: \n', unique_stem_count)
print('The 30 most frequent stems in the Cranfield text collection and their respective frequency information are: \n')
for i in most_frequent_stems:
    print(i)
print("The average number of word-stems per document are: \n", len(stemmer)/len(cranfield_files))

# Total Time taken
print("The total time taken for tokenization and Stemming: \n", end_time - start_time)
