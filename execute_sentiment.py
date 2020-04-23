import json
import os
from backend_final.sentiment_analysis import sentiment
def get_data(form_name):
    
        
    #path="/var/www/FPSU/FPSU/backend_final/responses/"
    
    #filepath=os.path.join(path,form_name)
    #f=os.open(filepath, os.O_RDWR | os.O_CREAT)
    #data=os.read(f)
    f=open('/var/www/FPSU/FPSU/backend_final/responses/'+str(form_name),'r')
    
    
    data=json.load(f)
    
    f.close()
    #print(len(data))

    
    #  [u'41', u'51', u'61', u'71', u'81', u'101', u'111', u'141']
    #print(data)
    dictarray=[]
    dict={"data":[]}
    main_list={}
    main_list_reasons={}
    for i in data:
        list_in=[]
        list_reasons=[]
        list_temp=[]
        for j in data[i]:
            #print(j)
            list_temp.append((j[1:]))
        list_temp=sorted(list_temp,key=int)
        for k in list_temp:
            try:
                list_reasons.append(data[i]['q'+k]['negate']['data'])
            except: pass
            list_in.append(data[i]['q'+k]['data'])
        main_list_reasons[i]=(list_reasons)
        main_list[i]=(list_in)
    temp=[]
    for i in main_list:
        temp.append(main_list[i])
    #os.chdir('/var/www/FPSU/FPSU/backend_final')
    final_sent_values= sentiment.sentiment_return(temp)
    #print(final_sent_values)

    #print(main_list)
    #print(main_list_reasons)
    for i,j in zip(data,range(0,len(data))):
        dict_temp={}
        dict_temp['id']=i
        dict_temp['reasons']=main_list_reasons[i]
        dict_temp['sent_values']=final_sent_values[j]
        dict['data'].append(dict_temp)
    print(dict)
    return dict
#get_data('default_students_responses.json')