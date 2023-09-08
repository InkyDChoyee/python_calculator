# 오류 내기

# 예외
def division():
    try:
        num1 = input("첫번째 정수를 입력해주세요 > ")
        num2 = input("두번째 정수를 입력해주세요 > ")

        return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다")
    #except ValueError:
    #    print("숫자로 된 정수를 넣어주세요 !!")
    #except ZeroDivisionError:
    #    print("제발 !! 0을 입력하지 마세요!!")
    #except BaseException:             => 오류들에 대해 메세지 가능
    #except Exception as e:            as -> 오류 발생 원인을 볼 수 있다
    except Exception:
        print("오류가 발생했습니다")
    #else:           # 위쪽에 return이 있기때문에 else 구문 실행X
    finally:         # 오류가 발생하지 않아도 호출시키고 싶을 때 사용 = 무조건 실행
        print("정상적으로 나누기 함수가 호출 되었습니다")

division()

# help()         # 어떤 에러값을 상속받는지 보여줌
#help(ValueError)
#help(ZeroDivisionError)
#help(KeyboardInterrupt)

# valueError, ZeroDivisionError, keyboardInterrupt