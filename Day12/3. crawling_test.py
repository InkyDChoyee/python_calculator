# html에 사용할 모듈 만들기

# requests = 요청을 위한 라이브러리
# BeartifulSoup = 

import requests
from bs4 import BeautifulSoup

# print(requests.get("https://www.naver.com"))  # Response 200 = 정상작동O
#r = requests.get("https://www.naver.com")
# print(r.content)   # 자료의 원시값 => 16비트로 보여줌
# print(r.text)   # html 구조로 출력
#bs = BeautifulSoup(r.content, "html.parser")
# print(bs)
#h3 = bs.select("h3")  # select = 인자로 입력한 요소 전부를 선택
#print(h3[0].text) # 요소 가운데 text 요소만 선택
                  # select를 사용하는 경우 list 형태로 반환하기 때문에
                  # 인덱스를 직접 지정해주어야 한다

r = requests.get("https://www.naver.com")
bs = BeautifulSoup(r.content, "html.parser")

#h3 = bs.select_one("h3 > a")  # 자식요소를 선택할 때 = '>'사용
#selecter = bs.select_one("div.current_box")  # 클래스 속성 선택 가능
#print(selecter)

selecter = bs.select("div")
print(selecter)

#selecter = bs.find_all("div", {"class": "partner_box"})
#print(selecter)