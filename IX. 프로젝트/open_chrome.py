import pyautogui as pag
import time

if __name__ == '__main__':
    # data = pag.locateOnScreen("chrome.png")
    # print(data)
    # # pag.click(data.left + data.width / 2, data.top + data.height / 2)
    # center = pag.center(data)
    # print(center)

    # center = pag.locateCenterOnScreen("chrome.png")
    # pag.click(center)

    datas = pag.locateAllOnScreen("chrome.png")
    for data in datas:
        print(data)
