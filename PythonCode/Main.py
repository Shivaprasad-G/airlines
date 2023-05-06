import FileManager
import Db
from datetime import date 

#To create filenames with today date
today_date = str(date.today())

#Getting response from airlines url
response=FileManager.airlines_response() 
print("Got the Response from API")

#To create json file from json response
c_json=FileManager.create_json(response,today_date)
print(f"{c_json} is created")

#Converting json file to csv file
csv_filename=FileManager.json_to_csv(c_json,today_date)
print(f"{csv_filename} is created")

#Creating the postgres database connection
connection,cursor = Db.sql_conn() 

#Inserting  data into stg_airlines table 
stg=Db.stg_airlines(connection,cursor,csv_filename)
print(stg)

#Calling stored procedure to insert data into airlines
proc=Db.call_proc(connection,cursor)
print(proc)
connection.close()
