# 이름, 나이정보 -> sample02.txt
# 이 파일을 이용 -> 미성년자 체크 프로그램 작성
# 프로그램 데이터 저장 -> 파일 객체 myfile2 생성
# 반복문 사용 -> split(',')함수 사용 -> 데이터 분리
# 2번째 열 정보 = 나이 의미 -> 19세 이상인지 아닌지 판단
# 결과 내용 -> / 사용 -> 문자열 결합
# 최종 결과 = myfile2객체에 저장 -> close() 함수 사용 -> 파일 종료

with open('C:/Users/user/Desktop/sample02.txt', 'r', encoding = 'utf-8') as file:
    lines = file.readlines()

with open('C:/Choyee/Programming/Python/python/Day13/myfile2.txt', 'w', encoding = 'utf-8') as myfile2:
    for line in lines:
        parts = line.strip().split(',')
        name = str(parts[0])
        age = int(parts[1])

        if age >= 19:
            myfile2.write(f"{name}/{age}/성인입니다\n")
        else:
            myfile2.write(f"{name}/{age}/미성년자입니다\n")

myfile2.close()

print("최종결과 = myfile2객체에 저장되었습니다")