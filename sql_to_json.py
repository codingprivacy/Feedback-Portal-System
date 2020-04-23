import json
import gc
from mysql_dbconnect import *


resp = {}

def getusers():
    c, conn = connection_to_datahouse()
    c.execute("SELECT * FROM fdbck_resp_training")
    responses = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    gc.collect()

    return responses

rows = getusers()
for i in range(0,8):
    for j in range(0,10):
        if rows[i][j] == "":
            print("RESP_" + str(j+1) + " :  NULL")
        else:
            print("RESP_" + str(j+1) + " : " + str(rows[i][j]))
    print("\n")
