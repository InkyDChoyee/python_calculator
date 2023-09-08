import requests
from bs4 import BeautifulSoup

r = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8")
bs = BeautifulSoup(r.content, "html.parser")

whether = bs.select_one("div.temperature_text > strong > span.blind")

print("내가 알고싶은 것은{}입니다".format(whether.text))