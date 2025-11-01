import subprocess
import os
task_list = subprocess.check_output("tasklist").decode("utf-8") 

while True:
    if "uygulama.exe" in task_list:
        print("Program açık")
    else:
        os.system('"C:\\Program Files (x86)\\Honeygain\\Honeygain.exe"')