import subprocess

# Number of windows to open
num_windows = 10  # Change this to open more or fewer windows

for _ in range(num_windows):
    subprocess.Popen("notepad.exe")  # Opens Notepad
