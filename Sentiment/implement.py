__author__ = 'Harsh Patel'

import pickle
from sklearn.feature_extraction.text import CountVectorizer

file=open("reviews_train_clean","rb")
reviews_train_clean=pickle.load(file)
file.close()
print('start')
cv = CountVectorizer(binary=True)
cv.fit(reviews_train_clean)
print('fit')

list=["He does complete the course in time, but not in the pace we expect them to. Usually, the last chapters are not comprehensible at all.","I find him to have a very little knowledge on the subject he is teaching.","He responds to the questions well, yet he does not always provide the correct explanations/answers to the doubts.","There has always been a situation of chaos in the classroom. He can not manage the classroom at all.","He needs to work on that.","There is chaos all around. Students busy in their on work and life.","No, nothing that I can recall. I believe he should guide the students a bit more.Well, he tries to conduct tests, not regular though. Students don't show up and that doesn't seem to bother him much.,"He is fair while evaluating. I don't sense any partiality.
print(len(list))
list=cv.transform(list)

filename="finalized_model.sav"
final_model = pickle.load(open(filename, 'rb'))
print(final_model.predict(list))
