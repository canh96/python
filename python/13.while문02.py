#while True:
 #   print(f'{num}')
  #  num += 1

while True:
    print('''처리 번호를 입력하세요.
    1..회원 입력
    2.회원검색
    4.회원삭제
    5.종료
    입력번호''', end="")

    num = int(input())

    if num == 1:
        print('회원정보입력')
    elif num == 2:
        print('회원 검색') 
    elif num == 3:
        print('회원 수정')
    elif num == 4:
        print('회원 삭제')
    else:
        print('종료')