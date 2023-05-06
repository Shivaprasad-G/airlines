import csv
import psycopg2
from datetime import date 
import FileManager

def sql_conn():
    connection=psycopg2.connect(host="localhost",dbname="postgres",user="postgres",password="21021996",port=5432)
    cursor=connection.cursor()
    return connection,cursor

def stg_airlines(connection,cursor,csv_filename):
    cursor.execute("truncate table data_project.stg_airlines")
    connection.commit() 
    file=open(csv_filename,'r')
    data=csv.reader(file)
    header=next(data)
    for d in data:
        cursor.execute("insert into data_project.stg_airlines values (%s,%s,%s,%s,%s,%s,%s,%s)",d)         
    connection.commit()    

    return f"inserted values in to {csv_filename} table " 
def call_proc(connection,cursor):
    cursor.execute("call data_project.sp_airlines()")
    connection.commit()
    return "data entered in data_project.airlines table"
    
    
