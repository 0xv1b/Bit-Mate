import pyautogui

origin_x = ((1920/2) - (800/2))
origin_y = ((1080/2) - (480/2))

x = origin_x + 35
y = origin_y + 70 + 70 + 70 + 70 + 70

pyautogui.click(x, y)