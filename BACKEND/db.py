import oracledb

def get_connection():
    conn = oracledb.connect(
        user="MI_DESPENSA_VIRTUAL",
        password="MI_DESPENSA_VIRTUAL",
        dsn="localhost/XE"
    )
    return conn
