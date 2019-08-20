s = "name: {}, number: {}, soccer: {}"

print(s.format("Ronaldo", 7, True))

print("name: {name}, number: {num}".format(name = "Jordan", num = 23))

print("name: {0}, number: {1}, 등번호: {1}".format("손흥민", 7))
#number와 등번호에 7이라는 같은 값이 들어감. 만약 등번호: {0} 이라고 하면 등번호에 손흥민이라는 값이 들어감

print("name: {name}, number: {num}, 등번호: {num}".format(name = "손흥민", num = 7))
#중복 가능~

print("{:d}".format(515))

print("{:5d}".format(515))

print("{:+5d}".format(515))

print("{:=+5d}".format(515))

print("{:05d}".format(515))

print("{:+05d}".format(515))

print("{:f}".format(11.17))
print(11.17)

print("{:12f}".format(11.17))

print("{:12.1f}".format(11.17))

print("{:12.2f}".format(11.17))

print("{:12.3f}".format(11.17))
