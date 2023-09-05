# 집합

# add
week = {"월요일","화요일","수요일","목요일","금요일","토요일","일요일","월요일"}
week.add("화요일")
week.add(("일주일",))
print(week)
#  123, "문자", True, ("튜플") = 추가 가능
# [1,2,3], {keys:value} = 추가 불가능
# 주의 = 요소에 0, 1이 포함되어 있을 때는 True, False 사용 불가

# update
# 튜플형태의 문자열에서 요소만 추가됨
# list나 dictionary 형태도 추가 가능
week.update(("일주일",))
week.update(["일주일"],{"한달":123}) # dictionary 형태를 추가할 때는 키만 추가됨, 값 추가X
print(week)