#종류        형식           빈       셀 수 있냐          순서          변환함수            추정
#리스트    [값1, 값2]       []           O              O            list()            O
#튜플     (값1, 값2)        ()          O               O           tuple()            X
#딕셔너리  {키:값, 키:값}     {}          O               O           dict()             O
#셋       {값, 값}         set()        O              O            set()              O
#57p에 있숨둥


print(list(reversed(["Happy", "Birthday"])))        #reversed : 인덱스 순서를 뒤집음.(내용 x)

l = ['Happy', 'Birthday']
print(l)

l.sort()        #알파벳 순서로 정렬
print(l)

l.reverse()     #알파벳 역순으로 정렬
print(l)

print(list(reversed([456, 123,789])))
ln = [456, 123, 789]
print(ln)

ln.reverse()
print(ln)

ln.sort()
ln.reverse()        #sort => reverse : 내림차순

for i, value in enumerate(("funny", "Python")):
	print(i, value)         #인덱스 num + 값  => 튜플

for i, value in enumerate({"name":"봄이", "number":"4"}):
    print(i, value)         #인덱스 num + 키  => 딕셔너리