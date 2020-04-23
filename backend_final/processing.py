__author__ = 'Harsh Patel'
import json
import random

#     * for faculty , + for student


def q1(faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/greetings.json','r')
    j_file=json.load(file)
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
def q2(faculty,user):    #interrupted bye
    file=open('backend_final/Data/bye.json','r')
    j_file=json.load(file)
    j_file=j_file['interrupted']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
    if(isinstance(j_file[r_number],list)):   #if it is a list, display all values
        lista=[]
        for j in j_file[r_number]:
            j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
            j=str(j).replace('+',user)
            lista.append(j)
            print(j)
        return lista
    else:
        j_file[r_number]=str(j_file[r_number]).replace('*',faculty)
        j_file[r_number]=str(j_file[r_number]).replace('+',user)
        return str(j_file[r_number])
def q3(faculty="Nirali Naik",user="Harsh"):     #good_bye finally
    file=open('backend_final/Data/bye.json','r')
    j_file=json.load(file)
    j_file=j_file['good_bye']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])
def q4(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['course_completion']

    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    #print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
       # print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
def q4_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['course_completion_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])
def q5(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['punctuality']

    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    #print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
       # print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
def q5_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['punctuality_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])
def q6(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['creativity']
    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
        #print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
def q6_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['creativity_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])
def q7(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['solving_problems']

    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
       # print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
def q7_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['solving_problems_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])
def q8(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['knowledge']

    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    #print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
       # print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
def q8_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['knowledge_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])
def q9(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['mode_of_teaching']

    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    #print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
       # print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
def q9_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['mode_of_teaching_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])

def q10(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['motivate']

    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    #print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
       # print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
def q10_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['motivate_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])
def q11(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['interaction']

    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    #print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
       # print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
def q11_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['interaction_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])
def q12(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['pedagogical_effectiveness']

    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    #print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
       # print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
def q12_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['pedagogical_effectiveness_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])
def q13(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['classroom_env']

    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    #print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
       # print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
def q13_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['classroom_env_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])

def q14(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['communication_skills']

    #print('at_start',no_tracker)
    #print(no_tracker)
    range_list=range(1,len(j_file)+1)
    #print(len(j_file))
    question_no=random.randint(1,len(j_file))   #taking random value
    #print(len(no_tracker),len(range_list))
    if(len(no_tracker)!=len(range_list)):
        #print('in loop')
        print(question_no,no_tracker)
        while(question_no in no_tracker):
            question_no=random.randint(1,len(j_file))
            #print('in loop',question_no,no_tracker)
        #print(question_no)
        #print(j_file[question_no])
        #print(len(question_no[0]))
        r_number=random.randint(1,len(j_file[str(question_no)]))
        #print(j_file[question_no][str(r_number)])
        #input()
       # print(j_file[question_no][str(r_number)])
        if(isinstance(j_file[str(question_no)][str(r_number)],list)):   #if it is a list, display all values
            lista=[]
            for j in j_file[r_number]:
                j=str(j).replace('*',faculty)       #replacement * for faculty and + for student
                j=str(j).replace('+',user)
                lista.append(j)
                #print(lista)
            if((len(no_tracker))+1==len(range_list)):
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,lista]
            else:
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,lista]
        else:
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('*',faculty)
            j_file[str(question_no)][str(r_number)]=str(j_file[str(question_no)][str(r_number)]).replace('+',user)
            if((len(no_tracker))+1==len(range_list)):
                #print('question_no',question_no)
                no_tracker.append(question_no)
                #print(no_tracker)
                return ['finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]
            else:
                no_tracker.append(question_no)
                #print('question_no',question_no)
                #print(no_tracker)
                return ['not_finish',no_tracker,str(j_file[str(question_no)][str(r_number)])]

def q14_negate(no_tracker,faculty="Nirali Naik",user="Harsh"):
    file=open('backend_final/Data/characteristics.json','r')
    j_file=json.load(file)
    j_file=j_file['communication_skills_negate']
    r_number=random.randint(1,len(j_file))   #taking random value
    r_number=str(r_number).decode("utf-8")
    #print(r_number)
    # for i in j_file:
    #     print(type(i))
    #     print(j_file[i])
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
        return str(j_file[r_number])