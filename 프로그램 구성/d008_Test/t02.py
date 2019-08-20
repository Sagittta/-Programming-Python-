#N자리수의 각 자리 숫자 합 (for)

num = input("값을 입력해주세용 : ")
sum = 0

for i in range(0, len(num)) :
    sum += int(num[i])

print(sum)