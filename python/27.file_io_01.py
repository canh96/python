#파일 입출력1


f = open(file='C:/STUDY/StudyPython22/temp.txt', mode = 'w', encoding='utf-8')

f.write('안녕하세요\n')
f.write('저는 강동현입니다\n')
f.write('한국사람이죠\n')

f.close()  #필수
print('파일 생성 완료')