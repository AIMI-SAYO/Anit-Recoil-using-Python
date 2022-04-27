import pyautogui
import time
import win32api
import random
import keyboard
import ctypes
 
horizontal_range = 2

min_vertical = 1
max_vertical = 3

min_firerate = 0.03
max_firerate = 0.04

toggle_button = 'c'

enabled = False
 
def is_mouse_down():    
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0
 

print("Script running without error")
if enabled:
    print("Script is ENABLED")
else:
    print("Script is DISABLED")
 
last_state = False
while True:
    key_down = keyboard.is_pressed(toggle_button)
    
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("ENABLED")
            else:
                print("DISABLED")
    
    if is_mouse_down() and enabled:
        
        offset_const = 1000
        horizontal_offset = random.randrange(-horizontal_range * offset_const, horizontal_range * offset_const, 1) / offset_const
        vertical_offset = random.randrange(min_vertical * offset_const, max_vertical * offset_const, 1) / offset_const
 
        
        ctypes.windll.user32.mouse_event(0x1, int(horizontal_offset),int(vertical_offset),0,0)
 
        
        time_offset = random.randrange(min_firerate * offset_const, max_firerate * offset_const, 1) / offset_const
        time.sleep(time_offset)
    
    time.sleep(0.001)
