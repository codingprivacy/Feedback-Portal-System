from nltk.tokenize import sent_tokenize,word_tokenize
sentence="This is the world that you all were expecting from me mr. Smith. You Should not worry about too way too much."
print(sent_tokenize(sentence))
print(word_tokenize(sentence))
#str=' '.join(i for i in word_tokenize(sentence))    Converting List TO string Again
#print(str)

for i in word_tokenize(sentence):
    print(i)
