coffee = {"아메리카노" : 2500, "라떼" : 3000, "자바" : 2500}

for i in coffee.items():
# for i in coffee.keys():
# for i in coffee.values():
    print(i)

fruits = ["사과", "딸기", "바나나"]

for i in enumerate(fruits):
    print(i)
    print(f"{i[0]+1}번재 과일은 {i[1]}입니다")
for i,j in enumerate(fruits):
    print(f"{i+1}번재 과일은 {j}입니다")


# 중첩 for문
list_2nd = [[1,2,3,],["a","b","c"]]

for i in list_2nd:
    for j in i:
        print(j)

for i in range(1, 3):
    for j in range(1, 3):
        print("첫번째 for문의 반복{}번, 두번재 for문의 반복{}번".format(i, j))
        # 앞의 숫자 = i, 뒤의 숫자 = j 