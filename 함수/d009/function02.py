#문자열 관련 내장 함수와 문자열 형 변환 함수
user_name = input("이름은? ")               #input을 하면 String타입이 됨.
user_age = input("나이는? ")
print(user_name + "님! 나이는 " + str(user_age) + "세군요!")            #str() 생략 가능.

say = "{}님! 나이는 {}세군요!"               #이 문장이 포맷이다. 중복 가능
print(say.format(user_name, user_age))
say = "{0}님! 나이는 {1}세군요! {1}세라니 놀라워요!"
print(say.format(user_name, user_age))
say = "{name}님! 나이는 {age}세군요! {age}세라니 놀라워요!"
print(say.format(name = user_name, age = user_age))

pi = "3.141592"
print("문자열 출력 :", pi)
print("실수 변환 출력 :", float(pi))        # '+'를 사용하면 숫자는 출력할 수 없다. ','는 상관없다.
print(float(pi) + 1000)
year = "2018"
print("올해 연도 :", year)
print("100년 뒤는", int(year)+100, "년입니다.")
print("숫자를 문자열로 변환하려면 str()을 이용합니다.")
print("올해는 " + str(year) + "년입니다.")

list = ['d', 'c', 'a', 'b']
list.reverse()
print("리스트 항목 순서 뒤집기", list)      #인덱스 뒤집기
list.sort()
print("리스트 항목 정렬하기", list)         #내용을 보고 내림차순
list.sort(reverse = True)
print("리스트 항목 역정렬하기", list)       #내용을 보고 오름차순
for index, value in enumerate(list) :
    print("인덱스", index, "위치의 값은", value)

# str = "나는 문자열이다."    #함수 str --> 문자열 str
#print(str)
n = 3
print(str(n))           #str이 함수였는데 문자열이 됨. 그래서 함수의 기능이 사라졌다.