h = "  Happy Programming! "

print(len(h))               #글자 수 세기

print(h.count("p"))         #h 문자열에서 인자 'p'의 개수 세기. 대소문자 구분O
print(h.count("og"))
print(h.count("ogzzzzzz"))

print(h.upper())            #모두 대문자로 변환

print(h.lower())            #모두 소문자로 변환

print(h.strip())            #왼쪽, 오른쪽 모두 공백 없애기. \t이어도 공백 없앰. 많이 사용!

print(h.replace("Happy", "Funny"))  #문자열 대체하기. Happy => Funny. 원래 h는 변하지 않음
print(h)

print(h.find("ap"))         #문자열에서 인자 'ap'를 왼쪽부터 찾기. 0-1-2-3으로 3에 a가 시작하므로 3이 출력됨

print(h.rfind("a"))         #문자열에서 인자 'a'를 오른쪽부터 찾기. 수는 왼쪽에서 셈.

print(h.find("zoo"))        #찾지 못하면 -1 리턴

print("===============")

print("a" in h)             #문자열에 a가 있는지 확인
print("amp" in h)           #문자열에 amp가 있는지 확인
x = "01::23::ab::&&"        
y = x.split("::")           #x문자열을 ::로 나누어 리스트 만들기
print(y)
", ".join(y)                #y 리스트를 ', '로 이어서 문자열 만들기
