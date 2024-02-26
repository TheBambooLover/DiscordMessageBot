import pyautogui
import time
import pyautogui
import time

pyautogui.FAILSAFE = False

def send_message():
    message = "milanesa"

    for char in message:
        pyautogui.write(char)
    pyautogui.press("enter")
    pyautogui.press("enter")

def main():
    time.sleep(2)
    while True:
        send_message()
        time.sleep(35)


if __name__ == "__main__":
    main()

