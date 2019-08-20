l = []
print(l)

player = ["Messi", 10, True]        #타입이 달라도 상관ㄴ
print(type(player))

print(list("Happy"))

print(list((1125, 2436)))

print(list({"menu":"gopchang","price":14900}))  #key : 값

print(list({"사과", "배", "망고", "딸기", "포기"}))      #set

nums = list(range(3))   #range함수 개중요 *** 0부터 3전까지의 정수를 리스트화함.
print(nums)

print(nums + [10, 11])  #하나의 리스트로 연결이 됨. nums가 바뀌지는 않음
print(nums)

nums += [10, 11]
print(nums)

nums.append(20)     #리스트 뒤에 추가
print(nums)

nums.append([30, 31])   #리스트가 한 항목 안에 들어감 like 이차원 배열. 리스트 항목은 총 7개
print(nums)

nums.insert(2, 40)      #삽입 위치를 지정(2), 삽입할 수를 지정(40). 대체되는 것이 아니라 뒤로 밀려남.
print(nums)

nums.extend([50, 51])   #list에서 빠져나와서 리스트에 추가됨. append와 다른 점에 주의
print(nums)

print(nums[0])
print(nums[2])
print(nums[7])          #리스트가 출력됨.

print(nums[7][1])       #리스트 7번째의 1번째 인덱스를 출력

nums[7] = 60            #리스트 변경
print(nums)

del nums[2]             #두 번째 '인덱스' 지워버림. 예약어에오
print(nums)

nums.remove(20)         #값으로 지워버린당.
print(nums)

#Stack : Last In First Out : LIFO
#Quew : First In First Out : FIFO
#스택이라면 51이 먼저 빠져나가고, 큐라면 0이 먼저 빠져나갈 것이당.
print(nums.pop())       #마지막 잘라내기(뽑아냄)
print(nums)

print(nums.pop(5))      #5번째 인덱스 잘라내기(뽑아내기)
print(nums)

nums.clear()        #nums의 요소를 다 지움.
print(nums)

#del nums        #아예 nums를 없애버림
print(nums)
print("==============")

nums = list(range(3))
print(nums)

nums += [10, 11]
print(nums)

print(nums[3])
print(3 in nums)
print(10 in nums)

print(len(nums))        #길이 세는 것

nums.sort()             #차례대로 정렬
print(nums)

nums.reverse()          #거꾸로 정렬
print(nums)
