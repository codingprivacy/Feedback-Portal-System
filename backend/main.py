__author__ = 'Harsh Patel'
import nltk
import re
import time
import os
import json
import random

action='p'
q=1
flag=1
before_flag=1                                 # flag that is used last time

def emotions(text):                           #  finding the emotion of the text
    if(text=="yes" or text=='Yes'):
        flag=1
        #print(flag)
        return flag
    elif(text=="no" or text=="No"):
        flag=0
        #print(flag)
        return flag

def takeaction_form(q,action,text):         # this decides what to do for each question

    f=open('backend/response.json','r')     # response
    data=json.load(f)
    data[str(q)+action]=text
    #print(data)
    f.close()
    with open('backend/response.json','w') as f:
        json.dump(data,f)
    f.close()

def initialiser(sid):                                # creates a file and stores initial q,action,flag,before_flag values (first time when client connects)
    if(os.path.isfile('temp/'+str(sid)+'.json')):    # returns true when file is createdd
        #print('file is created already')
        f=open('temp/'+str(sid)+'.json','r+')
        file=json.load(f)
        #print('file in if',file)
    else:                                            # if file is not created
        f=open('temp/'+str(sid)+'.json','w+')
        file={}
        file[sid]={'q':1,'action':'p','flag':1,'before_flag':1}
        #print('file in else',file)
        json.dump(file,f)
    q=file[sid]['q']
    action=file[sid]['action']
    flag=file[sid]['flag']
    before_flag=file[sid]['before_flag']
    f.close()
    ret_list=[q,action,flag,before_flag]    #q=questions,action=p or n (+ve or -ve), flag shows semantic of the text (yes or no

    #print('ret_list',ret_list)
    return ret_list

def update_initialiser(q,action,flag,before_flag,sid):      #updates the values at each loop
    f=open('temp/'+str(sid)+'.json','w+')
    file={}
    #print('file_before_updated is',file)
    file[sid]={'q':q,'action':action,'flag':flag,'before_flag':before_flag}
    #print('file updated is',file)
    json.dump(file,f)
    f.close()


def get_question(sid,form):                 # called for each time client asks for response to get question.
    ret_list=initialiser(sid)          # function to maintain temp data of session
    q=ret_list[0]
    action=ret_list[1]
    flag=ret_list[2]
    before_flag=ret_list[3]


    with open("backend/"+form+'.json') as file:
        data=json.load(file)
        #print(data[str(q)])
    #try:
    if str(action)+str(q)  in data.keys():
        print("status",str(action)+str(q))
        print(data[str(action)+str(q)])

        print(random.randint( 1,len(data[str(action)+str(q)]) ))
        print(data[str(action)+str(q)][str( random.randint( 1,len(data[str(action)+str(q)]) ) )])
        return data[str(action)+str(q)][str( random.randint( 1,len(data[str(action)+str(q)]) ) )]
    else:
        print('here')
        return "end"

    # except:
    #     os.remove("temp/"+str(sid)+".json")
    #     return "end"

def save_answar(sid,answar,form):
        ret_list=initialiser(sid)       # function to maintain temp data of session
        q=ret_list[0]
        action=ret_list[1]
        flag=ret_list[2]
        before_flag=ret_list[3]

        output=answar["data"]               # take answar
        #print('output',output)
        before_flag=flag
        takeaction_form(q,action,output)    # what function needs to be run if this is the case  (q is the same question for which answar need to be recorded)
        flag=emotions(output)               # function to detect a response, flag=1 if positive
        #print("before_flag=",before_flag)
        #print("flag",flag)


        if(form=="form1"):                     # rules for form1
            if(q==1 and action=='n'):
                time.sleep(0.1)
                exit()
            if(action=='p' and q==2 and flag==0):
                action='n'
            elif(action=='p' and q==1 and flag==0):
                action='n'
            else:
                action='p'
                q+=1
        update_initialiser(q,action,flag,before_flag,sid)
