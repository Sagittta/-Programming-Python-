from datetime import datetime

print("현재 날짜 시각 객체 얻기")
today = datetime.now()
print("today = datetime.now()", today)

print("년 월 일 :", today.year, today.month, today.day)
print("시 분 초 :", today.hour, today.minute, today.second)
print("요일 :", today.weekday())
print()

print("특정 날짜 시각 객체 만들기")
day = datetime(2019, 1, 1, 0, 0, 0)
print("day = datetime(2019, 1, 1, 0, 0, 0) :", day)
print()

print("2019년부터 지나온 시간 구하기")
print("today - day :", today - day)
print()

# 태어난지 몇 일 되었는지
birth = datetime(2002, 12, 10, 12, 0, 0)
print("태어난 지 몇 일 됐는지? :", today - birth)

# 올해 크리스마스 몇 일 남았는지
xmas = datetime(2019, 12, 25, 0, 0, 0)
print("크리스마스 몇 일 남았는지? :", xmas - today)

# 내 생일이랑 몇 일 남았는지
birthday = datetime(2019, 12, 10, 12, 0, 0)
print("내 생일 몇 일 남았는지? :", birthday - today)
