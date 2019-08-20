def hello(msg="안녕하세요"):
    print(msg + "!")

hello("오랜만이에요")
hello("전은정")
hello()

print("--------")

def hello2(name="무명", msg="안녕하세요"):
    print(name,"님",msg,"!")

hello2("전은정", "오랜만이에요")
hello2()
hello2("엄하늘")
hello2(msg="오랜만이에요")

print("--------")

def hello3(name, msg="안녕하세요"):
    print(name,"님",msg,"!")

hello3("전은정", "오랜만이에요")
hello3("엄하늘")
#hello3()       에러 발생.

print("--------")

def fn1(a, b=[]):
    b.append(a)
    print(b)

fn1(3)          #[3]
fn1(5)          #[3, 5]
fn1(10)         #[3, 5, 10]
fn1(7, [1])     #[1, 7]     b에 값을 넣어주면 앞에 넣었던 값이 사라짐.