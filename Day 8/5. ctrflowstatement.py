# input 함수
#text = input("성을 입력해주세요 >")
#text2 = input("이름을 입력해주세요 >")
#print(text + text2)

number = input("첫번째 정수를 입력해주세요  >") # 50
number2 = input("두번째 정수를 입력해주세요 >") # 30
print(number + number2) # str타입 => 5030 출력 = 문자열 형식
# => 자료형 변환을 해줘야 한다
print(int(number) + int(number2))
# => 처음부터 형 변환을 해주고 계산해도 된다
# number = int(input("첫번째 정수를 입력해주세요  >"))
# number2 = int(input("두번째 정수를 입력해주세요 >"))
# print(number + number2)