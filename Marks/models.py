from django.db import models
import pymysql

db=pymysql.connect('localhost','root','root','DBMS')

cursor=db.cursor()

print("Database connectivity done....")


