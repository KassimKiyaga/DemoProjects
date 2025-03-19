import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Change if necessary

num_windows = 10  # Adjust as needed

for _ in range(num_windows):
    subprocess.Popen(chrome_path)  # Opens Chrome using the full path

