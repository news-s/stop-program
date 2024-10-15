import psutil
from time import sleep
import tkinter as tk
from tkinter import messagebox

# Nazwa programu, którego uruchomienie chcesz monitorować
TARGET_PROGRAM = ["VALORANT.exe", "chrome.exe", "LeagueClient.exe", "Discord.exe", "Riot Client.exe"]  # Zmień na nazwę programu, który chcesz monitorować
exc_list = []

def is_program_running(program_name):
    for proc in psutil.process_iter(['name']):
        name = proc.info['name']
        if name in program_name:
            if name not in exc_list:
                return True
    return False

def show_popup():
    root = tk.Tk()
    root.withdraw()  # Ukrywa główne okno
    messagebox.showinfo("Program uruchomiony", "Czy jesteś pewien, że potrzebujesz z niego korzystać?")
    root.destroy()  # Zamyka okno po potwierdzeniu

if __name__ == "__main__":
    print("Monitoring uruchomienia programu...")

    # Pętla, która monitoruje uruchomienie programu
    while True:
        if is_program_running(TARGET_PROGRAM):
            show_popup()
        sleep(5)
