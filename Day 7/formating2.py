# 데이터 타입

weather = "맑음"
temperature = 20

print("{0:s},{1:d},{1:f},{1:o},{1:x}".format(weather, temperature))

# 정렬 방법 변경
left = "left"
right = "right"
middle = "midle"
# <>^ 사용
print("({2:>10s}),({1:^10s}),({0:<10s})".format(left,middle,right))
# 공백 10칸 지정 -> 공백에 채울 문자도 지정 가능
print("({2:!>10s}),({1:@^10s}),({0:#<10s})".format(left,middle,right))
# 문자열에서 지정해준 만큼만 출력 가능
print("({2:>10.4s}),({1:^10.3s}),({0:<10.2s})".format(left,middle,right))

print("====================================")


# f-string

weather = "맑음"
temperature = 20

print(f"오늘의 날씨는 {weather}이며, 기온은 {temperature}도 입니다")
print(f"2곱하기 30의 결과값 = {2*30}")
# 수식의 결과값도 포메팅 출력 가능