#파일 입출력 2 -파일 읽기

f = open(file='./temp.txt', mode  ='r', encoding= 'utf-8')

#t = f.read()
while True:
    line = f.readline()
    if not line:
        break

    print(line)

f.close()
print('파일 읽기 완료')