import pyautogui
from time import sleep

sleep(5)

while True:
    pyautogui.typewrite("Eu quero")

    pyautogui.press("enter")
    print('a')
    sleep(60)
