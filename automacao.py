import pyautogui as pa
import time

pa.pause=1
pa.press('win')
pa.write('Microsoft Edge')
pa.press('Enter')
time.sleep(3)
pa.write('Youtube.com')
pa.press('Enter')