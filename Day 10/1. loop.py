# for문
for i in range(1, 10+1):
    print(i)

for i in "일이삼사오":
    print(i)

fruits = ["사과","딸기","바나나"]
for i in fruits:
    print("과일 바구니에 {}가 들어있습니다".format(i))

# 1부터 30가지의 수 중에서 3의 배수들의 합을 구하시오.
# 3의 배수 구하기
# 짝수 % 2 == 0
# / 2 == 2의 배수와 같다
sum =0

for i in range(1, 30+1):
    if i % 3 == 0:
        print("{} + {} = ".format(sum, i), end = "")
        sum += i
print(sum)

# if문을 사용하지 않고 동일한 결과값 얻기
for i in range(3, 30+1, 3): # step 사용하기
    print("{} + {} = ".format(sum, i), end = "")
    sum += i
print(sum)
