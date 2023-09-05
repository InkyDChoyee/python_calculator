# <dictionary>
people = {
    "name" : "김개똥",        # 키 : 값
    "phone" : "010-1234-5678"
}
print(people["name"])  # dictionary에 접근할 때는 index를 사용하지 않고
print(people["phone"]) # 키를 사용하여 값에 접근한다

books = {"Daniel Pink":["파는것이 인간이다", "언제할 것 인가"],
         "Eric Schmidt" : "새로운 디지털 시대"
}
print(books["Daniel Pink"])
# 주의 0과False, 1과True는 같은 값으로 인식되기 때문에
# 같이 사용하는 것을 피해야 한다

coffee = {"JAVA":2500, "Americano":2500, "Latte":3000}
coffee["JAVA"] = 3000 # 키값을 이용하여 변경
print(coffee["JAVA"])
coffee["Moca"] = 2800 # 키값을 이용하여 추가
print(coffee["Moca"])
del coffee["Latte"] # 키값을 이용하여 삭제
print(coffee)

# dictionary 메서드
coffee = {"Java": 2500, "Americano" : 2000, "Latte" : 3000}
coffee["Moca"] = 3000
print(coffee.get("Moca"))
print(coffee.keys())
print(coffee.values())
print(coffee.items())