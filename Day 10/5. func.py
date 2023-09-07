# 가변 매개변수

# def add(num1, num2 = 20, num3 = 30):
#     return num1 + num2 + num3
# print(add(num1 = 20, num3 = 2))

a, b = 20, 40

def add(num1=a, num2=b): # 함수가 정의되는 시점에서 변수들에 대한 평가를 한다
        return num1 + num2

a, b = 5, 10            # 이후에 변수들의 값이 바뀐다고 하더라도 결과값 영향X
        
print(add())  # 바뀐 값으로 출력을 하고 싶은 경우 => print(add(a, b))

# 예제
def add(*args):   # 가변 매개변수 = 앞에*를 붙임  // 일반 매개변수 앞에 올 수 없음
        sum = 0
        for i in args:
            sum += i
        print(sum)

add(10, 20, 30, 40)


# 키워드 매개변수

def star_player(**kwargs):
       for i in kwargs.items():   # .items()를 붙여줌
              print(i)  # tuple형태로 반환
        
star_player(축구 = "손흥민", 야구 = "박용택", 농구 = "허재")  # dictionary 형태로 값 전달

def func_a(name, *args, address = "한국", **kwargs):  # 순서를 바꾸게 되면 오류남
       print(name, args, address, kwargs)

func_a("홍길동", "옛날", "사람", address = "한양", 직업 = "도둑")
