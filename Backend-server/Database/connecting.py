import mysql.connector
import os



def connect_to_db():
    my_config={
        "host":"localhost",
        "port":3306,
        "user":"root",
        "password":"jothijpn@123",
        "database":"myproject"
       
    }
    connection=mysql.connector.connect(**my_config)
    return connection
   



def db_validation(user_query,user_params=[]):
    try:
        sqlconnection=connect_to_db()
        if sqlconnection:
            cursor=sqlconnection.cursor()
            cursor.execute(user_query,user_params)
            sqlconnection.commit()
            result=cursor.lastrowid
            print (result)
            print("hello")
        else:
            return False
    except Exception as err:
        return "error"


# def db_valid(user_query,user_params=[]):
#     try:
#         sqlconnection=connect_to_db()
#         if sqlconnection:
#             cursor=sqlconnection.cursor()
#             cursor.execute(user_query,user_params)
#             sqlconnection.commit()
#         else:
#             return False
#     except Exception as err:
#         return "error"

# def db_validation_withdraw(user_query,user_params=[]):
#     try:
#         sqlconnection=connect_to_db()
#         if sqlconnection:
#             cursor=sqlconnection.cursor()
#             cursor.execute(user_query,user_params)
#             sqlconnection.commit()
#         else:
#             return False
#     except Exception as err:
#         return "error"  


a= connect_to_db()
print(a)
















# def db_validation(user_query,user_params=[]):


# def db_validation(user_query,user_params=[]):
#     connect = sqlite3.connect("saran.db")
#     cursor = connect.cursor()
#     cursor.execute(user_query, user_params)
#     connect.commit()
#     print(connect)
#     return cursor


# db_validation(
#   """ CREATE TABLE TOKEN(
#     EMAIL TEXT PRIMARY KEY,
#     USER_NAME TEXT NOT NULL,
#     MOBILE INTEGER  NOT NULL,
#     CREDENTIALS TEXT NOT NULL)
#     """
#   )



