import os
import platform
import sys
def shutdown_computer():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    if platform.system() == "Windows":
        os.system("shutdown /s /t 0")
    elif platform.system() == "Linux":
        os.system("sudo shutdown now")
    else:
        os.system("python3 typings_.py")
    os.chdir(current_directory)
    sys.exit()a
if __name__ == "__main__":
    shutdown_computer()
