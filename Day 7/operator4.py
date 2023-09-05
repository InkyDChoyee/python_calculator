# and

print(True and True)
print(True and False)
print(10>3 and 3<5)
print(10==1 and 1==5)

print("==============")

# or

print(True or False)
print(False or True)
print(False or False)

print("==============")

# 다른 사용법

#and
print("a" and 10>3 and True and False) # => 거짓으로 판별되는 가장 첫 번째 값이 반환됨
print("a" and 1 and True and "참") # => 모두 참인 경우 마지막 항의 결과값이 반환됨

#or
print(0 or 1 or False or "a") # => 참으로 판별되는 첫번째 값이 반환됨
print(0 or 0.0 or False or '') # => 모두 거짓인 경우 마지막 결과값이 반환됨

print("===============")

#and, or 연산자 우선순위
print(True or False and "참")
# and 연산자가 or 연산자보다 우선순위가 높다
# => False 와 "참" 부분을 먼저 처리하고 나온 값인 False 와 True를 나중에 처리한다

print((True or False)and "참")
# or 연사자를 먼저 처리하고 싶다면 괄호를 한번 더 사용

print("===============")


#not 연산자

print(not True)
print(not 10>3)
# => 결과값이 반대가 된다

print("===============")

# 연산자의 우선순위
print(3*2**2+1/2)