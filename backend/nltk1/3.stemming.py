__author__ = 'Harsh'
#Stemming removes all the postfix and prefix part thats not needed
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
example="it is very important to be pythonly while you are pythoning with python.all pythoners have pythoned poorly at least once."

words=word_tokenize(example)
print(words)
for w in words:
    print(ps.stem(w))     #print stemmed words of all the words of the sentece