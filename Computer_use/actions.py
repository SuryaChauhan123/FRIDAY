import pyautogui
import time


def click(x, y):
    pass


def double_click(x, y):
    pass


def right_click(x, y):
    pass


def move(x, y):
    pass


def drag(start_x, start_y, end_x, end_y):
    pass


def type_text(text):
    pass


def press_key(key):
    pass


def hotkey(*keys):
    pass


def scroll(direction, amount):
    pass


def wait(seconds):
    pass

def finish():
    pass


def fail(reason):
    pass


def ask_user(question, options):
    pass



def execute_action(action):

    action_type = action["action"]

    if action_type == "click":
        return click(action["x"], action["y"])

    elif action_type == "double_click":
        return double_click(action["x"], action["y"])

    elif action_type == "right_click":
        return right_click(action["x"], action["y"])

    elif action_type == "move":
        return move(action["x"], action["y"])

    elif action_type == "drag":
        return drag(
            action["start_x"],
            action["start_y"],
            action["end_x"],
            action["end_y"]
        )

    elif action_type == "type":
        return type_text(action["text"])

    elif action_type == "press":
        return press_key(action["key"])

    elif action_type == "hotkey":
        return hotkey(*action["keys"])

    elif action_type == "scroll":
        return scroll(
            action["direction"],
            action["amount"]
        )

    elif action_type == "wait":
        return wait(action["seconds"])

    elif action_type == "finish":
        return finish()

    elif action_type == "fail":
        return fail(action["reason"])

    elif action_type == "ask_user":
        return ask_user(
            action["question"],
            action["options"]
        )

    else:
        raise ValueError(f"Unknown action: {action_type}")