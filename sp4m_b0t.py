import sys
import pyautogui
import time
import keyboard

print('Sp4m_B0t.py')
print('made by sh1nt31m41\n\n')

print('Press Enter to determine your mouse position\n')

try:
    while True:
        x, y = pyautogui.position()

        if keyboard.is_pressed('enter'):
            break

        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    sys.exit()

_ = input('') # clear stdinput

count = int(input('Enter spam counts: '))
message = str(input('Enter spam message: '))

while count > 0:
    pyautogui.click(x, y)
    pyautogui.write(message)
    pyautogui.press('enter')

    time.sleep(1)
    count -= 1
