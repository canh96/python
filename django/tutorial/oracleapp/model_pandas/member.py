import pandas as pd
import cx_Oracle as ora

# 오라클 연결 및 접속하기
def getConnection() :
    # 오라클 연결하기
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    # 오라클 접속하기
    conn = ora.connect(user='busan06', password='dbdb', dsn=dsn)
    return conn

# 커서 받기
def getCursor(conn):
    cursor = conn.cursor()
    return cursor

# 접속 정보 및 커서 반납하기
def dbClose(cursor, conn):
    # 커서 먼저 반납 먼저
    cursor.close()
    # 마지막에 접속정보 반납
    conn.close()
    
###### <실제 사용하는 함수> ######

# 회원 전체 리스트 조회
def getMemberList():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = ''' SELECT *
    FROM member '''
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    dbClose(cursor, conn)
    
    return row

# 한건 행에 대한 딕셔너리 만드는 함수
def getDictType_FetchOne(col_name, row_one):
    dict_row = {}
    
    for i in range(0, len(row_one), 1):
        dict_row[col_name[i].lower()] = row_one[i]
    
    return dict_row

# 회원 상세조회 - 1건 조회하기
def getMember(id):
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = ''' SELECT * 
    FROM member 
    WHERE mem_id = :mem_id '''
    cursor.execute(sql, mem_id=id)
    
    row = cursor.fetchone()
    
    # 컬럼명 조회하기
    colname = cursor.description
    col = []
    for i in colname:
        col.append(i[0])
    
    dict_row = getDictType_FetchOne(col, row)
    
    dbClose(cursor, conn)
    
    return dict_row

# 여러건에 대한 리스트 + 딕셔너리 만드는 함수
def getDictType_FetchAll(col_name, row):
    list_row = []

    for tup in row:
        col_dict = {}
        
        for i in range(len(tup)):
            col_dict[col_name[i].lower()] = tup[i]
        
        list_row.append(col_dict)
    
    return list_row

def getDictType_Member():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = ''' SELECT *
    FROM member '''
    
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    col_name = cursor.description
    col = []
    for i in col_name:
        col.append(i[0])
        
    row_list = getDictType_FetchAll(col, row)
    
    dbClose(cursor, conn)

    return row_list



# 전체조회(딕셔너리 형태로)
def getMemberListDict():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = ''' SELECT *
    FROM member '''
    
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    col_name = cursor.description
    col = []
    for i in col_name:
        col.append(i[0])
        
    row_list = getDictType_FetchAll(col, row)
    
    dbClose(cursor, conn)

    return row_list