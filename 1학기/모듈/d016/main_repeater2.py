#p153

from repeater import repeat, once

s = input("반복할 문자를 입력하세요 : ")
a = input("구분할 문자를 입력하세요 : ")
n = input("반복할 횟수를 입력하세요 : ")

repeat(s, a, int(n))
repeat(s)
once(s)
