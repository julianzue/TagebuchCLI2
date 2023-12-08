from colorama import Fore, init
import time
import os
import datetime
import scantree


# colors
r = Fore.LIGHTRED_EX
y = Fore.LIGHTYELLOW_EX
c = Fore.LIGHTCYAN_EX
re = Fore.RESET


class Diary():
    def __init__(self):
        self.prompt()

    def prompt(self):
        self.commands = [
            {
                "id": 1,
                "name": "add",
                "description": "Fügt ein Eintrag hinzu.",
                "function": self.add
            },

            {
                "id": 2,
                "name": "show",
                "description": "Listet alle Einträge in allen Dateien.",
                "function": self.show
            },

            {
                "id": 3,
                "name": "help",
                "description": "Zeigt die Hilfe an.",
                "function": self.help
            },

            {
                "id": 4,
                "name": "search",
                "description": "Sucht in allen Dateien.",
                "function": self.search
            },

            {
                "id": 5,
                "name": "exit",
                "description": "Schließt das Programm.",
                "function": self.exit
            }
        ]

        command = input(y + "[+] > " + re)

        print("")

        for command_in_list in self.commands:
            if command == command_in_list["name"]:
                command_in_list["function"]()
                print("")

        self.prompt()


    def add(self):
        entry = input(y + "[+] Neuer Eintrag: " + re)

        year = time.strftime("%Y")
        week = time.strftime("%V")
        day = time.strftime("%A")[:3].upper()

        if not os.path.exists("tagebuch"):
            os.mkdir("tagebuch")

        if not os.path.exists("tagebuch/" + year):
            os.mkdir("tagebuch/" + year)

        if not os.path.exists("tagebuch/" + year + "/" + week):
            os.mkdir("tagebuch/" + year + "/" + week)
        
        with open("tagebuch/" + year + "/" + week + "/" + day + ".txt", "a") as fa:
            fa.write(time.strftime("%Y-%m-%d") + " | " + entry + "\n")
            
        print(c + "[*] " + re + "Eintrag erfolgreich hinzugefügt.")


    def show(self):
        for item in os.scandir("tagebuch"):
            if item.is_dir():
                for subitem in os.scandir("tagebuch/" + item.name):
                    if subitem.is_dir():
                        for subsubitem in os.scandir("tagebuch/" + item.name + "/" + subitem.name):
                            if subsubitem.name.endswith(".txt"):
                                with open("tagebuch/" + item.name + "/" + subitem.name + "/" + subsubitem.name, "r") as fr:
                                    for line in fr.readlines():
                                        print(subsubitem.name.strip(".txt") + " | " + line.strip("\n"))



    def help(self):
        for item in self.commands:
            print(item["name"] + "\t" + item["description"])
  

    def search(self):

        search_text = input(y + "[+] Suchtext eingeben: " + re)
        print("")

        for item in os.scandir("tagebuch"):
            if item.is_dir():
                for subitem in os.scandir("tagebuch/" + item.name):
                    if subitem.is_dir():
                        for subsubitem in os.scandir("tagebuch/" + item.name + "/" + subitem.name):
                            if subsubitem.name.endswith(".txt"):
                                with open("tagebuch/" + item.name + "/" + subitem.name + "/" + subsubitem.name, "r") as fr:
                                    for line in fr.readlines():
                                        if search_text in line:
                                            print(subsubitem.name.strip(".txt") + " | " + line.strip("\n"))


    def exit(self):
        print(r + "[!] " + re + "Programm geschlossen.")
    
        quit()


Diary()