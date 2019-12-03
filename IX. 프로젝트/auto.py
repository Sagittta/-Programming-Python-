# PyAutoGUI 설치  (pip install pyautogui)
import pyautogui as pag
import time

if __name__ == '__main__':
    # while True:
    #     x, y = pag.position()
    #     print("x : {}\t\ty : {}".format(x, y), end="\r")
    # chrome 위치로 이동 (duration=2 : 2초 동안 움직임)
    # pag.moveTo(334, 1045)
    # 지금 위치에서 -100, -200 만큼 이동
    # pag.move(-100, -200)
    # pag.click()
    # pag.doubleClick()     # pag.click(clicks=2)       # pag.click()   pag.click()
    # pag.drag(200, 0, duration=2)
    # pag.rightClick()

    pag.click(334, 1045)
    # TODO : scroll
    # chrome 켜지는 거 기다리기
    time.sleep(1)
    pag.typewrite("ticket.interpark.com")
    pag.press("enter")