#문자열 포맷팅
#a = "i'm so happy {0} you .". format('for')
#print(a)
name = '홍길동'
login_str = '{0}님 로그인중'.format(name)

print(login_str)

#print('{0}, {1}, {2}'.format('하나, 2, True'))
#print(f"{'하나'}, {2}, {True}")

#소수점 표현
PI = 3.141592
print('{0: 0.2f}'.format(PI))
print(f'{PI:0.2f}')    #위 와 아래 둘다 같은 식임 밑이 더 쉬움

full_name = 'Hugo MG Sung'
sp_names = full_name.split()  # 문자열은 ''로 잘라서 리스트로 만듦
print(sp_names)
print(sp_names[0])

greeting = 'hello, world'
words = full_name.split(',')  # 문자열은 ,로 잘라서 리스트로 만듦
print(words)

hi = '     hello~    '
print(hi.lstrip())              # ltrim()    공백 없애기   글을 왼쪽으로 정렬
print(hi.rstrip())              # rtrim
print(hi.strip())               # trim
#print(words[1].strip())

#문자열 특정 단어. 문자열 값 변경
print(full_name.replace('Hugo MG', 'Ashley'))    # replace(기존 값 , 바꿀 값)

#리스트 연산
arr = ['1',2, 3, '4', 5]    #리스트 안의 문자는 문자끼리 숫자는 숫자끼리 합칠 수 있음

print(arr[3])
print(arr[3] * arr[2])   # == 444      4라는 문자를 3 번 출력

print(arr[4] + arr[2])  #그냥 더하기 8
print(arr[3] + arr[0])  # '4'와 '1'을 합치기
print(arr[3] * arr[2])  # '4'글자를 3번 반복 출력

#이중 리스트
arr2 = [1, 2, 3.14, ['Hi', 'My', 'Friends']]
print(arr2[2])
print(arr2[3][1])   #My
print(arr2[3][1][0]) # M

arr3 = arr = arr2
print(arr3)