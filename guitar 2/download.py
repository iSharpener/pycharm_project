import urllib
import requests
import time

headers={
    "Accept": "itext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID=rqbn7uhkt2dhd2q03kt0fsftm1; Hm_lvt_dca7dc99d8ac55393ef7fbc057d85ffb=1526026130; bdshare_firstime=1526026130077; cnum_2=dwED_; cnum_300791=wCrmv; Hm_lpvt_dca7dc99d8ac55393ef7fbc057d85ffb=1526102981",
    "Host": "www.qupu123.com",
    "Referer": "http://www.qupu123.com/get_img/314042/3/4ff1e66c91",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}
imgurl = 'http://www.qupu123.com/tempimg/314042/3/2/102ff00458'
imgpath = '/Users/xiaopeng/Music/download'+'/test.png'
r = requests.post("http://www.qupu123.com/get_img/314042/3/4ff1e66c91",headers = headers)

print(dir(r))
print(r.json)

req = requests.get(imgurl,headers = headers)
print(req)
with open("test.png","wb") as f:
    f.write(req.content)


#urllib.request.urlretrieve(img_url,)