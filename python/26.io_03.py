#두 개의 값을 입력받아 두개의 변수에 나눠담기

x, y = input('두 단어를 입력하세요 >').split(': ')

# print(x,y) 와 print(x) , print(y)는 그냥 사용 불가 .split()을 붙여야함

print(int(x) * int(y))


# ====
# x, y, z = map(int(input('두 단어를 입력하세요 >').split(': ')))

# print(x * y)

