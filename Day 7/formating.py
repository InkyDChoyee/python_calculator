weather = "맑음"
temperature = 20

print("오늘의 날씨는", weather, "기온은", temperature, "도 입니다")
print("오늘의 날씨는 %s 기온은 %d 도 입니다"%(weather, temperature))
print("오늘의 날씨는 {} 기온은 {} 도 입니다".format(weather, temperature))

print("================")

# Percent Sign(%)

weather = "맑음"
temperature = 20
chance_shower = 33.5

print("오늘의 날씨는 %s 기온은 %d 도 비가 내일 확률은 %.1f%%입니다"%(weather, temperature, chance_shower))
# 서식하고자 하는 데이터 타입을 명확하게 모른다면 오류가 발생할 확률이 높아진다

# Format 함수

weather = "맑음"
temperature = 20
chance_shower = 33.5

print("오늘의 날씨는 {} 기온은 {}도 비가 내일 확률은 {}입니다" .format(weather, temperature, chance_shower))
# 자료형을 명확하게 명시해주지 않아도 그대로 요소들을 서식해와서 원하는 결과물이 나온다
# {}-> 안에 요소들의 순서를 지정해준다면 순서도 마음대로 바꿔서 출력시킬 수 있다
# {} 중괄호의 숫자가 요소보다 많다면 에러 발생
# {} 중괄호의 숫자가 요소보다 부족한 경우 -> 부족한 요소는 가져오지 않고 앞에서부터 가져온다

print("{:10},{:10}".format(weather, temperature))
# => 맑음        ,        20