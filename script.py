import pyautogui
import time
import random

def send_prowl():
    pyautogui.click(x=-920, y=996)

    message = "message"

    for char in message:
        keypress_interval = random.uniform(0.1, 0.5)
        pyautogui.write(char, interval=keypress_interval)
    pyautogui.press("enter")

def main():
    while True:
        interval = random.uniform(310, 497)
        send_prowl()
        time.sleep(interval)

if __name__ == "__main__":
    main()


# import pyautogui

# input("Move your mouse over the Discord text box and press Enter.")

# # Get the current mouse coordinates
# x, y = pyautogui.position()

# print(f"Coordinates (x, y): {x}, {y}")
