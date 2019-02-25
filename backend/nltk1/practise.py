from __future__ import print_function
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps=PorterStemmer()
example=raw_input()
words=word_tokenize(example)           #tokenizing
stop_words=set(stopwords.words("english"))
for w in words:

    if(w not in stop_words):           #Stopwords removal
        print(ps.stem(w),end=" ")#Stemming

