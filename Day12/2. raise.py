# 사용자가 직접 예외를 발생시키는 방법
# raise 구문

# 화장실이 너무 급한 남자

class Toilet:
    def __init__(self):
        self.using = False
    
    def in_use(self):
        if self.using == False:
            print("화장실을 사용합니다!")
            self.using = True
        else:
            raise Exception("안에 사람이 있어요!! 잠시 기다려주세요!!")  # 오류에 대한 지정
    
    def not_in_use(self):
        self.using = False
        print("안에 사람이 없습니다!")

man = Toilet()

while True:
    use = input("화장실을 사용하시겠습니까?(y/n)")
    try:
        if use == "y":
            man.in_use()
        else:
            man.not_in_use()
    except Exception as e:  # 오류에 대한 처리
        print(e)