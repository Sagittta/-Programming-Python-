from drink import Drink

class BubbleTea(Drink):
    _pearls = ["타피오카펄", "코코펄", "젤리펄", "알로에펄"]

    def __init__(self, name, price):
        super().__init__(name, price)       #Drink의 생성자 가져옴
        self.pearl = 0

    def __str__(self):
        return super().__str__() + "\t펄: " + BubbleTea._pearls[self.pearl]

    def set_Pearl(self):
        self.pearl = input("펄을 선택하세요 (0: 타피오카펄, 1: 코코펄, 2: 젤리펄, 3: 알로에펄) : ")
        if self.pearl == "":
            self.pearl = 0
        else:
            self.pearl = int(self.pearl)

    def order(self):
        super().order()     #Drink의 order()함수
        self.set_Pearl()
