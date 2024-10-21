import psutil
from time import sleep
import tkinter as tk
from functools import partial
import subprocess


def is_program_running(program_name):
    for proc in psutil.process_iter(['name']):
        name = proc.info['name']
        if name in program_name:
            return [True, name]
    return [False, None]

def delete_popup(pop, name):
    pop.destroy()
    try:
        TARGET_PROGRAM.remove(name)  # Dodaje program do listy wykluczeń, aby nie pokazując powtórnego powiadomienia
    except ValueError:
        pass

def delete_program(pop, name):
    pop.destroy()
    subprocess.call(['taskkill', '/F', '/IM', name])

def show_popup(name):
    popup = tk.Tk()
    popup.title("Program uruchomiony")  # Tytuł okna

    popup.attributes("-topmost", True)
    popup.attributes("-toolwindow", True)
    # Ustawienia szerokości i wysokości okna
    popup.geometry("1000x550")

    # Komunikat informujący o uruchomieniu programu
    label = tk.Label(popup, text=f"{name} został uruchomiony! Czy napewno chcesz z niego korzystać?", padx=20, pady=20)
    label.pack()
    # Przycisk OK
    ok_button = tk.Button(popup, text="Dodaj do wykluczeń", command=partial(delete_popup, popup, name))  # Zamyka okno po naciśnięciu
    ok_button.pack(pady=10)
    no_button = tk.Button(popup, text="Wyłącz", command=partial(delete_program, popup, name))  # Zamyka okno po naciśnięciu
    no_button.pack(pady=10)

    popup.mainloop()  # Wyświetla okno w trakcie działania programu

if __name__ == "__main__":
    # Nazwa programu, którego uruchomienie chcesz monitorować
    TARGET_PROGRAM = ["VALORANT.exe", "chrome.exe", "LeagueClient.exe", "Discord.exe", "Riot Client.exe"]  # Zmień na nazwę programu, który chcesz monitorować

    # Pętla, która monitoruje uruchomienie programu
    while True:
        program = is_program_running(TARGET_PROGRAM)
        if program[0]:
            show_popup(program[1])
        sleep(5)
