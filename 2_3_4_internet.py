import requests
import re

"""
res = requests.get("https://docs.python.org/3.5/")
print(res.status_code)
print(res.headers["Content-type"])

print(res.content)
print(res.text)

# picture
res = requests.get("https://docs.python.org/3.5/_static/py.png")
print(res.status_code)
print(res.headers["Content-type"])

#(res.content)

with open("python.png", "wb") as f:
    f.write(res.content)


res = requests.get("https://yandex.ru/search/", params={"text": "Stepic"})
print(res.status_code)
print(res.headers["Content-type"])
print(res.url)
print(res.text)



###########################################
url1 = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
url2 = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
flg = "No"
#print(requests.get(url1).text)

for url in re.findall(r"<a href=\"(.*)\">", requests.get(url1).text):
    if url2 in re.findall(r"<a href=\"(.*)\">", requests.get(url).text):
        flg = "Yes"
        break

print(flg)

"""

#fl = open("in_data.txt", "r").read()

import requests
import re

fl = requests.get("http://pastebin.com/raw/hfMThaGb")

link_pattern = re.compile(r"<a[^>]*?href=[\"|\'](.*?)[\"|\'][^>]*?>")
out = list()

for ln in link_pattern.findall(fl.text):
    print(ln)
    m = re.match(r"(\w+://)*(([\w|-]+[\.]*)*)", ln)

    if m is not None:
        out.append(m.group(2))

print("=== OUTPUT ===")
print(*sorted(set(out)), sep="\n")
print("=== END ===")
