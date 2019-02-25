__author__ = 'Harsh'
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps=PorterStemmer()
example=raw_input()
words=word_tokenize(example)           #tokenizing
#stop_words=set(stopwords.words("english"))
#a=[]
#for w in words:
#    if(w not in stop_words):           #Stopwords removal
#        a.append(ps.stem(w))#Stemming

tagged=nltk.pos_tag(words)
print(tagged)
named_entity=nltk.ne_chunk(tagged,binary=False)
l=list(named_entity)
print(l)






