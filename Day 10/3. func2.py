# 끝말잇기 함수 만들기
def game(text):
    while True:
        print(text)
        keyword = input("끝말을 이어주세요 > ")
        if text[-1] == keyword[0]:
            text = keyword
        else:
            print("끝말이 이어지지 않았습니다")
            break

game("함수호출")