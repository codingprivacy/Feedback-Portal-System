__author__ = 'Harsh Patel'
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

f=open('responses/default_students_responses.json','r')
data=json.load(f)




def do_nltk(sentence):
    stop_words=set(stopwords.words("english"))  #Set of stop words
    #print(stop_words)
    words=word_tokenize(sentence)
    filtered_lists=[]
    for w in words:
        if(w not in stop_words):
            filtered_lists.append(w)
    return filtered_lists


dict={}
sent_with_points={}
for i in data:
    for j in data[i]:    #for every user response
        #print(j)
        try:
            #print(data[i][j]['negate']['data'])
            #if data[i][j]['negate']['data'] not in dict:
            #temp_list=word_tokenize()
            temp_list=do_nltk(data[i][j]['negate']['data'])
            for item in temp_list:
                if item in dict:
                    dict[item]+=1
                else:
                    dict[item]=1


                #main_list.append(data[i][j]['negate']['data'])
        except: pass
        #if data[i][j]['data'] not in dict:
        temp_list=do_nltk(data[i][j]['data'])
        #temp_list=word_tokenize()
        for item in temp_list:
                if item in dict:
                    #print('here',dict[item])
                    dict[item]+=1
                else:
                    dict[item]=1
            #main_list.append(data[i][j]['data'])

print(len(dict))
print(dict)



for i in data:
    for j in data[i]:    #for every user response
        #print(j)
        try:
            #print(data[i][j]['negate']['data'])
            #if data[i][j]['negate']['data'] not in dict:
            #temp_list=nltk.tokenize.word_tokenize()
            temp_list=do_nltk(data[i][j]['negate']['data'])
            points_add=0
            for k in temp_list:
                points_add=points_add+dict[k]
            sent_with_points[data[i][j]['negate']['data']]=points_add
        except:pass

        #temp_list=nltk.tokenize.word_tokenize()
        temp_list=do_nltk(data[i][j]['data'])
        points_add=0
        for k in temp_list:
            points_add=points_add+dict[k]
        sent_with_points[data[i][j]['data']]=points_add
print(sent_with_points)



max_list=[0,0,0,0,0]    #getting top 5 points
for i in sent_with_points:
    if(sent_with_points[i]>max_list[0]):
        max_list[0]=sent_with_points[i]
        print(sent_with_points[i])
for i in sent_with_points:
    if(sent_with_points[i]>max_list[1] and sent_with_points[i]<max_list[0]):
        max_list[1]=sent_with_points[i]
        print(sent_with_points[i])
for i in sent_with_points:
    if(sent_with_points[i]>max_list[2] and sent_with_points[i]<max_list[1]):
        max_list[2]=sent_with_points[i]
        print(sent_with_points[i])
for i in sent_with_points:
    if(sent_with_points[i]>max_list[3] and sent_with_points[i]<max_list[2]):
        max_list[3]=sent_with_points[i]
        print(sent_with_points[i])
for i in sent_with_points:
    if(sent_with_points[i]>max_list[4] and sent_with_points[i]<max_list[3]):
        max_list[4]=sent_with_points[i]
        print(sent_with_points[i])
print(max_list)


final_list=[]     #sentences of top 5 points
for i in max_list:
    l=[k for k,v in sent_with_points.items() if v == i]
    for value in l:
        if(len(final_list)<5):
            final_list.append(value)
    else: pass
print(final_list)

f=open('corpus_pool/suggestions.json','w')
json.dump(final_list,f)
f.close()


