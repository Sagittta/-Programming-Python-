'''
x = int(input("숫자 입력 ~\n"))

if x % 2 == 0:
    print("짝수")
else:
    print("홀수")


password = input("암호 입력 ㄱㄱ \n")

if password == "암호":
    print("암호이다.")
else:
    print("암호가 아니다.")


x = int(input("숫자 입력 ㄱ ~ \n"))

if x % 4 == 0:
    print("4의 배수")
elif x % 3 == 0:
    print("3의 배수")
elif x % 2 == 0:
    print("2의 배수")
else:
    print("다른 고 입력해봥 ~")


x = int(input("숫자 입력 ㄲ \n"))

if 10 <= x < 20:
    print("10대")
elif 20 <= x < 30:
    print("20대")
elif 30 <= x < 40:
    print("30대")
else:
    print("10대, 20대, 30대가 아니네요 ^^ 늙어땅")


x = int(input("ㄱ \n"))

if x > 10 and x % 2 == 0:
    print("10 초과 짝수")
#if x > 10 && x % 2 == 0            => error.
'''

x = int(input("ㄱ \n"))
if x > 10:
    if x % 2 == 0:
        print("10 초과 짝수")
    else:
        print("10 초과 홀수")
else:
    print("10 이하")