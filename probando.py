import requests

url = "https://api.telegram.org/bot5960321871%3AAAF-MiS07aKNj_ktcUB6qiKsnWy6TISjjlY/sendPhoto"

data={'photo':'foto','chat_id':"-1001774229640"}

files={'photo':open('/home/software2_utec/BD2-P3/data/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg','rb')}

headers = {}

status = requests.post(url+"?chat_id="+data['chat_id'], files=files)

print(status.text)


#print(response.text)
