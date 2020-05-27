<!-- // This code Is written by Shivam Gupta(SXG190040) -->
<!-- Information Retrieval (CS 6322.001) Assignment 1(Tokenization and Stemming) -->

## Implementation of Tokenization and Stemming in Cranfield documents Collection

        
        ## Functions:
                - 'load_doc_data()' - function to load all the data (Cranfield documents)
                - 'remove_punct_special_chars()': function to remove all sort of punctuations

     


        ## Variables
                - 'all_punctuations' :The punctuations and the special characters
                - 'tokens' : The tokens which we extract from the documents
                - 'stemmer' :The stems which we extract from the documents
                - 'count_unique_tokens' :The count of the unique(distinct) tokens
                - 'unique_stem_count' :The count of the unique(distinct) stems
                - 'most_common_tokens' :The 30 most frequent tokens
                - 'most_frequent_stems' :The 30 most frequent stems
                - 'dic_token_stem' :The dictionary which contains the tokens and their respective stem words

                

        ## The folder named "Cranfield" contains all the 1400 Cranfiled documents(collection).


## Compiling and Running the Code:

# For Running: Run command:- ```python3 main.py``` on UTD CS Linux Servers / Anaconda Prompt

# Note: If you are using UTD CS Linux server comment line no. 41 and uncomment line no. 40 and If you are using your local machine comment line no. 40 and uncomment line no. 41 in the "main.py" file.


In the ```main.python``` file, We can modify the code by including the <TITLE> tags data as well along with the <TEXT> tags data.
The results will be displayed as follows:

## Results

#----------------------------------Tokenization of Cranfield Documents-------------------------------- #
The number of tokens in the Cranfield text collection are:
 201520
The number of unique words in the Cranfield text collection are:
 8514
The number of words that occur only once in the Cranfield text collection are:
 3551
The 30 most frequent words in the Cranfield text collection and their respective frequency are:

('the', 18682)
('of', 11312)
('and', 5693)
('a', 5283)
('to', 4372)
('in', 4235)
('is', 4107)
('for', 3265)
('are', 2425)
('with', 2082)
('by', 1695)
('at', 1591)
('that', 1565)
('on', 1552)
('flow', 1412)
('be', 1269)
('an', 1258)
('as', 1101)
('this', 1079)
('from', 1067)
('pressure', 1021)
('which', 968)
('number', 905)
('results', 873)
('it', 851)
('mach', 725)
('boundary', 722)
('was', 698)
('theory', 693)
('method', 634)
The average number of word tokens per document are:
 143.94285714285715
#---------------------------------- Stemming of Cranfield Documents------------------------------- #
The number of distinct stems in the Cranfield text collection are:
 5839
The number of stems that occur only once in the Cranfield text collection are:
 2428
The 30 most frequent stems in the Cranfield text collection and their respective frequency information are:
('the', 18682)
('of', 11312)
('and', 5693)
('a', 5283)
('to', 4372)
('in', 4235)
('is', 4107)
('for', 3265)
('ar', 2426)
('with', 2082)
('on', 1818)
('by', 1695)
('flow', 1598)
('at', 1591)
('that', 1565)
('be', 1366)
('an', 1258)
('number', 1236)
('pressur', 1180)
('as', 1101)
('thi', 1079)
('result', 1072)
('from', 1067)
('it', 1029)
('which', 968)
('effect', 839)
('method', 820)
('solut', 785)
('theori', 780)
('boundari', 750)
The average number of word-stems per document are:
 143.94285714285715
The total time taken for tokenization and Stemming:
  0:00:01.529268