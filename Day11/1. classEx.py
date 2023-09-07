# 클래스
class BreadMold:
    category = "크림빵"  # 클래스의 속성
    def make_bread(self):
        print("빵을 만들어 냅니다")

bread = BreadMold() # 클래스의 객체

bread.make_bread()  # def make_bread옆에 속성을 넣어줘야 출력 가능

# bread.price = 3000  # 새롭게 추가된 속성 = 객체의 고유한 속성이 된다

# bread_choco = BreadMold()
# bread_choco.category = "초코크림빵"  => 다른 객체 -> 가격X 

# 참조연산자 (ex = .format())
# print("{}의 가격은 {}입니다".format(bread.category, bread.price))


print(id)

number = 1
# 1 = 데이터 int 인스턴스(객체)
a = 1

# id() = 객체의 주소값을 반환해주는 함수
print(id(number))
print(id(a))
print(id(1))  # 이 셋의 주소가 같다 = 같은 객체이다

number = 1
a = 1.0

print(isinstance(number, int))
print(isinstance(a, int))

# 사실은
int("12345") # => 자료형 변환이 아니라 int 클래스의 새로운 객체를 만드는 것이었다
             # = 새로운 인스턴스를 만든 것

text1 = 12345
text2 = "12345"

print(id(text1), id(text2))
print(id(text1), id(int(text2))) # => text2의 주소값이 바뀜
                                 #     = 새로운 객체를 생성했다는 의미