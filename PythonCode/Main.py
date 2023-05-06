import FileManager
import Db
from datetime import date 

today_date =str(date.today())

#Getting response from url
response=FileManager.airlines_response() 
print("Got the Response from API")
#To create json file Today date

c_json=FileManager.create_json(response,today_date)
print(f"{c_json} is created")

#convert json to csv
csv_filename=FileManager.json_to_csv(c_json,today_date)
print(f"{csv_filename} is created")

#create connection
connection,cursor = Db.sql_conn() 

#pass data into stg_airlines table
 
stg=Db.stg_airlines(connection,cursor,csv_filename)
print(stg)
#calling stored procedure for data enter into airlines
proc=Db.call_proc(connection,cursor)
print(proc)
connection.close()
