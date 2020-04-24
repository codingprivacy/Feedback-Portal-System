from flask import Flask, render_template, request, redirect, flash, url_for, session, jsonify
from mysql_dbconnect import *
from pymysql import escape_string as thwart
from bokeh.embed import components
from graphs import *
from secret_hash import *
from functools import wraps

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField

import customfunc
import execute_schedule
import _email
import gc
import os
import pickle
import json
import data_calculation
import wordcloud_generate

#Creating the Flask app.
app = Flask(__name__)

class Multi_Select_Form(FlaskForm):
    semester_type = SelectField('semester_type', choices=[('default', 'Select any entry'), ('even', 'Even'), ('odd', 'Odd')])
    semester_list = SelectField('semester_list', choices=[])
    class_list = SelectField('class_list', choices=[])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


#Created a login_required wrapper function that wraps other functions in-order to force to do login first before accessing any pages.
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('admin_login'))
    return wrap
@app.route('/admin/triggeranalysis/success/', methods = ['GET', 'POST'])
def admin_trigger_analysis_success():
    if request.method == "POST":
        return render_template("triggeranalysis_success.html")

@app.route('/admin/triggeranalysis/')
def admin_trigger_analysis():
    return render_template("triggeranalysis.html")

#Route and function for about functionality.
@app.route('/admin/about/', methods = ['GET', 'POST'])
def admin_about():
    return render_template("about.html")


#Route and function for logs functionality.
@app.route('/admin/logs/', methods = ['GET', 'POST'])
def admin_logs():
    c, conn = connect_to("fpsu")
    c.execute("SELECT * FROM email_logs")
    x = c.fetchall()

    c.close()
    conn.close()
    gc.collect()

    logs = []
    for row in x:
        log = dict(timestamp=str(row[0]), email=str(row[1]), decoded_code=str(row[2]))
        logs.append(log)
    return render_template("logs.html", logs=logs)


#Route and function for schedule success functionality.
@app.route('/admin/schedule/done/', methods = ['GET', 'POST'])
def admin_schedule_success():
    if request.method == "POST":
        try:
            semester_type = request.form['semester_type']
            semester_list = request.form['semester_list']
            class_list = request.form['class_list']

            class_list_json = []
            c, conn = connect_to("pumis")
            if semester_list == "all":
                if semester_type == "even":
                    semester_list = ["2", "4", "6", "8"]
                    for sem in semester_list:
                        c.execute("SELECT class FROM semester_info WHERE semester IN (%s)", (sem))
                        x = c.fetchall()
                        for i in x:
                            class_list_json_Obj = {}
                            class_list_json_Obj['semester'] = sem
                            class_list_json_Obj['class'] = i[0]
                            class_list_json.append(class_list_json_Obj)

                else:
                    semester_list = ["1", "3", "5", "7"]
                    for sem in semester_list:
                        c.execute("SELECT class FROM semester_info WHERE semester IN (%s)", (sem))
                        x = c.fetchall()
                        for i in x:
                            class_list_json_Obj = {}
                            class_list_json_Obj['semester'] = sem
                            class_list_json_Obj['class'] = i[0]
                            class_list_json.append(class_list_json_Obj)

                c.close()
                conn.close()
                gc.collect()

            else:
                if class_list == "all":
                    c.execute("SELECT class FROM semester_info WHERE semester IN (%s)", (semester_list))
                    x = c.fetchall()
                    for i in x:
                        class_list_json_Obj = {}
                        class_list_json_Obj['semester'] = semester_list
                        class_list_json_Obj['class'] = i[0]
                        class_list_json.append(class_list_json_Obj)

                    c.close()
                    conn.close()
                    gc.collect()

                else:
                    class_list_json_Obj = {}
                    class_list_json_Obj['semester'] = semester_list
                    class_list_json_Obj['class'] = class_list
                    class_list_json.append(class_list_json_Obj)

            semclass_combo = jsonify({"semclass_combo" : class_list_json}).get_data(as_text=True)
            emailing_data = execute_schedule.generate_list(semclass_combo)
            EMAIL_COUNT = 0
            for row in emailing_data:
                _email.send_email(row[1], row[2], row[3])
                EMAIL_COUNT += 1

            err = "Email has been sent successfully."
            return render_template("schedule_success.html", err=err, EMAIL_COUNT = EMAIL_COUNT)
        except Exception as e:
            return render_template("schedule_success.html", err=str(e))


