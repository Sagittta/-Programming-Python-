table = [
    ["월", "화", "수"],
    [1, 2, 3]
]

for row in table:       #첫 번째 row는 월화수 list, 두 번쨰 row는 123 list
    for col in row:
        print(col)
    print("======")