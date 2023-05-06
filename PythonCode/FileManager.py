import requests
import json
import csv
import psycopg2

def airlines_response():
    url="https://api.instantwebtools.net/v1/airlines"
    response=requests.get(url,headers={"Accept":'application/json'})
    return response

def create_json(response,today_date):
    response_json=response.text
    file_name= f"airlines_{today_date}.json"
    with open(file_name,"w") as file:
        file.write(response_json)
    return file_name    

def json_to_csv(c_json,today_date):
    with open(c_json,'r') as json_file:
        jsondata = json.load(json_file)
    csv_filename=f'airlines2_{today_date}.csv'
    data_file = open(csv_filename, 'w', newline='')
    header=['id', 'name', 'country', 'logo', 'slogan', 'head_quaters', 'website','established']
    csv_writer = csv.DictWriter(data_file,fieldnames=header)
    csv_writer.writeheader()
    for f  in jsondata:
        if 'id' in f and f.get('id') != None:
            if f["id"] < 9223372036854775807:
                values={"id":f.get('id'),
                        "name":f.get('name'),
                        "country":f.get('country'),
                        "logo":f.get('logo'),
                        "slogan":f.get('slogan'),
                        "head_quaters":f.get('head_quaters'),
                        "website":f.get('website'),
                        "established":f.get('established')}
                csv_writer.writerow(values)
    return csv_filename