#Route and function for schedule functionality.
@app.route('/admin/schedule/', methods = ['GET', 'POST'])
def admin_schedule():
    multi_select_form = Multi_Select_Form()
    multi_select_form.semester_list.choices = [("default", "Select any entry")]
    multi_select_form.class_list.choices = [("default", "Select any entry")]
    return render_template("schedule.html", form=multi_select_form)


#Route for AJAX. Function to handle list of semesters.
@app.route('/admin/schedule/semester/<semester_type>')
def semester_list(semester_type):
    semesterArray = []
    if semester_type == "even":
        semesters = [8, 6, 4, 2]
        for sem in semesters:
            semesterObj = {}
            semesterObj['id'] = int(sem)
            semesterObj['name'] = str(sem)
            semesterArray.append(semesterObj)
    else:
        semesters = [7, 5, 3, 1]
        for sem in semesters:
            semesterObj = {}
            semesterObj['id'] = int(sem)
            semesterObj['name'] = str(sem)
            semesterArray.append(semesterObj)
    semesterObj = {}
    semesterObj['id'] = "all"
    semesterObj['name'] = "All"
    semesterArray.append(semesterObj)
    return jsonify({"semesters" : semesterArray})


#Route for AJAX. Function to handle list of classes.
@app.route('/admin/schedule/class/<semester>')
def class_list(semester):
    classArray = []
    classes = customfunc.get_class_list(semester)
    for _class in classes:
        classObj = {}
        classObj['id'] = _class
        classObj['name'] = _class
        classArray.append(classObj)
    classObj = {}
    classObj['id'] = "all"
    classObj['name'] = "All"
    classArray.append(classObj)
    return jsonify({"classes" : classArray})


#Route and function for analysis show report functionality. A next page for analysis.html
@app.route('/admin/analysis/showreport/', methods = ['GET', 'POST'])
def admin_analysis_showreport():
    if request.method == "POST":
        try:
            err = ""
            faculty_name = request.form['faculty_name']
            semester = request.form.getlist('semester')
            c, conn = connect_to("pumis")
            c.execute("SELECT post, dept, institute, email, id, avatar FROM faculty_new WHERE full_name=(%s)", (faculty_name))
            x = c.fetchone()
            c.close()
            conn.close()
            gc.collect()
            post = x[0]
            dept = x[1]
            institute = x[2]
            email = x[3]
            id = x[4]
            avatar = x[5]
            dept = dept + " Department"
            img_file_link = "/static/images/faculties/" + avatar
            faculty_mailto_email = "mailto:" + str(email)
            #positiveList

            positiveList,negativeList=data_calculation.calculate_values(faculty_name,tuple(semester))
            RAW_MESSAGES = data_calculation.save_data()
            wordcloud_generate.generate_graph()
            return render_template("showreport.html", err=err, faculty_name=faculty_name, img_file_link=img_file_link, faculty_mailto_email=faculty_mailto_email, post=post, dept=dept, institute=institute, id=id, positiveList=positiveList, negativeList=negativeList, RAW_MESSAGES=RAW_MESSAGES)

        except Exception as e:
            return render_template("showreport.html", err=str(e), faculty_name=faculty_name, img_file_link=img_file_link, faculty_mailto_email=faculty_mailto_email, post=post, dept=dept, institute=institute, id=id, RAW_MESSAGES=RAW_MESSAGES)



#Route and function for analysis functionality.
@app.route('/admin/analysis/', methods = ['GET', 'POST'])
def admin_analysis():
    c, conn = connect_to("pumis")
    c.execute("SELECT first_name, last_name FROM faculty GROUP BY first_name, last_name")
    data = c.fetchall()
    c.close()
    conn.close()
    gc.collect()
    full_name_list = list()
    for i in data:
        full_name_list.append(i[0] + " " + i[1])

    return render_template('analysis.html', full_name_list=full_name_list)


