fi = open("history.ama", "r", encoding="utf8")

while True:
    data = fi.readline()

    if not data:
        break
    # print(data)
    # 한 줄 차이 나는 이유 : \n + print() 때문.
    print(data, end="")
    # 마지막이 "\n" 이라는 의미.
    
    # 한 줄 안에서 이름  가격  , ... 자르기
    # 총금액 계산하고, 출력하기

fi.close()

# print(data)