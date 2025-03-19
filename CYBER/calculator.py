import subprocess

num_windows = 100  # Adjust as needed

for _ in range(num_windows):
    subprocess.Popen("calc.exe")  # Opens Calculator
