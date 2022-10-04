from django.http import HttpResponse
import pandas as pd
import cx_Oracle as ora

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

# 주문내역 상세조회 - 1건 조회
def getCart(no, prod):
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = ''' SELECT *
    FROM cart
    WHERE cart_no = :cart_no
    AND cart_prod = :cart_prod '''
    
    cursor.execute(sql,
                   cart_no=no,
                   cart_prod=prod)
    
    # 한건조회
    row = cursor.fetchone()
    
    col_name = cursor.description
    col = []
    for i in col_name:
        col.append(i[0])
    
    dict_row = getColList(col, row)
        
    dbClose(cursor, conn)
    
    return dict_row

# 주문내역 입력하기
def setCartInsert(id, prod, qty):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문번호 생성을 위한 sql문 작성
    sql = ''' SELECT DECODE(SUBSTR(MAX(cart_no), 1, 8),
                TO_CHAR(SYSDATE, 'YYYYMMDD'), MAX(cart_no)+1,
                TO_CHAR(SYSDATE, 'YYYYMMDD') || '00001') AS max_no
                FROM cart '''

    cursor.execute(sql)
    # 한건조회
    max_no = cursor.fetchone()
    no = max_no[0]
    
    # 주문내역 입력을 위한 sql문 작성
    sql = ''' INSERT INTO cart(cart_member, cart_no, cart_prod, cart_qty) 
                VALUES (:cart_member, :cart_no, :cart_prod, :cart_qty) '''
    cursor.execute(sql,
                   cart_member=id,
                   cart_no=no,
                   cart_prod=prod,
                   cart_qty=qty)

    conn.commit()
    
    dbClose(cursor, conn)
    
    return 'Y'

# 여러건에 대한 리스트 + 딕셔너리 만드는 함수
def getDictType_FetchAll(col_name, row):
    list_row = []

    for tup in row:
        col_dict = {}
        
        for i in range(len(tup)):
            col_dict[col_name[i].lower()] = tup[i]
        
        list_row.append(col_dict)
    
    return list_row

def getDictType_FetchOne(col_name, row_one):
    dict_row = {}
    
    for i in range(0, len(row_one), 1):
        dict_row[col_name[i].lower()] = row_one[i]
    
    return dict_row

# 전체조회(딕셔너리 형태로)
def getDictType_Cart():
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = ''' SELECT *
    FROM cart '''
    
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    col_name = cursor.description
    col = []
    for i in col_name:
        col.append(i[0])
        
    row_list = getDictType_FetchAll(col, row)
    
    dbClose(cursor, conn)

    return row_list

# 주문내역 삭제하기
def setCartDelete(no, prod):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문내역 입력을 위한 sql문 작성
    sql = ''' DELETE FROM cart
                WHERE cart_no = :cart_no
                AND cart_prod = :cart_prod '''
                
    cursor.execute(sql,
                   cart_no=no,
                   cart_prod=prod
                   )

    conn.commit()
    
    dbClose(cursor, conn)
    
    return 'Y'

# 주문내역 수정하기
def setCartUpdate(no, prod, qty):
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문내역 입력을 위한 sql문 작성
    sql = ''' UPDATE cart 
                SET cart_qty = :cart_qty
                WHERE cart_no = :cart_no
                AND cart_prod = :cart_prod '''
                
    cursor.execute(sql,
                   cart_no=no,
                   cart_prod=prod,
                   cart_qty=qty
                   )

    conn.commit()
    
    dbClose(cursor, conn)
    
    return 'Y'


    
   
