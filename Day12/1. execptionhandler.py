# 구문 오류
print ("구문 오류 내기")
# 텍스트 에디터가 구문오류가 있다고 알려준다

# 예외
#def division():
#    num1 = int(input("첫번째 정수를 입력해주세요 > "))
#    num2 = int(input("두번째 정수를 입력해주세요 > "))
    # 정수 이외를 입력하면 Error가 발생

#    return print(f"{num1}을 {num2}로 나눈 값은 {num1/num2}입니다")

#division()

#def division():
#    num1 = (input("첫번째 정수를 입력해주세요 > "))
#    if num1.isdigit():
#        num2 = (input("두번째 정수를 입력해주세요 > "))
#        if num2.isdigit() and num2 !="0":
#            return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다")
#        else:
#            print("숫자로 된 정수를 입력하세요")
#    else:
#        print("숫자로 된 정수를 입력하세요")
#division()

# 예외처리 - try, except 코드
def division(): 
    try:
        num1 = (input("첫번째 정수를 입력해주세요 > "))
        num2 = (input("두번째 정수를 입력해주세요 > "))

        return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다")
    except:
        print("0이 아닌 숫자로 된 정수를 입력해주세요!!")

division()