import random

# def rolling_dice(pip) :
#     n = random.randint(1, pip)
#     print(pip, "면 주사위 굴린 결과 :", n)

# # rolling_dice()        Error Occurs.
# rolling_dice(4)
# rolling_dice(6)
# rolling_dice(8)
# rolling_dice(10)
# rolling_dice(12)
# rolling_dice(20)

def rolling_dice(pip, repeat) :
    for r in range(1, repeat+1):
        n = random.randint(1, pip)
        print(pip, "면 주사위 굴린 결과", r, ":", n)

# rolling_dice(2)       위에 정의했던 함수는 사라짐.
rolling_dice(6, 1)
rolling_dice(6, 2)
rolling_dice(12, 0)     #0번 돌리라 함.
rolling_dice(20, -3)    #-3번 돌리라 함.