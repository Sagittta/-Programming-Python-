#행복한 프로그래밍
print("Hello World")
5+11
5*11
["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
#결과를 보이기 위해선 앞에 print를 써야 함

print(5+11)
print(5*11)
print(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"])
print("5",11)
print("5"+"11")

#Traceback (most recent call last):
#  File "D:/미림 2학년/학교활동 O/PYTHON/d001.py", line 7, in <module>
#    print("5"+11)
#TypeError: can only concatenate str (not "int") to str
# 무슨 파일에서 무슨 줄에 에러가 났다. 정수형이 아닌 자료형은 계산할 수 없다.

print("박성래 선생님"+"사랑해요")
print("박성래 선생님","사랑해요")
# +는 띄어쓰기가 안 된다.
# ,는 자동으로 띄어쓰기가 된다.

print("5"*11)
print("Hello World"*5)
#문자열을 곱한 수만큼 출력
