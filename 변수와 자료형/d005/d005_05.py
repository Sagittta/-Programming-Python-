s3 = {3, 6, 9, 12}
s4 = {4, 8, 12, 16}
print(s3 & s4)          #교집합
print(s3 | s4)          #합집합
print(s3.intersection(s4))      #교집합
print(s3.union(s4))             #합집합
print(s3 - s4)              #차집합
print(s4 - s3)
print(s3.difference(s4))
print(s3 ^ s4)      #XOR 대칭 차집합(교집합 빼고 나머지 다 출력)
print(s3.symmetric_difference(s4))
