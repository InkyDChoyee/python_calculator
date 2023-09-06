# 사용자 정의함수
# 정의
def menu():
    print("오늘의 메뉴")
    print("오늘 점심메뉴는 제육볶음입니다")
    print("내일의 메뉴")
    print("내일의 점심메뉴는 돈까스입니다")
# 호출
menu()

# 파이썬 내장함수
print("사용할 데이터")
input("데이터")

# 매개변수
def add(num1, num2):   # num1, num2 = 매개변수
    print(num1 + num2) # = 함수정의

add(1, 2)  # 함수호출 -> 인자(1, 2)들이 매개변수로 전달되어진다
# 주의할 점 = 함수를 호출 할 때에는 인자의 개수와
#             매개변수의 개수가 같아야 한다

def add(text1, text2):
    '''문자열  두개(성, 이름)을 입력받아서 합쳐서 출력
    args
        text1 : 성을 받는 문자열
        text2 : 이름을 받는 문자열
    '''  # 독스트린 = 메모
    print(text1 + text2)

(add("홍","길동"))

# return
def add(text1, text2):
    text = text1 + text2  # 2. 전달 받은 매개변수들이 합쳐짐
    return text  # 3. 합쳐진 데이터를 return = 함수 호출 지점으로 반환

print(add("홍","길동"))  # 1. 함수를 호출할 때 인자들이 매개변수에 전달
                         # 4. 반환받은 값을 출력