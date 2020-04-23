__author__ = 'Harsh Patel'
import os
import json
import random
from nltk.sentiment.vader import SentimentIntensityAnalyzer   #sentiment analysis
from textblob import TextBlob
import processing
list_questions=[]
def clear_no_tracker(sid):
    f=open('temp/'+str(sid)+'.json','r')
    file=json.load(f)
    f.close()
    file['number']=[]
    print('clear_no_tracker',file)
    f=open('temp/'+str(sid)+'.json','w')
    json.dump(file,f)
    f.close()

def default_question(sid,saving_id,*args):
    ret_list=initialiser(sid)
    task=ret_list[0]
    response=ret_list[2]
    track_method=ret_list[3]
    no_tracker=ret_list[5]
    working=ret_list[6]
    #print('',len(args))
    if(len(args)==1):
        for arg in args:
            print(arg)

        faculty=args[0][0]
        name=args[0][1]
        print(faculty,name)
    else:
        faculty=ret_list[7]
        name=ret_list[8]
        print(faculty)
        print(name)
    #print(working)

    def phase2():
        #clear_no_tracker(sid)
        if(response=="yes"):
            if(working=="finish"):
                no_tracker_local=[]
                #print('working=finish')
                global list_questions
                list_questions=['q4','q5','q6','q7','q8','q10','q11','q14']
                r_number=random.randint(0,len(list_questions)-1)
                #print('track_method',len(track_method))
                #print('list',len(list))
                #print(list)
                #print('before_function',no_tracker)
                # print('track_method',track_method)
                if(len(track_method)!=len(list_questions)):
                    while(r_number in track_method):
                        r_number=random.randint(0,len(list_questions)-1)
                    #print('r_number',r_number)
                    result=eval('processing.'+str(list_questions[r_number])+"("+str(no_tracker_local)+",'"+faculty+"','"+name+"')")
                    #print('result0',result[0])
                    #print(result[1])
                    #print(result[2])
                    update_initialiser(['sid',sid] , ['task',str(list_questions[r_number])] ,['flag',0], ['methods',int(r_number)],['working',result[0]],['number',result[1]],['faculty',faculty],['name',name])
                    #print('r_number',r_number)
                    #print('result',result)
                    return result[2]
                else:
                    #print('here')
                    result=eval('processing.q3("'+faculty+'","'+name+'")')
                    update_initialiser(['sid',sid],['task','q3'],['flag',0],['working','finish'])
                    saving_feedback(saving_id)
                    return result
            elif(working=="not_finish"):
                #print('before_function',no_tracker)
                result=eval('processing.'+str(task)+"("+str(no_tracker)+",'"+faculty+"','"+name+"')")
                #print('result0',result[0],result[1],result[2])
                update_initialiser(['sid',sid],['working',result[0]],['flag',0],['number',result[1]])
                return result[2]
        if(response=="no"):
             print('response=no enter',response)
             result=eval("processing."+str(task)+"_negate("+str(no_tracker)+",'"+faculty+"','"+name+"')")
             update_initialiser(['sid',sid],['flag',1])
             return result
    if(task=="none"):
        result=processing.q1(faculty,name)   #greetings
        update_initialiser(['sid',sid],['task','q1'],['faculty',faculty],['name',name])
        return result
    elif(task=="q1" and response=="no"):
        #print('here')
        result=processing.q2(faculty,name)
        update_initialiser(['sid',sid],['task','q2'])
        return result
    elif(task=="q1" and response=="yes"):
        #print('harsh')
        return phase2()
    elif(task=="q3" or task=="q2"):
        #print('harsh')

        return 'end'

    else:
        return phase2()

