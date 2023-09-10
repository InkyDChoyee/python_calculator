def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2 

def divid(num1, num2):
    if num2 == 0:
        print("0으로 나눌 수 없습니다")
        return
    else:
        return num1 / num2
    
while True: 
    print("어떤 계산을 할까요?")
    print("1. 더하기, 2. 빼기, 3. 곱하기, 4. 나누기, 5. 종료")
    
    cal = input("번호를 입력해주세요 > ")

    if cal == '5':
            print("종료합니다")
            break
    
    if cal in ('1', '2', '3', '4', '5'):
        num1 = float(input("첫 번째 숫자를 입력하세요 > "))
        num2 = float(input("두 번째 숫자를 입력하세요 > "))
        
        if cal == '1':
            print("답 = ", add(num1, num2))
        elif cal == '2':
            print("답 = ", sub(num1, num2))
        elif cal == '3':
            print("답 = ", multi(num1, num2))
        elif cal == '4':
            print("답 = ", divid(num1, num2))
        
    else:
        print("1, 2, 3, 4, 5 번 중에서 선택해주세요!")