#문자열
bruce_eckel = 'life is short,\n\t you need Python'
print(bruce_eckel)

#여러줄 문자열
multi_line = '''life is short
you need python
and i need c# too.'''

#리스트(배열)
b = [1, 2, 3, 4]

print(b)

b.append(5)  #append는 맨마지막에 추가
print(b)

b.insert(3, 10) #insert는 원하는 위치에 추가  (위치, 넣고싶은 숫자)
print(b)

b.sort()   #순서대로 정렬 (오름차순)
print(b)

b.reverse()
print(b)  #역순으로 정렬 (내림차순)

print(type(b))


#튜플
c = (1, 2, 3, 4)
print(c)

# 튜플에서는 append()로 값 추가 불가


print([c])

# 딕셔너리 key : value쌍의 집합
spiderman =  {
    'name' : '피터 파커',
    'age' : 18,
    'weapon' : '웹슈터',
    'member0favengers' : True}

print(spiderman)
print(spiderman['name'])
print(spiderman) # [2] , .age  같은 것 안됨 ([key값]만 들어감) 