# 일주일에 얼마나 일하는지
# 몇 주 일하는지
# 시급 얼마인지
# 총 15시간 이상이면 주휴수당 지급
# 주휴수당은 5일 일한 것의 1일치 급여 더 지급

day = int(input("일주일에 몇 일동안 일하세요? (단위:일) "))
time = int(input("몇 시간 동안 일하세요? (단위:시간) "))
week = int(input("몇 주 동안 일하세요? "))
money = int(input("시급이 얼마세요? (단위:원) "))
time_salary = 0

if time*day >= 15:
    time_salary = time * day + (time * day) / 5
    salary = time_salary * week * money

salary = day * time * week * money
print("총 금액은 ", salary)
