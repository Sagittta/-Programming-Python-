#main.py
from order import Order
from file_manager import FileManager

# 주문 내역 불러오고, 보여주자
# answer = input("주문 내역을 볼까요? (y/n) : ")
file_manager = FileManager("history.bin")       # __init__
# if answer == "y":
history = []
try:
    history = file_manager.load()                   # load()
    sum = 0
    for h in history:
        print(h)        # 리스트에서 하나씩 뽑아서 프린트
        sum += h.price
    print("여태까지 내가 아마스빈에 쏟아부은 돈 : " + str(sum) + "원")
except FileNotFoundError:
    print("주문 내역이 없습니다.")

o = Order()
o.order_drink()

# 주문 내역 저장하자
file_manager.save(history + o.order_menu)
