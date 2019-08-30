t = ()
print(t)

xy = (2560, 1140)
print(xy)

color = 129, 247, 216       #팩킹
print(color)

print(xy + color)       #문자열처럼 할 수 있다.
print(xy * 2)

print(xy)       #실제로 변하지 않음

print(color[0])

red, green, blue = color    #언팩킹
print(red)
print(green)
print(blue)

x, y = xy
print(x)
print(y)

#x, y, z = xy
#Error 발생. 
