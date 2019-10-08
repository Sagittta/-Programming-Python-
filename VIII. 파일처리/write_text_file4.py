fi = open("history.ama", "w", encoding="utf8")       # ama 는 윈도우에서 열 수 없음. 보여주지 않기 위함.

# 원 생략, 레귤러-0 / 점보-1, 50%-1, 100%-2, 0%-0 / 코코펄-1, 타피오카펄-0
fi.write("아메리카노\t2300\t0\t1\t2\t1\n")
fi.write("타로버블티\t3200\t1\t2\t2\t0\n")
fi.write("티라미수버블티\t3800\t1\t0\t2\t0\n")

fi.close()