str_slice = "0123456789"

print(str_slice[0:7]) # = 0123456
print(str_slice[0:]) # 마지막인덱스를 명시하지 않으면 끝까지 출력
print(str_slice[:10]) # 앞부분의 인덱스를 명시하지 않으면 제일 처음까지 출력
print(str_slice[:]) # 앞과 뒤를 정하지 않으면 제일 처음과 제일 끝가지 모두 출력

print(str_slice[-8:-1])

print("==================")

str_slice = "Python is easy" # 0 - 13

print(str_slice[:])
print(str_slice[-14:0]) # [-1:-14] => 문자열을 잘못 지정해주면 아무것도 출력되지 않음

print("===============")

#step

str_slice = "0123456789"

print(str_slice[0:10:2]) # 앞에서 부터 2개씩 뛰어서
print(str_slice[::-3]) # 뒤에서부터 3개씩 뛰어서
