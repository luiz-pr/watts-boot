import pyautogui
import time
import os

os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')

time.sleep(3)

pyautogui.write('https://web.whatsapp.com/')

pyautogui.keyDown('enter')

pyautogui.keyUp('enter')

time.sleep(5)

# coloque o qr code e escolha o contato

pyautogui.write('Oi')

