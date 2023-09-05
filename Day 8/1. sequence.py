# <시퀀스 자료형 *list>

a = 1
b = 2
c = 3
d = 4

print(a, b, c, d)

# list[] 안에 ','를 사용

# 모든 자료형 사용 가능
list_a = [a, b, c, d]
list_b = ["a", "b", "c"]
list_c = [True, False]
list_d = [1, "a", True]

print(list_a)
print(list_b)
print(list_c)
print(list_d)

# 인덱싱, 슬라이싱 사용 가능
numbers = [0,1,2,3,4,5,6,7]

print(numbers[0])
print(numbers[3:5])
print(numbers[1:])
print(numbers[-3:-1])

# 문자열
list_lan = ["JAVA", "C", "Python", "Go"]

print(list_lan[0][0]) # = 0번째 문자열에서 0번째 문자 반환
print(list_lan[2][2:4]) # 2번째 문자열에서 슬라이싱을 사용해 두번째 세번째 문자 반환

# 인덱싱
list_lan[1] = "C++" # = 문자열 변경도 가능
print(list_lan)

list_lan[1:3] = ["C#", "Python3"] # 리스트의 내용이 줄거나 늘어날 수 있음
print(list_lan)