# 🖱️ Cookie Clicker Auto Clicker

A fast and lightweight Windows-based auto-clicker built with Python. It simulates real mouse (i.e.hardware-like input) using the Windows API,
making it harder for games to detect compared to software-level automation.

## ⚙️ Features

- Hardware-like mouse input (via `SendInput`)
- 60 clicks per second (CPS) by default
- Hotkey-controlled:
  - `s`: Start clicking
  - `e`: Stop clicking
  - `Esc`: Exit the program

## 🔒 Hardware vs Software-Based Input

This script uses **hardware-level input simulation** via the `ctypes.windll.user32.SendInput` API. This is the same system-level function Windows uses for real mouse events. Because of this:

- The operating system treats clicks as if they came from a physical mouse
- Many web games (like Cookie Clicker) or simple anti-cheat mechanisms cannot distinguish it from real user input
- It offers a stealthier alternative to software-only clickers or browser automation

> ⚠️ Note: This does not guarantee bypassing all forms of anti-cheat in more sophisticated games, but works well for lightweight detection like in idle clickers or web-based games.

## 🚀 Getting Started

### Requirements

- Python 3.6+
- Windows OS (required due to use of Windows API)
- This script must be run with **administrator privileges** to allow global hotkey listening.


## 🛠️ Want Custom Automation?

Looking to automate mouse input in a different way—maybe targeting specific apps, adjusting click patterns, adding right-clicks, coordinates-based actions, or even drag-and-drop?

Whether it's gaming, repetitive tasks, or a unique use-case, feel free to reach out!

**Let me know and I can help expand the project too.**
