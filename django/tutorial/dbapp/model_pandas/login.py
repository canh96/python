from django.http import HttpResponse
import pandas as pd
import cx_Oracle as ora

from dbapp.model_pandas.cart import getDictType_FetchAll

# 오라클 연결 및 접속하기
def getConnection() :
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user='busan06', password='dbdb', dsn=dsn)
    return conn

# 커서 받기
def getCursor(conn):
    cursor = conn.cursor()
    return cursor

# 접속 정보 및 커서 반납하기
def dbClose(cursor, conn):
    cursor.close()
    conn.close()
    
# 카트 전체 리스트 조회
def getCartList():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = ''' SELECT *
    FROM cart '''
    
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    dbClose(cursor, conn)
    
    return row

# 열이름 받아오기
def getColList(col, row):
    col_dict = {}
    
    for i in range(len(row)):
        col_dict[col[i].lower()] = row[i]
    
    return col_dict

def getDictType_FetchOne(col_name, row_one):
    dict_row = {}
    
    for i in range(0, len(row_one), 1):
        dict_row[col_name[i].lower()] = row_one[i]
    
    return dict_row

# 주문내역 상세조회 - 1건 조회
def getLogin(id, pw):
    
    
    
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = ''' SELECT  mem_id, mem_pass, mem_name
    FROM member
    WHERE mem_id = :mem_id
    AND mem_pass = :mem_pass '''
    
    cursor.execute(sql,
                   mem_id = id,
                   mem_pass = pw)
    
    # row 값이 없는 경우:조회 결과가 없는 경우
    # 아이디 또는 패스워드가 틀린 경우 조회 결과 없음..
    # 조회결과 없으면 오류 발생
    row = cursor.fetchone()
    
    if row == None :
        dbClose(cursor,conn)
        return {'rs':'no'}
    
    
    col_name = cursor.description
    col = []
    for i in col_name:
        col.append(i[0])
    

    dict_row = getDictType_FetchOne(col, row)
    dict_row['rs'] = 'yes'
        
    dbClose(cursor, conn)
    
    return dict_row




    
   
