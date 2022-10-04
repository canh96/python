#사람 객체를 위한 클래스 Person




class Person:
    __name = ''   #이름속성
    age = 0     #나이속성
    height = 100
    weight = 40
    speed = 60

    #생성자 제조기    (class person:을 하면 def __inint__해줘야 하지만 class person():을 하면 __init__을 안해도됌   ()이 __init__을 포함함)
    def __init__(self, name=None) -> None:   # ->은 return과 같다
        if name == None:
            self.__name = '강동현'
        else:
            self.__name = name

        print(f'{self.__name}탄생!!!')

    #매직메서드 __str__사용 재정의
    # def __str__(self) -> str:
    #     pass


    def  walk(self, speed,):
        print(f'{self.__name}이(가)  {speed}km/h로 걷습니다.')
        value = f'''객체{self.__name}\n
        나이 : {self.age}\n
        키 : {self.height}'''
        return value

    def run(self, speed):
        print(f'{self.__name}이(가 {speed}km/h로 뛴다')
        
p = Person('강동현')    #객체 생성
p.__name = '강동현'    # __name은 스페셜함 출력을 안시킴
p.age = 27
p.height =169
p.weight = 60

p.walk(2)
p.run(10)

print(type(p))

# p.age = 47

# print(p.__name)
# print(p.age)                     
