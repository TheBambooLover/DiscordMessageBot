import pyautogui
import time
import random
from datetime import datetime
import numpy as np
import pyautogui
import time

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
    this_time = random.randint(310,311)
    print(this_time)
    go_to_thread()
    while time.time()-start_time < this_time:
        click_by_color()
        time.sleep(2)

def click_by_color():
    target_color = "#248046"  # Example color in IR format
    # Get current pixel colors
    pixel_color_1 = pyautogui.screenshot().getpixel((416, 950))
    pixel_color_2 = pyautogui.screenshot().getpixel((511, 957))

    # Convert colors to strings in IR format for case-insensitive comparison
    pixel_color_str_1 = "#" + "".join(["{:02X}".format(c) for c in pixel_color_1])
    pixel_color_str_2 = "#" + "".join(["{:02X}".format(c) for c in pixel_color_2])

    # Click on pixel 1 if it changed to the target color
    if pixel_color_str_1.lower() == target_color.lower():
        pyautogui.click(416, 950)
        pyautogui.click(511, 1030)
        print(f"Clicked on pixel ({416}, {950}) with color {pixel_color_str_1}")

    # Click on pixel 2 if it changed to the target color
    if pixel_color_str_2.lower() == target_color.lower():
        pyautogui.click(511, 957)
        pyautogui.click(511, 1030)
        print(f"Clicked on pixel ({511}, {957}) with color {pixel_color_str_2}")

def go_to_thread():
    pyautogui.click(x=187, y=403)

def get_cursor_coords():

    input("Move your mouse over the Discord text box and press Enter.")

    # Get the current mouse coordinates
    x, y = pyautogui.position()

    print(f"Coordinates (x, y): {x}, {y}")

def main():
    while True:
        send_message()


if __name__ == "__main__":
    opt = 1
    while opt != 0:
        opt = int(input("Select option: \n1) Run the program\n2) Get mouse coords\n0) To exit\n"))
        if opt == 1:
            main()
        elif opt == 2:
            get_cursor_coords()
        elif opt == 0:
            break
        else:
            print("Please, select a correct option")

