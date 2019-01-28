"""
### - Task - Base - http://openweathermap.org
import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"
city = "Minsk"
template = "Current temperature in {} is {}"

params = {
    "q": city,
    "appid": "11c0d3dc6093f7442898ee49d2430d20",
    "units": "metric"
}

res = requests.get(api_url, params=params)
#print(res.status_code)
#print(res.json())

data = res.json()
print(template.format(city, data["main"]["temp"]))


### - Task - 1 - http://numbersapi.com/
import requests

api_url ="http://numbersapi.com/<number>/math?json=true"

with open("in_data.txt", "r") as fl:
    for ln in fl:
        ln = ln.strip()
        res = requests.get(api_url.replace("<number>", ln))
        if res.json()["found"]:
            print("Interesting")
        else:
            print("Boring")

"""

### - Task - 2 - http://artsy.net

import requests
import json

client_id = 'a9c1a391f28784d77dfc'
client_secret = '3d080be1499dc5c03b0a573faed83cee'
d = {}

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}


with open("in_data.txt", "r") as fl:
    for ln in fl:
        ln = ln.strip()

        # инициируем запрос с заголовком
        r = requests.get("https://api.artsy.net/api/artists/{id}".format(id=ln), headers=headers)
        r.encoding = 'utf-8'
        # разбираем ответ сервера
        j = json.loads(r.text)
        #print(j)
        d[j["sortable_name"]] = j["birthday"]

d = sorted(d.items(), key=lambda kv: [kv[1], kv[0]])

#print(*d)

for l in d:
    print(l[0])
