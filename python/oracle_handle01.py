#오라클 db연동         #다시 공부하기 구글링하기
import cx_Oracle 
#데이터 소스 네임 객체 생성(접속주소, 포트번호, 서비스명)
dsn = cx_Oracle.makedsn('localhost', 1521, service_name = 'orcl')
#db연결객체
conn = cx_Oracle.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')

cur = conn.cursor() #커서생성
query = 'SELECT * FROM memberTBL'
for row in cur.execute(query):
    print(row)

cur.close()
conn.close()
