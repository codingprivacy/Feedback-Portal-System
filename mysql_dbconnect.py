import pymysql

def connect_to(datab=""):
    conn = pymysql.connect(host = "localhost",
                        user = "vatsal",
                        passwd = "finalyearproject",
                        db = datab)
    c = conn.cursor()

    return c, conn

def connection_to_pumis():
    conn = pymysql.connect(host = "localhost",
                        user = "vatsal",
                        passwd = "finalyearproject",
                        db = "pumis")
    c = conn.cursor()

    return c, conn

def connection_to_datahouse():
    conn = pymysql.connect(host = "localhost",
                        user = "vatsal",
                        passwd = "finalyearproject",
                        db = "datahouse")
    c = conn.cursor()

    return c, conn
