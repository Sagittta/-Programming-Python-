# 국어, 영어, 수학, 자바, 파이썬, JSP
# 총점, 평균 구하기
# 용돈 구하기
# 90점 이상 : 100,000원
# 80점 이상 : 80,000원
# 70점 이상 : 70,000원
# 60점 이상 : 60,000원
# 그 미만 : 50,000원

k = int(input("국어 성적 입력 : "))
e = int(input("영어 성적 입력 : "))
m = int(input("수학 성적 입력 : "))
jv = int(input("자바 성적 입력 : "))
p = int(input("파이썬 성적 입력 : "))
jsp = int(input("JSP 성적 입력 : "))

score = k + e + m + jv + p + jsp
avg = round(score / 6, 2)

print("\n총점 :", score, "점\n평균 :", avg, "점")

if avg >= 90:
    print("이번 용돈은 100,000원 ~")
elif avg >= 80:
    print("이번 용돈은 80,000원 ~")
elif avg >= 70:
    print("이번 용돈은 70,000원 ~")
elif avg >= 60:
    print("이번 용돈은 60,000원 ~")
else:
    print("이번 용돈은 50,000원 ~")