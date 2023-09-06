# 지역변수(Local Variable)

# def jeju_potato():
#     potato = "고구마"
#     print(potato)
#
# jeju_potato()


# 전역변수(Global Varialbe)

potato = "감자"  # 변수 선언

def jeju_potato():
    potato = "고구마"
    print(potato)  # 함수 내부에서 호출

print(potato)  # = 전역변수
jeju_potato()  # = 지역변수