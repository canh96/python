from tkinter import N


def multi(a, b):
    res = a * b
    return res

def divide(a, b):
    res = 0
   

    try:
        res = a / b
    except Exception as e:       ### 정말 중요함  예외 발생은 Exception으로 통일해서 예외 처리하면됌
        print(f'예외발생 {e}')
    finally:
        return res


value = 7
print('곱셈/ 나눗셈')
print(divide(6, 0))
print(multi(6, 6))


print(multi(6, 6))
print('종료')
