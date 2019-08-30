for x in range(3, 9, 2) :       #3부터 9-1인 8까지 2씩 증가
    print(x)

print("=======")

for x in range(3, 9, 1) :
    print(x)

print("=======")

for ch in "LOVE" :              #문자열은 하나씩 뽑아서 출력
    print(ch)

print("=======")

for item in ["힙합", "발라드"] :    #리스트 하나씩 골라서 끝까지
    print(item + "즐겨듣는다.")

print("=======")

for item in (2560, 1440) :          #튜플은 하나씩 뽑아서 출력
    print(item)

print("=======")

pl = {"C":1972, "Java":1995, "Python":1991}     #딕셔너리는 키를 하나씩 뽑아서 출력
for key in pl :
    print(key, ":", pl[key])

for key, value in pl.items() :                  #pl.items()를 쓰면 키와 값 모두 가져올 수 있다.
    print(key, ":", value)
    
print("=======")

for item in {"HTML5", "CSS3", "JavaScript"} :       #set은 순서 상관 ㄴ
    print(item + "를 할 수 있다.")