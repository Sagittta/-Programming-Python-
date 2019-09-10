# 버스 여유, 보통, 혼잡
# 탑승객, 하차객 입력 받자
# 0 이상 10 미만 : 여유
# 10 이상 20 미만 : 보통
# 20 이상 : 혼잡

sum = 0

while True:
    in_person = int(input("탑승객 수는? (-1: 끝) "))
    if in_person == -1:
        break
    out_person = int(input("하차객 수는? "))
    sum += in_person - out_person

print("버스에 있는 사람 수는", sum, "명\n")

if sum < 0:
    print("오류 발생")
elif 0 <= sum < 10:
    print("여유")
elif 10 <= sum < 20:
    print("보통")
else:
    print("혼잡")