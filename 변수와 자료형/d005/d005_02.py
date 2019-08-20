x = 2560    #=(Swap)=> x = 1440
y = 1440    #=(Swap)=> y = 2560
x, y = y, x
print(x)
print(y)
x, y = "정윤", "가연"
print(x)
print(y)

a = (123, "abc", True, 123)
print(a)
print(a[1])
print(a[2:])        #slicing
print(a[:2])
#a[1] = 2       튜플은 수정 불가능
print(a.index("abc"))       #abc의 인덱스 알려줌
a.count(123)    #123이 몇 개냐


#튜플 연습 ~
