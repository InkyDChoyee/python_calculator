domain = input("웹 사이트 주소를 입력해주세요 > ")
nation = domain.split(".")

# kr = 한국, uk = 영국, com = 기업, org = 기관, 알 수 없음
# 가장 뒤쪽의 요소를 [-1]

if nation[-1] == "kr":
    print("한국")
elif nation[-1] == "uk":
    print("영국")
elif nation[-1] == "com":
    print("기업")
elif nation[-1] == "org":
    print("기관")
else:
    print("알 수 없음")