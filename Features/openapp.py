import pyautogui

def openapp(app):
    pyautogui.hotkey('win', 's')
    pyautogui.write(app)
    pyautogui.press('enter')

    return f"opening {app},sir"