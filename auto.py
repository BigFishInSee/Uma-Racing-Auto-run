from pynput import mouse, keyboard
import threading
import time
import random
 
spamming = False
kb = keyboard.Controller()

def spam_keys():
    global spamming
    while spamming:
        kb.press('q')
        kb.release('q')
        time.sleep(random.uniform(0.02, 0.04))  

        kb.press('e')
        kb.release('e')
        time.sleep(random.uniform(0.02, 0.04)) 

def on_click(x, y, button, pressed):
    global spamming
    if button == mouse.Button.right and pressed:
        spamming = not spamming
        if spamming:
            threading.Thread(target=spam_keys, daemon=True).start()
            print("Started spamming q and e")
        else:
            print("Stopped spamming q and e")


with mouse.Listener(on_click=on_click) as listener:
    listener.join()