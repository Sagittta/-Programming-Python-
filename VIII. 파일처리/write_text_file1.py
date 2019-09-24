# f = open("file.txt", "w")
f = open("file.txt", "a")

f.write("Hello")
f.write("\n")       # 이거 해줘야 줄바꿈이 됨.
f.write("World")

f.close()