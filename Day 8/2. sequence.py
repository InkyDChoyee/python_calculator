# list []  tuple ()
numbers = (1, 2, 3, 4)  # 소괄호 생략 가능
print(type(numbers))    # 주의 *tuple 안에 요소가 하나뿐이라면
                        #       마지막에 반드시 ','를 넣어줘야 한다
number1 = (1)
number2 = (1,)
print(type(number1))
print(type(number2))

numbers = (1,2,3)
print(3 * numbers)
print(numbers + numbers)
# append, extend, insert 사용불가

numbers = (1,2,3,(4,5,6,))
print(numbers)
print(numbers.index(3))

# 언팩킹
numbers = (1,2,3)

number1 = numbers[0]
number2 = numbers[1]
number3 = numbers[2] # 언팩킹을 사용하여 간단하게 줄이기 가능
print(number1,number2,number3)

number1, number2, number3 = numbers # 한줄로 줄이기 가능
print(number1, number2, number3)

numbers = 1, 2, 3, 4, 5, 6
number1, number2, *number3 = numbers  # *을 사용하여 나머지 묶음
print(number1, number2, number3)

# tuple에 요소를 추가할 수는 없지만
# 요소를 추가한 것 처럼 보이게 할 수는 있다
numbers = 1, 2, 3, 4
print(id(numbers))

numbers += 5, 6,
print(id(numbers))
# 메모리의 주소값을 확인해보면 서로 다른것을 알 수 있다