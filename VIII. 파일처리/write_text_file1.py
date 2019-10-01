# f = open("file.txt", "w")     # 덮어쓰기
f = open("file.txt", "a")       # 뒤에 이어서 쓰기

f.write("Hello")
f.write("\n")       # 이거 해줘야 줄바꿈이 됨.
f.write("World")

f.close()