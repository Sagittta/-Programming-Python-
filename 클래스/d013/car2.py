class Car:
    count = 0                   #클래스 변수

    @classmethod
    def get_count(cls):         #클래스 함수
        return cls.count

    def __init__(self, type, speed):        #type과 speed만 넣으면 됨.
        self.type = type
        self.speed = speed
        Car.count += 1

    def move(self):
        print(self.type + "가 " + str(self.speed) + " 속도로 움직입니다.")

    def speed_up(self, amount):
        self.speed += amount

    def speed_down(self, amount):
        self.speed -= amount

print(Car.get_count())
c1 = Car("스포츠카", 100)
c2 = Car("트럭", 50)
c3 = Car("벤츠", 300)
print(Car.get_count())