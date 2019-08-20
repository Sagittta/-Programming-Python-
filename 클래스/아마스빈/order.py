from coffee import Coffee
from bubbletea import BubbleTea

class Order:
    _menus = [Coffee("아메리카노", 1800), BubbleTea("딸기요거트", 3500), BubbleTea("타로밀크티", 3500)]

    def __init__(self):
        self.order_menu = []
        self.order = None

    def show_menu(self):
        print("<Menu>\n0: 아메리카노 1800원, 1: 딸기요거트 3500원, 2: 타로밀크티 3500원")

    def sum_price(self):
        sum = 0
        for drink in self.order_menu:
            sum += drink.price

        return sum

    def order_drink(self):
        #반복
            #메뉴 보여주기
            #주문 받기 -> 음료 선택 -> 음료 객체 생성
            #옵션 선택 -> 컵 사이즈 얼음량 당도 펄
            #주문한 음료 리스트에 추가
        #주문한 음료 출력
        #금액 합계 출력
        while True:
            self.show_menu()
            self.order = input("음료를 선택하세요 : ")
            if self.order == "":
                break
            if int(self.order) == 0:
                drink = Coffee("아메리카노", 1800)
            elif int(self.order) == 1:
                drink = BubbleTea("딸기요거트", 3500)
            elif int(self.order) == 2:
                drink = BubbleTea("타로버블티", 3500)
#           drink = Order._menus[int(self.order)]
            drink.order()
            self.order_menu.append(drink)
            print("주문 음료 : ", drink, "\n")
        
        print("\n<Order List>")
        for drink in self.order_menu:
            print("주문 음료 : ", drink)
        print("\n총 금액 : ", self.sum_price(), "원")
