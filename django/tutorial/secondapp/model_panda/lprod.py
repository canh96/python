import pandas as pd
import cx_Oracle as ora

# 오라클 연결 및 접속하기
def getConnection() :
    # 오라클 연결하기
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    # 오라클 접속하기
    conn = ora.connect(user='busan_06', password='dbdb', dsn=dsn)
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
    
# 열이름 받아오기
def getColList(col, row):
    col_dict = {}
    
    for i in range(len(row)):
        col_dict[col[i].lower()] = row[i]
    
    return col_dict

# 여러건에 대한 리스트 + 딕셔너리 만드는 함수
def getDictType_FetchAll(col_name, row):
    list_row = []

    for tup in row:
        col_dict = {}
        
        for i in range(len(tup)):
            col_dict[col_name[i].lower()] = tup[i]
        
        list_row.append(col_dict)
    
    return list_row

# 전체조회(딕셔너리 형태로)
def getLprodList():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = ''' SELECT *
    FROM lprod '''
    
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    col_name = cursor.description
    col = []
    for i in col_name:
        col.append(i[0])
        
    row_list = getDictType_FetchAll(col, row)
    
    dbClose(cursor, conn)

    return row_list

# 주문내역 상세조회 - 1건 조회
def getLprod(gu):
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = ''' SELECT *
    FROM lprod
    WHERE lprod_gu = :lprod_gu '''
    
    cursor.execute(sql,
                   lprod_gu=gu)
    
    # 한건조회
    row = cursor.fetchone()
    
    col_name = cursor.description
    col = []
    for i in col_name:
        col.append(i[0])
    
    dict_row = getColList(col, row)
        
    dbClose(cursor, conn)
    
    return dict_row