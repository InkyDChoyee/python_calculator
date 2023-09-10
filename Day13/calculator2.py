class Calculator2:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def sub(self, num):
        self.result -= num

    def multi(self, num):
        self.result *= num 

    def divid(self, num):
        if num == 0:
            print("0으로 나눌 수 없습니다")
        else:
            self.result /= num

    def __str__(self):
        return str(self.result)
    
Cal = Calculator2()

