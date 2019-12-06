# 메모장 프로그램 실행
# 'hello world' 작성
# 두 줄 내리고
# '반갑구나 세상아' 작성
# 저장 (hello world.txt 로)

import pyautogui as pag
import time

if __name__ == '__main__':
    pag.press("winleft")
    pag.typewrite("note")
    pag.press("enter")
    time.sleep(1)
    pag.typewrite("hello world")
    pag.press("enter", presses=2)
    pag.press("hangul")
    time.sleep(1)
    pag.typewrite("qksrkqrnsk tptkddk")
    time.sleep(1)
    pag.hotkey("ctrl", "s")
    pag.press("hangul")
    time.sleep(1)
    pag.typewrite("hello world")
    pag.press("enter")
