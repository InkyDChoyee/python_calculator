fruits = ["사과", "키위", "바나나", "사과", "바나나", "망고"]
print(fruits)
fruit = input("빼낼 과일을 입력해주세요 > ")

while fruit in fruits:
    fruits.remove(fruit)

print(fruits)
print("{}를 모두 제거했습니다".format(fruit))