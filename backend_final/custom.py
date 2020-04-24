__author__ = 'Harsh Patel'
import json
import random
import os
def greeting(sid,*args):
    faculty=args[0][0]
    user=args[0][1]
    initialisers(sid)
    update_initialiser(['sid',sid],['faculty',faculty],['name',user])
    file=open('backend_final/Data/custom_greetings.json','r')
    j_file=json.load(file)
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        #print(str(j_file[r_number]))
        return str(j_file[r_number])

def custom_question(sid,form_type,saving_id):
    list=initialisers(sid)
    track_number=list[0]
    print(track_number)
    f=open('backend_final/custom_forms/'+form_type+'.json','rb')
    data=json.load(f)
    update_initialiser(['sid',sid],['track_number',track_number+1])
    try:
        return data['q'+str(track_number+1)]
    except:
        saving_feedback(saving_id,form_type)
        return 'end'

def custom_answar(sid,form_type,message,saving_id):
    list=initialisers(sid)
    track_number=list[0]
    name=list[3]
    faculty=list[2]
    save_answar(sid,track_number,message,name,faculty,form_type,saving_id)

def save_answar(sid,track_number,message,name,faculty,form_type,saving_id):
    print(os.getcwd())
    if(os.path.isfile('backend_final/responses/temp_'+str(saving_id)+'_responses.json') != True):
        print('created')
        f=open('backend_final/responses/temp_'+str(saving_id)+'_responses.json','w')
        f.write('{}')
        f.close()

    f=open('backend_final/responses/temp_'+str(saving_id)+'_responses.json','r')     # response
    data=json.load(f)
    #text["reason"] = text.pop("data")
    #list.append(text)
    if(track_number==0):
        data["greetings"]=message
    else:
        data[track_number]=message
    #print('saved data',data)
    #print(data)
    f.close()
    with open('backend_final/responses/temp_'+str(saving_id)+'_responses.json','w') as f:
        json.dump(data,f)
    f.close()

def initialisers(sid):
    if(os.path.isfile('temp/'+str(sid)+'.json')):    # returns true when file is createdd
        #print('file is created already')
        f=open('temp/'+str(sid)+'.json','r')
        file=json.load(f)
        #print(file)
        faculty=file['faculty']
        name=file['name']
        track_number=file['track_number']
        flag=file['flag']

        ret_list=[track_number,flag,faculty,name]    #q=questions,action=p or n (+ve or -ve), flag shows semantic of the text (yes or no
        f.close()
        #print('file in if',file)
    else:                                            # if file is not created
        f=open('temp/'+str(sid)+'.json','w')
        file={}
        faculty=file['faculty']=''
        name=file['name']=''
        file['track_number']=0
        file['flag']=0

        track_number=file['track_number']
        flag=file['flag']
        ret_list=[track_number,flag,faculty,name]    #q=questions,action=p or n (+ve or -ve), flag shows semantic of the text (yes or no
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
        file[str(arg[0])]=arg[1]

    f=open('temp/'+str(argv[0][1])+'.json','w')
    json.dump(file,f)
    f.close()

def saving_feedback(saving_id,form_type):
    f=open('backend_final/responses/temp_'+str(saving_id)+'_responses.json','r')     # response
    data=json.load(f)
    f.close()
    os.remove('backend_final/responses/temp_'+str(saving_id)+'_responses.json')

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