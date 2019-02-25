from flask import Flask,request
from flask_socketio  import SocketIO, emit
from backend import main

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('start_event')
def handleMessage(msg):
    print("message",msg)
    question=main.get_question(request.sid,"form1")
    #print(question)
    emit('my_response',question)

@socketio.on('send_answar')
def question(msg):
    #print(msg)
    main.save_answar(request.sid,msg,"form1")
    question=main.get_question(request.sid,"form1")
    #print(question)
    emit('get_question',question)


if __name__ == '__main__':
    socketio.run(app)
