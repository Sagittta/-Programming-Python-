#수학 관련 내장함수 연습
print(10, "의 절댓값 :", abs(10))
print(-10, "의 절댓값 :", abs(-10))

print(128, "의 2진수 :", bin(128))     #0b가 앞에 붙음.
print(255, "의 2진수 :", bin(255))
print(7, "의 8진수 :", oct(7))         #0o가 앞에 붙음.    0o7 출력.
print(8, "의 8진수 :", oct(8))
print(15, "의 16진수 :", hex(15))      #0x가 앞에 붙음.    0xf 출력.
print(16, "의 16진수 :", hex(16))

numbers = [1, 5, -2, 0, 6]
print(numbers, "중 가장 큰 값은", max(numbers))
print(numbers, "중 가장 작은 값은", min(numbers))
print(numbers, "합계는", sum(numbers))
print("2의 10승은", pow(2, 10))        #1024

strings = ["고양이", "강아지", "토끼", "햄스터", "악어", "집가고 싶다"]
print(strings, "중 가장 큰 값은", max(strings))
print(strings, "중 가장 작은 값은", min(strings))
#print(strings, "합계는 ", sum(strings))    sum은 에러가 난다.
#print("강은서의 10승은 ", pow("강은서", 10))   pow는 에러가 난다.

pi = 3.141592
print(pi, "의 반올림은", round(pi))
print(pi, "의 소수점 0자리 반올림은", round(pi, 0))
print(pi, "의 소수점 1자리 반올림은", round(pi, 1))
print(pi, "의 소수점 2자리 반올림은", round(pi, 2))
print(pi, "의 소수점 3자리 반올림은", round(pi, 3))
print(pi, "의 소수점 4자리 반올림은", round(pi, 4))
print(5.5, "의 반올림은", round(5.5, 0))
print(-5.5, "의 반올림은", round(-5.5, 0))            #자바와는 다르게 -를 상관하지 않는다. -6 출력. (자바라면 -5가 출력됨.)