def default_answar(sid,message,saving_id):

    ret_list=initialiser(sid)
    task=ret_list[0]
    flag=ret_list[1]
    working=ret_list[6]
    response=ret_list[2]
    faculty=ret_list[7]
    name=ret_list[8]

    # if(working=="finish" and response=="no"):
    #      response="yes"
    #      update_initialiser(['sid',sid],['response','yes'])
    # else:
    if(flag==1):
        update_initialiser(['sid',sid],['response','yes'])
    elif(flag==0):
        response=emotions(message['data'])
        #print('response',response)
        update_initialiser(['sid',sid],['response',response])
    #if(working=="finish"):
    answars=ret_list[4]
    number_track=ret_list[5]
        #if(flag==1):
        #    takeaction_form(1,task+'_negate',number_track,message,answars)
        #else:

    if(task=='q1' or task=='q2' or task=='q3'): pass
    else: takeaction_form(name,faculty,flag,task,number_track,message,answars,saving_id)
    #remove_temp_answars(task,flag,response,sid)
    #elif(working=="not_finish"):
        #print('not_finish')
     #   update_initialiser(['sid',sid],['answars',message])
    # if(flag==1):
    #     #print('flag1')
    #     answars=ret_list[4]
    #     #number_track=ret_list[5]
    #     #remove_temp_answars(task,flag,response,sid)     #removing temp stored answar list
    #     #takeaction_form(1,task,number_track,message,answars)                 #storing to permanent location
    #     #print('flag1 complete')
    # if(flag==0):
    #     #print('flag0')
    #     update_initialiser(['sid',sid],['message',message],)  #flag=0 means answars to store in temporary location.
    #     #print('flag0 complete')

def initialiser(sid):                                # creates a file and stores initial q,action,flag,before_flag values (first time when client connects)
    if(os.path.isfile('temp/'+str(sid)+'.json')):    # returns true when file is createdd
        #print('file is created already')
        f=open('temp/'+str(sid)+'.json','r')
        file=json.load(f)
        #print(file)
        faculty=file['faculty']
        name=file['name']
        task=file['task']
        flag=file['flag']
        response=file['response']
        track_method=file['methods']
        number_track=file['number']
        working=file['working']
        answars=file['answars']
        ret_list=[task,flag,response,track_method,answars,number_track,working,faculty,name]    #q=questions,action=p or n (+ve or -ve), flag shows semantic of the text (yes or no
        f.close()
        #print('file in if',file)
    else:                                            # if file is not created
        f=open('temp/'+str(sid)+'.json','w')
        file={}
        faculty=file['faculty']=''
        name=file['name']=''
        file['task']='none'
        file['flag']=0
        file['response']='nil'
        file['methods']=[]
        file['answars']=[]
        file['number']=[]
        file['working']='finish'
        task=file['task']
        flag=file['flag']
        response=file['response']
        track_method=file['methods']
        number_track=file['number']
        working=file['working']
        answars=file['answars']
        ret_list=[task,flag,response,track_method,answars,number_track,working,faculty,name]    #q=questions,action=p or n (+ve or -ve), flag shows semantic of the text (yes or no
        json.dump(file,f)
        f.close()
    return ret_list

def update_initialiser(*argv):
    f=open('temp/'+str(argv[0][1])+'.json','r')
    file=json.load(f)
    #print('getting type',type(file['methods']))
    f.close()
    #print(argv)
    for arg in argv[1:]:
        if(arg[0]=="methods" or arg[0]=="answars"):
            file[str(arg[0])].append(arg[1])
            #print('file_temp',file)
            #print('temp file_methods_answars',file)
        elif(arg[0]=="number"):
            #print('update_function',arg[0],arg[1])
            file[(str(arg[0]))]=arg[1]
            #print('temp file_number',file)
        else:
            file[str(arg[0])]=arg[1]
            #print('temp file_else',file)


    f.close()
    f=open('temp/'+str(argv[0][1])+'.json','w')
    json.dump(file,f)
    f.close()




    #print('ret_list',ret_list)


