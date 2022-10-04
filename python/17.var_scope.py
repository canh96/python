#지역변수
a=1                     
print(a)

def vartest(a):
    print(a)
    a = a+ 10
    return a

a = vartest(3)
print(a)

#전역 변수
a=1                     
print(a)

def vartest():
    global a   #전역 변수  (쓰려면 지역 파라미터를 없애야 함)
    print(a)
    a = a+ 10
    return a

a = vartest()
print(a)

#람다 함수  = 코드를 간결하게 한줄로 만들어주는 함수

def addd(x, y):
    return x + y

