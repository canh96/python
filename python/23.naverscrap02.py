#네이버 웹페이지 긁어오기2
import requests as req

res = req.get('https://www.naver.com/')

print(res.content)