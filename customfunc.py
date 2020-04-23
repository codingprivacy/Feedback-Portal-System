import os
import json
from mysql_dbconnect import *
import gc


forms_dir_path = "/var/www/FPSU/FPSU/alg252kjaglasj/forms/"

def jsonifyforms(form_name, new_quest_list):
    try:
        file_name = form_name + ".json"
        file_path = os.path.join(forms_dir_path, file_name)
        data = {}
        for i in range(10):
            data['q' + str(i+1)] = new_quest_list[i]
        json_data = json.dumps(data)
        f = os.open(file_path, os.O_RDWR | os.O_CREAT)
        os.write(f, json_data)
        os.close(f)
        return True

    except Exception as e:
        return False

def list_out_forms():
    return os.listdir(os.path.join(forms_dir_path, ""))

def count_forms():
    return len(list_out_forms())

def get_class_list(semester):
    c, conn =  connect_to("pumis")
    c.execute("SELECT class FROM semester_info WHERE semester IN (%s)", str(semester))
    x = c.fetchall()
    c.close()
    conn.close()
    gc.collect()
    class_list = list()
    for i in x:
        class_list.append(i[0])

    return class_list
