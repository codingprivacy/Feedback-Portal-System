__author__ = 'Harsh'
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#stopping words are the words that are not needed for the data analysis like 'and,but,off etc'
#We remove stopping words in this one

sentence="This is an example showing off stop words filtration."
stop_words=set(stopwords.words("english"))  #Set of stop words
#print(stop_words)
words=word_tokenize(sentence)
# filtered_lists=[]
# for w in words:
#     if(w not in stop_words):
#         filtered_lists.append(w)
# print(filtered_lists)

# or the one liner way
#filtered_lists=[w for w in words if w not in stop_words]
#print(filtered_lists)