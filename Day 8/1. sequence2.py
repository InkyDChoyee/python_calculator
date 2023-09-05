# *list 메서드 - 요소 추가

list_lang = ["JAVA","C","Python","Go"]
print(len(list_lang)) # 리스트 요소의 개수 값을 반환

# append() = 리스트 맨 뒤 마지막 인덱스(-1)에 새로운 요소 추가
list_lang.append("Ruby")
print(list_lang)

list_a = [1,2,3,]
list_lang.append(list_a)
print(list_lang) # list 안에 list 자체가 요소로써 추가됨

# extend() = list 안에 list가 아닌 요소자체가 추가됨
list_lang.extend("JavaScript")
print(list_lang)

# insert(index, data)
list_lang.insert(0,"R")
print(list_lang)