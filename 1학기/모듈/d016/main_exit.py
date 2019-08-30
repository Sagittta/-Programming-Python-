#p152 main_exit.py

# import sys
from sys import exit

while True:
    print("종료하려면 exit를 입력하세요")
    user_input = input("> ")
    if user_input == "exit":
        # sys.exit()
        exit()