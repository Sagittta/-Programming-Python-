array = []
for i in range(1, 10, 2) :  #1~10 중 2씩 수를 출력
    array.append(i)
print(array)

array2 = [i for i in range(1, 10, 2)]
print(array2)

array3 = [i*i for i in range(1, 10, 2)]
print(array3)

array4 = [i*i for i in range(1, 10, 2) if i*i > 30]
print(array4)

array5 = []         #array4 == array5
for i in range(1, 10, 2) :
    if i*i > 30 :
        array5.append(i*i)
print(array5)