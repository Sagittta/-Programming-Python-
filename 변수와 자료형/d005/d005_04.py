set()
s = {}
print(type(s))
s = set()

game = {"LOL", "Overwatch", "Tetris", 1942, 2048}
print(game)
#중복이 불가능. 순서를 막 해줌.

print(set("Funny")) #글자 하나 가져오기 불가능.

print(set((2560, 1440))
      #tuple
set({"google":"google.com", 18:"unesco.org"})
      #dict
print(set(range(3)))

game.add("슈의 라면가게")

game.update(("Sudden Attack", "Battle Ground"))     #튜플 내용이 따로따로 들어감.
game.add(("Fifa", "NBA"))       #튜플 내용이 덩어리로 들어감.

print(len(game))

game.remove("Sudden Attack")
print(game)
