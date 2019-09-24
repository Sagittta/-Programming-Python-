# p219
class MyError(Exception):
    pass


class OddError(Exception):
    def __init__(self, message="홀수는 ㄴㄴ"):
        self.message = message

    def __str__(self):
        return self.message


n = 11
'''
if n % 2 != 0:
    # raise : 에러 발생 예약어
    raise OddError
else:
    print(n, ", n / 2 =", n / 2)
    
이렇게 하면 OddError 에서 사용한 message 가 자동으로 출력됨.
'''

try:
    if n % 2 != 0:
        # raise : 에러 발생 예약어
        raise OddError
    else:
        print(n, ", n / 2 =", n / 2)
except OddError as e:
    print("에러 발생", e)
