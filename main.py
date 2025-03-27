import ctypes
import time
import threading
import keyboard

# --- Windows API Constants ---
INPUT_MOUSE = 0
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP   = 0x0004

# --- Define the MOUSEINPUT Structure ---
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]

# --- Define the INPUT Structure ---
class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("mi", MOUSEINPUT)
    ]

def send_click():
    """
    Sends a left mouse click using the Windows API SendInput function.
    Two events (left button down and left button up) are sent together.
    """
    inputs = (INPUT * 2)()  # Array of two INPUT events
    extra = ctypes.c_ulong(0)
    
    # Configure left mouse button down
    inputs[0].type = INPUT_MOUSE
    inputs[0].mi.dx = 0
    inputs[0].mi.dy = 0
    inputs[0].mi.mouseData = 0
    inputs[0].mi.dwFlags = MOUSEEVENTF_LEFTDOWN
    inputs[0].mi.time = 0
    inputs[0].mi.dwExtraInfo = ctypes.pointer(extra)
    
    # Configure left mouse button up
    inputs[1].type = INPUT_MOUSE
    inputs[1].mi.dx = 0
    inputs[1].mi.dy = 0
    inputs[1].mi.mouseData = 0
    inputs[1].mi.dwFlags = MOUSEEVENTF_LEFTUP
    inputs[1].mi.time = 0
    inputs[1].mi.dwExtraInfo = ctypes.pointer(extra)
    
    # Send both events together
    ctypes.windll.user32.SendInput(2, ctypes.pointer(inputs), ctypes.sizeof(INPUT))

# --- Global Control Variables ---
running = False
click_speed = 1/60  # 60 cps i.e. Each click happens every ~16.67 milliseconds

def click_loop():
    """
    Continuously sends clicks while 'running' is True.
    """
    global running
    while running:
        send_click()
        time.sleep(click_speed)

def start_clicking():
    """
    Starts the clicking thread if it's not already running.
    """
    global running
    if not running:
        running = True
        threading.Thread(target=click_loop, daemon=True).start()

def stop_clicking():
    """
    Stops the clicking process.
    """
    global running
    running = False

# --- User Instructions ---
print("Cookie Clicker Auto Clicker")
print("Press q to start clicking, y to stop clicking, and Esc to exit.")

# --- Set Hotkeys ---
keyboard.add_hotkey('s', start_clicking)  # Start clicking with s
keyboard.add_hotkey('e', stop_clicking)   # Stop clicking with e

# Wait until Esc is pressed to exit the script
keyboard.wait('esc')
