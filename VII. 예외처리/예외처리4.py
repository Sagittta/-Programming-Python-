# p217

l = [1, 2, 3]

try:
    print(1[1])
    print(1[2])
    # print(1[4])       # IndexError: list index out of range
except IndexError as e:
    print("인덱스 에러")
    print(e)
else:
    print("성공적으로 모든 코드를 실행")