#Route and function for create form success functionality.
@app.route('/admin/createform/success/', methods=["GET", "POST"])
def admin_createform_success():
    try:
        err = ""
        if request.method == "POST":
            FORMS_LIST_count = customfunc.count_forms()
            form_name = request.form['form_name']
            new_quest_list = list()
            for i in range(1, 11):
                new_quest_list.append(str(request.form["new_quest_" + str(i)]))

            resp = customfunc.jsonifyforms(form_name, new_quest_list)

            if resp == True:
                err = "Your form has been saved. FeedBot has started learning from it!"
                return render_template("createform_success.html", err=err, FORMS_LIST_count=FORMS_LIST_count)

            else:
                err = "Something went wrong. Please try agani or contact admin."
                return render_template("createform_success.html", err=err, FORMS_LIST_count=FORMS_LIST_count)

        return render_template("createform_success.html", err=err, FORMS_LIST_count=FORMS_LIST_count)

    except Exception as e:
        return render_template("createform_success.html", err=str(e), FORMS_LIST_count=FORMS_LIST_count)


#Route and function for create form functionality.
@app.route('/admin/createform/')
def admin_createform():
    FORMS_LIST = customfunc.list_out_forms()
    FORMS_LIST_count = customfunc.count_forms()
    return render_template("createform.html", FORMS_LIST=FORMS_LIST, FORMS_LIST_count=FORMS_LIST_count)


#Route and function for log out.
@app.route('/admin/logout/')
@login_required
def admin_logout():
    err = "You have been successfully logged out."
    session.clear()
    gc.collect()
    return render_template("login.html", err=err)


#Route and function for admin dashboard.
@app.route("/admin/dashboard/", methods=["GET", "POST"])
@login_required #login_required wrapper created above is used here. It should be always placed under the main Flask app wrapper.
def admin_dashboard():
    return render_template("dashboard.html")

#Route and function for admin login.
@app.route("/admin/login/", methods=["GET", "POST"])
def admin_login():
    err="" #Defining err a login page jinja variable.
    try:
        #Authenticating username and password with database.
        c, conn = connect_to("fpsu")
        if request.method=="POST":
            username = request.form['username']
            c.execute("SELECT password FROM user WHERE email = (%s)", (username))
            password_stored = c.fetchone()[0]
            password = request.form['password']
            if password == password_stored:
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('admin_dashboard')) #Redirect to admin dashboard page if login is successful.
            else:
                err = "Invalid Credentials. Please try again!" #Error message defined.

        return render_template("login.html", err=err) #Returning login page again in case of above authentication fails, alongwith err in jinja variable names err.
    except Exception as e:
        return render_template("login.html", err=str(e)) #DEBUG PURPOSE : Exception Handling with passing exception message into jinja varialbe err.


#Route and function for chatbot with unique_route_string.
@app.route('/chatbot/<unique_route_string>', methods=['GET'])
def chatbot_page(unique_route_string):
    try:
        c, conn = connect_to()
        c.execute("SELECT enrollment_number FROM fpsu.route_string WHERE string=%s", (unique_route_string))
        enrollment_number = (c.fetchall()[0])[0]
        decrypted_string = decrypt_string(unique_route_string.encode())
        sem = decrypted_string[5]
        student_class = decrypted_string[6:8]
        subject_fpsu_code = decrypted_string[8:]
        c.execute("""SELECT faculty.first_name, faculty.last_name, subject.subject_name
                    FROM pumis.faculty, pumis.subject
                    WHERE faculty.subject_fpsu_code=%s
                    AND faculty.class_alloted=%s
                    AND faculty.semester_alloted=%s""",(subject_fpsu_code, student_class, sem))
        resp = c.fetchall()
        faculty_firstname = resp[0][0]
        faculty_lastname = resp[0][1]
        subject_name = resp[0][2]
        c.close()
        conn.close()
        gc.collect()
        return render_template("chatbot.html")
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run()
