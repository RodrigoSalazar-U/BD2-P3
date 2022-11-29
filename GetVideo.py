import requests
import subprocess

import wget
from requests.structures import CaseInsensitiveDict
import time
import os
from google.cloud import pubsub_v1
import json
import hashlib

credentials_path = '/home/software2_utec/PubVideoGoogle/double-backup-369500-6723c8f08472.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/double-backup-369500/topics/wifi'

#url = "https://api.telegram.org/bot5960321871:AAF-MiS07aKNj_ktcUB6qiKsnWy6TISjjlY/getUpdates"
url = "https://api.telegram.org/bot5960321871:AAF-MiS07aKNj_ktcUB6qiKsnWy6TISjjlY/"
url_image = "https://api.telegram.org/file/bot5960321871:AAF-MiS07aKNj_ktcUB6qiKsnWy6TISjjlY/"
url_photo = "https://api.telegram.org/bot5960321871%3AAAF-MiS07aKNj_ktcUB6qiKsnWy6TISjjlY/sendPhoto"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
last_query = 0

post_json = {
    "user" : "",
    "time" : "",
    "format" : "",
}

ultimo=""
actual=""
ruta=["",""]
while True:
    resp = requests.get(url+"getUpdates", headers=headers)
    data = resp.json()
    #actual=str(data)
    tipo = "texto"
    if data['result'][-1]['message']['from']['is_bot'] == False:
        if(len(data['result'])==1):
            time.sleep(1)
            continue
        if('text' in data['result'][-1]['message']):
            tipo="texto"
            actual=str(data['result'][-1]['message']['text'])
        elif ('photo' in data['result'][-1]['message']):
            tipo="foto"
            actual=str(data['result'][-1]['message']['photo'][-1]['file_id'])
        if(actual==ultimo):
            print(actual)
            ultimo=actual
            time.sleep(1)
            continue
        else:
            ultimo=actual
            if(tipo=="foto"):
                payload = {"file_id": actual}
                headers = {
                    "accept": "application/json",
                    "content-type": "application/json"
                }
                response = requests.post(url+"getFile", json=payload, headers=headers).json()['result']['file_path']
                
                wget.download(url_image+response,out="/home/software2_utec/BD2-P3/new_data/photos/")
                ruta[0]="/home/software2_utec/BD2-P3/new_data/"+response
            else:
                ruta[1]=data['result'][-1]['message']['text']
                
            if(ruta[0]!="" and ruta[1]!=""):
                print("EJECUTANDOSE")
                if(ruta[1].split()[0] == "seq"): 
                    results=subprocess.check_output(["python3","seq.py","-n",ruta[1].split()[1],"-f",str(ruta[0])])
                if(ruta[1].split()[0] == "rt"): 
                    results=subprocess.check_output(["python3","rt.py","-n",ruta[1].split()[1],"-f",str(ruta[0])])
                if(ruta[1].split()[0] == "kd"): 
                    results=subprocess.check_output(["python3","kdtree.py","-n",ruta[1].split()[1],"-f",str(ruta[0])])
                for val in str(results).replace("'","").split("\\n"):

                    if val != "":
                        actual = val.split(" ")[0]
                        if(actual[0] == "b"):
                            #print("ESTO ES VAL: ",val.split(" ")[0][1:-1])
                            actual = val.split(" ")[0][1:-1]
                        if(actual[-1] == "p"):
                            actual = actual + "g"
                        print(actual)
                        data = {'photo':'foto','chat_id':'-1001774229640'}
                        #print(val.split(" ")[0][1:-1])
                        if(actual[0] == '"'):
                            actual = actual[2:-1]
                        elif(actual[-1] == 'p'):
                            actual = actual + 'g'
                        files={'photo':open("/home/software2_utec/BD2-P3/"+actual,'rb')}
                        requests.post(url_photo+"?chat_id="+data['chat_id'],files=files)

                #print(str(results).split("\\n")[0])



            

        '''
        message = data['result'][-1]['message']['text'].lower()
        words = message.split()
        if words[0] == 'grabar':
            query = data['result'][-1]['update_id'] 
            post_json['user'] = data['result'][-1]['message']['from']['id']
            post_json['time'] = int(words[1])
            post_json['format'] = words[2][:3]
            if last_query != query:
                json_string = json.dumps(post_json)
                json_string = json_string.encode('utf-8')
                #print(json_string)
                future = publisher.publish(topic_path, json_string)
                #print(f'Published message id {future.result()}')
                last_query = query
        '''

        #time.sleep(1)
