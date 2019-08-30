#main_fruits.py

'''
from foods.fruits import orange, apple, watermelon
orange.eat()
apple.eat()
watermelon.eat()            #NoError
'''

from foods.fruits import *
orange.eat()
apple.eat()
watermelon.eat()            #NoError
# __init__.py 에서 __all__ 에 넣어주지 않으면 name 'apple' is not defined 라고 에러가 발생함.
# import * 에서 *은 __all__에 있는 것만 가져옴.