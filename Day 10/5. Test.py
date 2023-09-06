# 최대, 최소값을 구학

def max_min_search(*number):
    max_num = number[0]
    min_num = number[0]
    for num in number:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num, min_num
print(max_min_search(15, 30, 4, 60, 7, 80, 32)) # tuple형태로 자료 전달

# 간단하게 만들기
def max_min_search(*number):
    return max(number), min(number)
print(max_min_search(15, 30, 4, 60, 7, 80, 32))