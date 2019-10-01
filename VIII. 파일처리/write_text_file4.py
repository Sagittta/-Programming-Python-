fi = open("history.ama", "w", encoding="utf8")       # ama 는 윈도우에서 열 수 없음. 보여주지 않기 위함.

fi.write("아메리카노\t2300원\t레귤러\t50%\t100%\t코코펄\n")
fi.write("타로버블티\t3200원\t점보\t100%\t100%\t타피오카펄\n")
fi.write("티라미수버블티\t3800원\t점보\t0%\t100%\t타피오카펄\n")

fi.close()