import json
from mysql_dbconnect import *
import gc


def generate_list(semclass_combo):
    semclass_combo_json = json.loads(semclass_combo)
    c, conn = connect_to()
    emailing_data = list() # [enrollment_number, first_name, email_id, route_string]
    for entry in semclass_combo_json['semclass_combo']:
        c.execute("SELECT student.enrollment_number, first_name, email_id, route_string.string FROM pumis.student, fpsu.route_string WHERE semester=(%s) AND student_class=(%s) AND student.enrollment_number = route_string.enrollment_number", (entry["semester"], entry["class"]))
        x = c.fetchall()
        for row in x:
            row_list = list()
            row_list.append(row[0])
            row_list.append(row[1])
            row_list.append(row[2])
            row_list.append(row[3])
            emailing_data.append(row_list)
        c.close()
        conn.close()
        gc.collect()

    return emailing_data
