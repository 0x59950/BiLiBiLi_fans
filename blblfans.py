import requests
import json

t = ["1314", "1111", "1234", "187603749", "13076861",       #test
     "365135915", "8366990", "456664753", "20165629",      #欣小萌  欣小萌  央视新闻  共青团中央
     ]      # uuid合集  往列表(数组)里加就可以了
for x in t:
    a = requests.get("https://api.bilibili.com/x/web-interface/card?mid="+x)
    # print(a)
    print(a.text)
    i = json.loads(a.text)
    name = i["data"]["card"]["name"]
    fans = i["data"]["card"]["fans"]
    print(name+'\t'+str(fans))
