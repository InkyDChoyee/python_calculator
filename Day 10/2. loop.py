# break
i = 0

while True:
    print("{}번째 반복입니다.".format(i))
    i += 1
    if i > 10:
        break        # 이 뒤로는 반복문을 탈출

sum_ = 0
while sum_ < 100:
    num = int(input("정수를 입력해주세요 (0 입력시 종료) > "))
    if num == 0:
        print("반복문이 종료되었습니다")
        break
    sum_ += num
    print("현재 정수의 합은 {}입니다".format(sum_))
else:
    print("반복문이 종료되었습니다")

# 이중 list break
numbers = [[1,2,3],[10,20,30]]
for i in numbers:
    print(i)
    for j in i:
        print(j)
        break

# continue
numbers = [10, 200, 30, 400, 50]

for i in numbers:
    if i < 200:
        continue
    print("{}은 200이상의 숫자입니다".format(i))