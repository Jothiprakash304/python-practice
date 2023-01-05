from flask import Flask
from flask_jwt_extended import JWTManager
# from flask_mysqldb import MySQL
# import MySQLdb.cursors

from datetime import timedelta


ACCESS_EXPIRES=timedelta(seconds=30)

app=Flask(__name__)
app.config["JWT_SECRET_KEY"]="JOTHI"
app.config["JWT_ACCESS_TOKEN"]=ACCESS_EXPIRES
jwt=JWTManager(app)

# app.config['MYsql_host']="localhost"
# app.config["MYSQL_USER"]="root"
# app.config["MYSQL_PASSWORD"]="jothijpn@123"
# app.config["MYSQL_DB"]="myproject"

# mysql=MySQL(app)
from app import routes