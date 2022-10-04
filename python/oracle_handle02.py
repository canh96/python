#오라클 db 연동
import cx_Oracle as ora

def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
#db연결객체
    conn = ora.connect(user = 'scott', password = 'tiger', dsn=dsn, encoding = 'utf-8')
    return conn

def test01(conn):
    cur = conn.cursor()
    query = 'SELECT *FROM emp '

    for row in cur.execute(query):
        print(row)

    cur.close()
    conn.close()



if __name__ == '__main__' :
    print('-----기본실행----')
    test01(myconn())


def test02(conn):
    cur = conn.cursor()
    query = 'SELECT *FROM emp '

    while True:
        row = cur.fetchone()
        if row is None: break
        print(row)

    cur.close()
    conn.close()

if __name__ == '__main__':
    print('---sql조회 기본 실행 ---')
    test01(myconn())
    print(' --- sql 조회 fetchone 사용 ---')
    test02(myconn())