# def update_initialiser(task,flag,response,current_answars,track_methods,number_track,sid):      #updates the values at each loop
#     f=open('temp/'+str(sid)+'.json','rb')
#     file=json.load(f)
#     f.close()
#     print(file)
#     #print('file_before_updated is',file)
#
#     file[sid]={'task':task,'flag':flag,'response':response}
#
#     if(current_answars!='none'):
#         file['answars']=file['answars'].append(current_answars)
#         print(file['answars'])
#
#     print(track_methods)
#     if(track_methods!='none'):
#         file['methods'].append(track_methods)
#     print(file)
#
#     #print('file updated is',file)
#     f=open('temp/'+str(sid)+'.json','wb')
#     json.dump(file,f)
#     f.close()

def remove_temp_answars(task,flag,response,sid):
    f=open('temp/'+str(sid)+'.json','r')
    file=json.load(f)
    f.close()
    file['answars']=[]
    f=open('temp/'+str(sid)+'.json','w')
    json.dump(file,f)
    f.close()

def emotions(text):                           #  finding the emotion of the text
    # testimonial=TextBlob(text)
    # if(testimonial.sentiment.polarity>=0.0):
    #     print(testimonial.sentiment.polarity)
    #     response="yes"
    #     return response
    # elif(testimonial.sentiment.polarity<0.0):
    #     print(testimonial.sentiment.polarity)
    #     response="no"
    #     return response
    # print("text",text)
    # print(text)
    sid = SentimentIntensityAnalyzer()
    mydict=sid.polarity_scores(text)
    print(mydict)
    maximum = max(mydict, key=mydict.get)  # Just use 'min' instead of 'max' for minimum.
    print(maximum, mydict[maximum])
    if(maximum=='neg'):
        response='no'
        return response
    else:
        response='yes'
        return response
    # if(text=="yes" or text=="Yes"):
    #     response="yes"
    #     return response
    # elif(text=="no" or text=="No"):
    #     response="no"
    #     return response

def takeaction_form(name,faculty,flag,task,number_tracker,text,list,saving_id):         # this decides what to do for each question
    form_type='default'
    if(os.path.isfile('backend_final/responses/temp_'+str(saving_id)+'_responses.json') != True):
        #print('created')
        f=open('backend_final/responses/temp_'+str(saving_id)+'_responses.json','w')
        f.write('{}')
        f.close()

    f=open('backend_final/responses/temp_'+str(saving_id)+'_responses.json','r')     # response
    data=json.load(f)
    #text["reason"] = text.pop("data")
    #list.append(text)
    if(len(number_tracker)==0):
        data["greetings"]=text
    elif(flag==1):
        data[str(task)+str(number_tracker[-1])]["negate"]=text
    elif(flag==0):
        data[str(task)+str(number_tracker[-1])]=text
    #print('saved data',data)
    #print(data)
    f.close()
    with open('backend_final/responses/temp_'+str(saving_id)+'_responses.json','w') as f:
        json.dump(data,f)
    f.close()
    # if(flag==0):
    # print('list contains',len(data))
    # global list_questions
    # print(len(list_questions))
    # if(len(data)==len(list_questions)):


def saving_feedback(saving_id):
    f=open('backend_final/responses/temp_'+str(saving_id)+'_responses.json','r')     # response
    data=json.load(f)
    f.close()
    os.remove('backend_final/responses/temp_'+str(saving_id)+'_responses.json')
    form_type='default_students'
    if(os.path.isfile('backend_final/responses/'+str(form_type)+'_responses.json') != True):
        #print('created')
        f=open('backend_final/responses/'+str(form_type)+'_responses.json','w')
        f.write('{}')
        f.close()
    f=open('backend_final/responses/'+str(form_type)+'_responses.json','r')     # response

    main_data=json.load(f)
    f.close()
    f=open('backend_final/responses/'+str(form_type)+'_responses.json','w')     # response
    main_data[saving_id]=data
    json.dump(main_data,f)

