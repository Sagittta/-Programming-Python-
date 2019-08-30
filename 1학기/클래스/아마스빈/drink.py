class Drink:
    _cups = ["레귤러", "점보"]      #리스트. 앞의 밑줄을 쓰는 이유는 밖에서 접근하면 안되는 정보이기 때문.
    _ices = ["0%", "50%", "100%", "150%"]
    _sugars = ["0%", "50%", "100%", "150%"]

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0                #기본값으로 초기화
        self.ice = 2
        self.sugar = 2
        #넣을 게 없으면 self.name = none 처럼 사용 가능

    def __str__(self):
        return "이름 : " + self.name + "\t가격 : " + str(self.price) + "원\t컵 사이즈 : " + Drink._cups[self.cup]\
            +"\t얼음량 : " + Drink._ices[self.ice] + "\t당도 : " + Drink._sugars[self.sugar]
                                                                            #클래스 변수 / 멤버변수는 __init__에서 초기화 해줘야 함 !!!

    def set_cup(self):
        self.cup = input("컵 사이즈를 선택하세요 (0: 레귤러, 1: 점보) : ")
        if self.cup == "":              #사용자가 엔터만 치면 기본값 0을 넣자
            self.cup = 0
        else:
            self.cup = int(self.cup)     #혹시 정수형으로 선택하지 않을 경우에 대비

        #점보 사이즈면 300원 추가
        if self.cup == 1:
            self.price += 300

    def set_ice(self):
        self.ice = input("얼음량을 선택하세요 (0: 0%, 1: 50%, 2: 100%, 3: 150%) : ")
        if self.ice == "":
            self.ice = 2
        else:
            self.ice = int(self.ice)

    def set_sugar(self):
        self.sugar = input("당도를 선택하세요 (0: 0%, 1: 50%, 2: 100%, 3: 150%) : ")
        if self.sugar == "":
            self.sugar = 2
        else:
            self.sugar = int(self.sugar)

    def order(self):
        #파이썬은 자신의 함수를 호출할 때에도 앞에 self.을 붙여야 함
        self.set_cup()
        self.set_ice()
        self.set_sugar()
