import pymysql


def insert_db(actid):
    host = 'Local mysql server ip' #default 127.0.0.1
    user = 'Username'
    password = 'Password'
    port = 3306 #default
    db = 'Database name'
    data_base = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
    cursor = data_base.cursor()
    try:
        sql = "INSERT INTO act(actid) VALUES (%d)" % (actid)
        cursor.execute(sql)
        data_base.commit()
    except ValueError as e:
        print(e)
        data_base.rollback()
    finally:
        cursor.close()
        data_base.close()


def select_db(actid):
    host = 'Local mysql server ip' #default 127.0.0.1
    user = 'Username'
    password = 'Password'
    port = 3306 #default
    db = 'Database name'
    data_base = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
    cursor = data_base.cursor()
    try:
        sql = "select isnull((select actid from act where actid=%d))" % (actid)
        cursor.execute(sql)
        data=cursor.fetchone()
        data_base.commit()
    except ValueError as e:
        print(e)
        data_base.rollback()
    finally:
        return data[0]
