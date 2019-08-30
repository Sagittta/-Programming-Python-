#114p varg3.py

def p(space, space_num, *args):
#def p(*args, space, space_num):         #가변인수 *args는 맨 뒤에만 위치함.
    string = args[0]                    #string = "heart"
    for i in range(1, len(args)):
        string += (space * space_num) + args[i]     #string = "heart" + (","*3) + "음"
    print(string)

p(",", 3, "♡")                  #하트만 출력됨. range(1, 1)은 0으로 바로 string을 출력함.
p(",", 3, "♡", "♪")             #space가 ,/space_num이 3/ *args가 기호.[0] = 하트, [1] = 음표.
p(",", 3, "♡", "♪", "♣")
p(",", 3, "♡", "♪", "♣", "♠")

#115p 혼자해보기 개어려움.........

def star(word, *args):
    for a in args:
        print(word*a)

star("♬", 3)            #♬♬♬
star("♡", 1, 2, 3)      #♡  ♡♡  ♡♡♡

#116p 키워드 인자를 사용한 함수

def fn(a, b, c, d, e):
    print(a, b, c, d, e)

fn(1, 2, 3, 4, 5)
fn(10, 20, 30, 40, 50)
fn(5, 6, 7, 8, 9)
fn(a=1, b=2, c=3, d=4, e=5)     #12345
fn(e=5, d=4, c=3, b=2, a=1)     #12345
fn(1, 2, c=3, e=5, d=4)         #12345

#117p 

#fn(d=4, e=5, 1, 2, 3)          1을 c로 봐야 하는지, a로 봐야 하는지 애매해서 에러 발생함.

#117p

# def fn(a, b, c, *d):
#     print(a, b, c, d)

#  fn(c=3, b=2, a=1, 4, 5)       #error
#  fn(1, 2, c=3, 4, 5)             #error (c=3으로 쓰기 시작하면 뒤도 다 써줘야 함.)
# fn(4, 5, a=1, b=2, c=3)           #error (a가 중복.)