from backend_final import execute_sentiment
from mysql_dbconnect import *
import gc
import pickle
import sys

def save_data():
    c, conn = connect_to("")
    sentiment_json = execute_sentiment.get_data("default_students_responses.json")
    reasons_list = list()

    for obj in sentiment_json['data']:
        decoded_code = obj['id']
        semester = decoded_code[5]
        student_class = decoded_code[6:8]
        subject_fpsu_code = decoded_code[8:]
        c.execute("""SELECT faculty.first_name, faculty.last_name
                    FROM pumis.faculty
                    WHERE faculty.subject_fpsu_code=%s
                    AND faculty.class_alloted=%s
                    AND faculty.semester_alloted=%s""",(subject_fpsu_code, student_class, semester))
        resp = c.fetchall()
        faculty_firstname = resp[0][0]
        faculty_lastname = resp[0][1]
        faculty_fullname = faculty_firstname + " " + faculty_lastname
        reasons_list.append(obj['reasons'])

        try:
            c.execute("INSERT INTO datahouse.sentimented_data_values VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (obj['id'], obj['sent_values'][0], obj['sent_values'][1], obj['sent_values'][2], obj['sent_values'][3], obj['sent_values'][4], obj['sent_values'][5], obj['sent_values'][6], obj['sent_values'][7], faculty_fullname, semester))
        except Exception as e:
            continue

        reasons_list.append(obj['reasons'])

    conn.commit()
    c.close()
    conn.close()
    gc.collect()
    
    return reasons_list

def calculate_values(faculty_fullname, semester):
    c, conn = connect_to("datahouse")
    c.execute("SELECT * FROM sentimented_data_values WHERE faculty_fullname = %s AND semester IN %s ", (faculty_fullname, tuple(semester)))
    x = c.fetchall()

    positiveList = [0,0,0,0,0,0,0,0]
    negativeList = [0,0,0,0,0,0,0,0]

    for row in x:
        for i in range(1,9):
            if int(row[i]) == 1:
                positiveList[i-1] += int(row[i])
            else:
                negativeList[i-1] += int(row[i]) * (-1)

    return positiveList,negativeList

#print(calculate_values("Darshana Parmar",('8','6')))
#print(save_data())
