def gugudan(num):
    for i in range(1, 9+1):
        print(num, "X", i, "=", num*i)
    print("==--==--==--==")

gugudan(3)
gugudan(2)

def sum(*numbers):
    sum_value = 0
    for number in numbers:
        sum_value += number

    return sum_value

result = sum(1, 3)
print("1 + 3 =",result)
print("1 + 3 + 5 + 7 =",sum(1, 3, 5, 7))

print("==========")

def min(*numbers):
    min_value = numbers[0]
    for number in numbers:
        if min_value > number:
            min_value = number

    return min_value

print("min(1, 3) =", min(1, 3))
print("min(0, 3, -11) =", min(0, 3, -11))

print("===========")

def max(*numbers):
    max_value = numbers[0]
    for number in numbers:
        if max_value < number:
            max_value = number

    return max_value

print("max(1, 3) =", max(1, 3))
print("max(1, 3, 111) =", max(1, 3, 111))

print("===========")

def multi_num(multi, start, end):
    result=[]
    for n in range(start, end):
        if n%multi == 0:
            result.append(n)

    return result

print("multi_num(17, 1, 200) =", multi_num(17, 1, 200))
print("multi_num(3, 1, 100) =", multi_num(3, 1, 100))

print("=================")

def min_max(*args):
    min = args[0]
    max = args[0]
    for arg in args:
        if min > arg:
            min = arg
        if max < arg:
            max = arg

    return min, max

print("min_max(52, -3, 23, 89, -21) =", min_max(52, -3, 23, 89, -21))
mini, maxi = min_max(52, -3, 23, 89, -21)
print("최소값 :", mini, "최대값 :", maxi)

#절차지향 프로그래밍 장단점 vs 객체지향 프로그래밍 장단점
#생성자, 내부메소드