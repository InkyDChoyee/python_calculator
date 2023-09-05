# ord, chr
print(ord("A"))
print(ord("a"))
print(ord("ㄱ"))
print(ord("ㅎ"))

print(chr(65))
print(chr(97))
print(chr(12593))
print(chr(12622))

# in연산자, not in 연산자
list_lang = ["JAVA", "C", "Python", "Go"]
numbers = [1,200,3,50,5,66,7,55,9]
print(50 in numbers)
print("C" not in list_lang)
print("JAVA script" not in list_lang, "JAVA script" in list_lang)

# 이차원 list
td_number = [[10,20,30],[1,2,3]]
print(td_number[1][2])
print(td_number[0][0:2]) # 슬라이싱