# list 메서드 - 정렬

# 숫자, 알파벳, 한글 모두 가능
numbers = [101, 50, 260, 100, 20000, 3450]

# sort = 오름차순으로 정렬
numbers.sort() 
print(numbers)

# reverse = 순서를 반대로 정렬
numbers.reverse()
print(numbers)

# ooo.sort(reverse = True) = 내림차순으로 정렬
numbers.sort(reverse = True)
print(numbers)

names1 = ["bananan","apple","carrot"]
names2 = ["세종대왕","충무공 이순신","율곡 이이", "퇴계 이황"]
names1.sort()
names2.sort()
print(names1, names2)
