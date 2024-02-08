import pyautogui
import time
import random
from datetime import datetime

def send_message():
    pyautogui.click(x=168, y=298)
    pyautogui.click(x=518, y=1038)
    message = "/earn"

    for char in message:
        keypress_interval = random.uniform(0.1, 0.5)
        pyautogui.write(char, interval=keypress_interval)
    pyautogui.press("enter")
    pyautogui.press("enter")
    now = datetime.now()
    print("Message sent at " + now.strftime("%H:%M"))
    start_time = time.time()
    this_time = random.randint(370,600)
    print(this_time)
    while time.time()-start_time < this_time:
        click_on_screen()
        time.sleep(0.1)



def click_on_screen():
    pyautogui.click(x=187, y=403)
    pyautogui.click(x=416, y=950)
    time.sleep(15)

def main():
    while True:
        send_message()


if __name__ == "__main__":
    main()


# input("Move your mouse over the Discord text box and press Enter.")

# Get the current mouse coordinates
# x, y = pyautogui.position()

# print(f"Coordinates (x, y): {x}, {y}")
