import pyautogui as pag

if __name__ == '__main__':
    while True:
        x, y = pag.position()
        print(x, y)
        # print("x : {}\t\ty : {}".format(x, y), end="\r")
