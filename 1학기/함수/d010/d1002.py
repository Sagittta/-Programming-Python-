# input("현재의 input() 함수는 사용자 정의 함수입니다.")          #이것이 있을 때는 input 해줌.
def input(s) :      #정의(내장함수의 기능을 잃어버리고 내가 정의한 함수로 사용됨. 추천 X)
    print(s)

input("현재의 input() 함수는 사용자 정의 함수입니다.")          #이것만 있을 때는 기다리지 않아.

import random

n = random.randint(1, 6)           # 1 <= x <= 6. 리턴 뒤의 수 포함 O.
print("결과 : ", n)
n = random.randint(1, 6)           # 1 <= x <= 6. 리턴 뒤의 수 포함 O.
print("결과 : ", n)
n = random.randint(1, 6)           # 1 <= x <= 6. 리턴 뒤의 수 포함 O.
# n = random.randrange(1, 6+1)        # 1 <= x < 6+1. 뒤의 수 포함 x
print("결과 : ", n)

def rolling_dice() :
    n = random.randint(1, 6)
    print("6면 주사위 굴린 결과 : ", n)
rolling_dice()
rolling_dice()

#star
def star() :
    print("*****")
star()
star()
star()