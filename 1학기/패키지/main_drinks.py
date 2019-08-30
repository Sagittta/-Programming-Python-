# import + (함수, 모듈)
# import 할 때에는 폴더에서 끝나면 안되고 모듈 또는 모듈 안에 있는 함수로 끝나야 함.
# from은 폴더로 끝나도 됨
'''
from : 폴더 or 모듈
import : 모듈 or 함수
import에 사용한 것은 무조건 다 나와야 함 !!!
'''

# from foods.drinks.milk import drink
# drink()                           #NoError
# from 디렉토리.디렉토리.모듈 import 함수

# from foods.drinks import milk
# milk.drink()                      #NoError
# from 디렉토리.디렉토리 import 파일

# import foods.drinks.milk
# foods.drinks.milk.drink()         #NoError
'''
===================================================
'''
# import foods.drinks
# foods.drinks.milk.drink()         #Error

# import foods
# foods.drinks.milk.drink()         #Error

# foods.drinks.milk.drink()         #Error


from foods.drinks import milk as m
m.drink()