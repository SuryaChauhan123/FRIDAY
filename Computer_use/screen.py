from pathlib import Path
import pyautogui

def take_screenshot():
    path = Path(__file__).parent / "screen.png"
    src = pyautogui.screenshot()
    src.save(path)
    return str(path)

take_screenshot()