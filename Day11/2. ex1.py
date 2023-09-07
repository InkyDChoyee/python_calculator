# 상속
# super, 부모 = 상위 클래스
# sub, 자식 = 하위 클래스

class ParentRestaurant:
    price = 15000

    def __init__(self, name, menu, recipe):
        self.name = name
        self.menu = menu
        self.recipe = recipe
    
    def __str__(self):
        return "가게이름 : {}, 가게의 메뉴 : {}, 메뉴의 조리법 : {}".format(self.name, self.menu, self.recipe)
    
    def __del__(self):
        pass

class ChildRestaurant(ParentRestaurant):  # 인자로 부모클래스의 이름을 넣어준다
    price = 20000
    
    def __init__(self, name, menu, recipe, marketing):
        ParentRestaurant.__init__(self, name, menu, recipe)
        self.marketing = marketing

    def __str__(self):
        return super().__str__() + "마케팅 방법 : {}".format(self.marketing)  # 상위클래스 참조 함수

restaurant_info = ChildRestaurant("자식의 가게", "붕어빵", "붕어빵을 굽는다", "온라인")
print(restaurant_info)

print(issubclass(ChildRestaurant, ParentRestaurant))
print(issubclass(ParentRestaurant, ChildRestaurant))