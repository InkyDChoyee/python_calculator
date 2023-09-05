# if문
if True:
    print("실행할 문장입니다") # 앞부분의 공백 4칸을 꼭 사용해야한다

weather = "비"
if weather == "비":
    print("우산을 챙겨주세요")

study_time = int(input("오늘의 공부시간을 입력해주세요 >"))
# 만약에 오늘 공부할 시간이 3시간 이상이라면 파이썬 공부
if study_time >= 3:
    print("오늘은 파이썬 공부를 합시다 !")
# 만약에 오늘 공부할 시간이 3시간 미만이라면 오늘은 놀자
if study_time < 3:
    print("오늘은 시간이 별로 없으니까 놀자 !")
# 만약에 오늘 공부할 시간이 3시간 이상이고,
# 6시간 이하라면 파이썬 공부
if study_time >= 3 and study_time <= 6:
    print("오늘은 파이썬 공부를 합시다 !")
if 6>= study_time >= 3:  # 축약해서 이렇게 만들 수 있다
    print("오늘은 파이썬 공부를 합시다 !")

