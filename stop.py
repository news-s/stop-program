# Note to person that found this program:
# This is NOT a malware. Just closing roblox.
# I dont have bad intensions.
# Im a good guy XD 

from time import sleep
import subprocess, os
try:
    import psutil
except:
    os.system("pip install psutil")
    sleep(20)
    import psutil


def is_program_running(program_name):
    for proc in psutil.process_iter(['name']):
        name = proc.info['name']
        if name in program_name:
            return True
    return False

if __name__ == "__main__":
    # Nazwa programu, którego uruchomienie chcesz monitorować
    TARGET_PROGRAM = "RobloxPlayerBeta.exe" # Zmień na nazwę programu, który chcesz monitorować

    # Pętla, która monitoruje uruchomienie programu
    while True:
        program = is_program_running(TARGET_PROGRAM)
        if program:
            subprocess.call(['taskkill', '/F', '/IM', TARGET_PROGRAM])
        sleep(5) 
