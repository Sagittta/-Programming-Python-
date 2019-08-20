#p153

import repeater as re

s = input("반복할 문자를 입력하세요 : ")
a = input("구분할 문자를 입력하세요 : ")
n = input("반복할 횟수를 입력하세요 : ")

re.repeat(s, a, int(n))
re.repeat(s)
re.once(s)
