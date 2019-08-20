for i in range(2, 9+1) :        #2부터 9까지 i에 넣음
    print("2 x {} = {}".format(i, 2*i))

print("===")

for i in range(1, 9+1) :        #1부터 9까지 i에 넣음
    print("2 x {} = {}".format(i, 2*i))

print("===")

for i in range(2, 9+1) :        #2부터 9까지 i에 넣음
    for j in range(1, 9+1) :
        print("{} x {} = {}".format(i, j, i*j))
    print("=== ")