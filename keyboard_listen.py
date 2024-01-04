from pynput import mouse, keyboard
import pyautogui
import time

last_activity_time = time.time()

def on_keyboard_activity(key):
    global last_activity_time
    last_activity_time = time.time()


def on_mouse_activity(x, y, button, b):
    print(button)
    global last_activity_time
    last_activity_time = time.time()


def is_system_idle(idle_duration_sec=5):
    current_time = time.time()
    idle_time = current_time - last_activity_time
    return idle_time >= idle_duration_sec


def automation_screen(flag):
    if flag == True:
        for i in range(50):
            pyautogui.moveTo(i * 10, 5)
            pyautogui.press("ctrl")
            for i in range(50):
                pyautogui.moveTo(5, (50 - i) * 10)
            pyautogui.hotkey("alt", "tab")
            for i in range(2):
                time.sleep(2)
            pyautogui.hotkey("win", "d")
            for i in range(2):
                time.sleep(2)
            pyautogui.press("win")


if __name__ == "__main__":
    # Setup keyboard listener
    keyboard_listener = keyboard.Listener(on_press=on_keyboard_activity)

    # Setup mouse listener
    mouse_listener = mouse.Listener(
        on_scroll=on_mouse_activity, on_click=on_mouse_activity
    )
    # mouse_listener = mouse.Listener(on_click=on_mouse_activity)

    # Start the listeners
    with keyboard_listener, mouse_listener:
        try:
            while True:
                if is_system_idle():
                    print("System is idle.")
                    automation_screen(True)
                else:
                    print("System is not idle.")
                    automation_screen(False)
                time.sleep(1)
        except KeyboardInterrupt:
            # Stop the listeners when Ctrl+C is pressed
            keyboard_listener.stop()
            mouse_listener.stop()
