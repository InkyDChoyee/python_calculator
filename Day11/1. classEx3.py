class BreadMold:
    category = "빵"
 
    def __init__(self,category, price):
        self.category = category
        self.price = price
        print("빵을 만들었습니다")

    #def __str__(self):
        # return "{}의 가격은 {}원 입니다".format(bread1.category, bread1.price
    

# __del__ 소멸자 메서드
    def __del__(self):
        print("빵이 없어졌습니다")

# __init__ 생성자 메서드
bread1 = BreadMold("붕어빵", 3000)
bread2 = BreadMold("잉어빵", 4000)
print("{}의 가격은 {}원 입니다".format(bread1.category, bread1.price))
print("{}의 가격은 {}원 입니다".format(bread2.category, bread2.price))

print(bread1)