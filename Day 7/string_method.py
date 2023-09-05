text = "www.GOOGLE.com"

# 내장함수 len
print(len(text)) # = 14

# 메서드 capitalize, upper, lower
txt_capitalize = text.capitalize() # 첫글자를 대문자로 변경
txt_upper = text.upper() # 문자열 전체를 대문자로 변경
txt_lower = text.lower() # 문자열 전체를 소문자로 변경

print(txt_capitalize)
print(txt_upper)
print(txt_lower)

print("==========================")

# 메서드 count, find, index
g_cnt = text.count('G')
g_find = text.find('G')
g_idx = text.index('G')

print(g_cnt)
print(g_find)
print(g_idx)

print("=============================")

# f_find = text.find('X')
# f_idx = text.index('X')

# print(f_find)
# print(f_idx)

# 메서드 replace
text_naver = text.replace("GOOGLE", "NAVER")
print(text_naver)

# 메서드 split
print(text.split('.'))
print(text.split('OO'))

# 메서드 strip
text1 = "      www.GOOGLE.com   "
print(text1)
stp = text1.strip()
print(stp)

text2 = "w w w . G O O G L E . c o m"
stp1 = text2.strip() #문자열 사이사이의 공백은 없애지 못한다
print(stp1)