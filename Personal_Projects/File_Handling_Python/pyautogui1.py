import pyautogui
import time


pyautogui.moveTo(592,1043)
pyautogui.click()
pyautogui.moveTo(1189,473)
pyautogui.click()
e = 0
while True:
    pyautogui.write('Hii')
    #time.sleep(0.25)
    pyautogui.press('enter')
    e+=1
    if e==11:
        break
