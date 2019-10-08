fi = open("history.ama", "r", encoding="utf8")
sum = 0

while True:
    data = fi.readline()

    if not data:
        break
    # print(data)
    # 한 줄 차이 나는 이유 : \n + print() 때문.
    # print(data, end="")
    # 마지막이 "\n" 이라는 의미.
    
    # 자르기 (split 이 자동으로 list 에 넣어줌)
    l = data.split()        # white space : \t, \n, 띄어쓰기 있는 걸 다 자름.
    sum += int(l[1])        # 음료 가격 합계를 구함.

print("총 금액 :", sum, "원")
fi.close()

# print(data)
