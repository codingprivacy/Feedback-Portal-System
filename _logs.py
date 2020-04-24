import datetime
from mysql_dbconnect import *
import gc
from secret_hash import *


def save_logs(email, route_string):
    decoded_code = decrypt_string(route_string)
    timestamp = str(datetime.datetime.now())
    c, conn = connect_to("fpsu")
    c.execute("INSERT INTO email_logs VALUES(%s, %s, %s)", (timestamp, email, decoded_code))
    conn.commit()
    c.close()
    conn.close()
    gc.collect()
