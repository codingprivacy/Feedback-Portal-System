import gmail
from mysql_dbconnect import *
import datetime
import _logs


def send_email(first_name, email_id, route_string):
    subject = "This is Emailing TEST. Do not respond to BOT. #ByVatsal"
    bodyHTML = 'Hey there, <br><br>Howdy %s ? I am FeedBot. I request you to please fill the feedback form by clicking <a href="http://134.209.42.61/chatbot/%s">here</a>.<br><br>It would not take much time.<br><br><br><a href="https://codingprivacy.github.io">CodingPrivacy.</a>' %(first_name, route_string)
    gmail.send_message(email_id, subject, bodyHTML)
    _logs.save_logs(email_id, route_string)
    #f.write( "nitindlalwani@gmail.com" + " " + subject + " " + str(datetime.datetime.utcnow()))
