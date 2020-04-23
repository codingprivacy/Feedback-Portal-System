from mysql_dbconnect import *
from pymysql import escape_string as thwart
import gc
from secret_hash import *

def save_to_db(encrypted_string, enr_num):
    c, conn = connect_to()
    c.execute("INSERT INTO fpsu.route_string VALUES(%s, %s)", (encrypted_string, enr_num))
    conn.commit()
    c.close()
    conn.close()
    gc.collect()

def generate_string():
    c, conn = connect_to("pumis")
    c.execute("""SELECT
                student.enrollment_number,
                student.first_name,
                student.last_name,
                student.semester,
                student.student_class,
                subject.subject_fpsu_code
                FROM student, faculty, subject
                WHERE faculty.subject_fpsu_code=subject.subject_fpsu_code
                AND student.student_class=faculty.class_alloted
                AND student.semester=faculty.semester_alloted ORDER BY student.student_class""")
    fetched_data = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    gc.collect()
    count = 0
    for i in fetched_data:
        enr_num = str(i[0])
        f_name = str(i[1])
        l_name = str(i[2])
        sem = str(i[3])
        stu_class = str(i[4])
        subject_fpsu_code = str(i[5])
        generated_code = enr_num[9] + f_name[0] + enr_num[10] + l_name[0] + enr_num[11] + sem + stu_class + subject_fpsu_code
        count+=1
        encrypted_string = encrypt_string(generated_code)
        decrypted_string = decrypt_string(encrypted_string)
        save_to_db(encrypted_string, enr_num)


generate_string()
