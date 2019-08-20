#시간 때우기
import time
time.sleep(0.1)         #0.1초 자자

#화면 지우기
import os
os.system('cls')

n = 0

while(True) :
    os.system('cls')
    print(" "*n+"0")
    n += 1
    time.sleep(1)       #1초 자자. ctrl+c 하면 종료.
    #경마장 게임만들기 가능.

# n = 0
# while(True) :
#     os.system('cls')
#     print(" "*n + "0")
#     n += 1
#     x = input()
#     if x == 'x' :
#         break

# n = 0
# os.system('cls')
# print("helloworld1" + str(n))
# n = input()
# os.system('cls')
# print("helloworld2" + str(n))
# n = input()
# os.system('cls')
# print("helloworld3" + str(n))
# n = input()
# os.system('cls')
# print("helloworld4" + str(n))
# n = input()

# n = 0
# os.system('cls')
# print("  "*n+"0")
# n+=1
# input()
# os.system('cls')
# print("  "*n+"0")
# n+=1
# input()
# os.system('cls')
# print("  "*n+"0")
# n+=1
# input()
# os.system('cls')
# print("  "*n+"0")
# n+=1
# input()
# os.system('cls')
# print("  "*n+"0")
# n+=1
# input()