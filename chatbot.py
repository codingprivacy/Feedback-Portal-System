from flask import Flask,request,render_template
import time
import json
from flask_socketio  import SocketIO, emit
from backend_final import default
from backend_final import custom
import intro


app = Flask(__name__)
socketio = SocketIO(app)

intro_result=[]
form_type=""
saving_id=""

@socketio.on('start_event')
def handleMessage(msg):
    global intro_result,form_type,saving_id
    print("handle_message",msg)
    msg=msg['data'].split('/')[4]
    intro_result=intro.get_data(msg)          #gets the student name and faculty name
    form_type='default_students'
    saving_id=intro_result[0]
    print('saving_id',saving_id)
    #saving_id="Ack8ytVGE50eYKMiGq0GCufusPGQLF48RFu9wV1cvJefpOx77gMhi4O_m3fFwtoRPsFU5hNhAcEM4edLlifD8Owk4_cA=="
    #intro_result=['Vatsal','Nirali Naik','Assistent Professor','Computer Science and Engineering','PIET','nirali.naik@paruluniversity.ac.in']
    with open('backend_final/images/nirali_naik.jpg', 'rb') as f:
        image_data = f.read()
        emit('get_faculty', {'image_data': intro_result[6],'fac_name':intro_result[2],'fac_desig':intro_result[3],'fac_dept':intro_result[4],'fac_insti':intro_result[5]})
        #print('get_faculty_done')
    #getting suggestions
    f=open('backend_final/corpus_pool/suggestions.json','r')
    emit('suggestions',json.load(f))
        #print('get_faculty_done')

@socketio.on('greet_event')

def handleMessage(msg):
    if(form_type=="default_students"):
        print('faculty',intro_result[2])
        question=default.default_question(request.sid,saving_id,[intro_result[2],intro_result[1]])
    else:
        question=custom.greeting(request.sid,[intro_result[2],intro_result[1]])
        print()
        #question=custom.question(request.sid,form_type,[intro_result[1],intro_result[0]])
    if(isinstance(question,list)):
        text=''
        for i in question:
            #print(i,'start here')
            text=text+i+'\n'

            #print(i,'end here')
        emit('get_question',text)
    else:
        #print('here finally')
        emit('get_question',question)

@socketio.on('send_answar')
def question(msg):
    #print(msg)
    if(form_type=="default_students"):
        default.default_answar(request.sid,msg,saving_id)    #taking answar
        question=default.default_question(request.sid,saving_id)    #sending question
    else:
        question=custom.custom_answar(request.sid,form_type,msg,saving_id)
        question=custom.custom_question(request.sid,form_type,saving_id)
    #print('question',question)
    if(isinstance(question,list)):
        text=''
        for i in question:
            text=text+i+'\n'
        emit('get_question',text)
    else:
        time.sleep(0.1)
        emit('get_question',question)

@app.route("/home")
def main_file():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)
