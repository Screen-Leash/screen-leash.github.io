import webbrowser
import os
import getpass

webbrowser.open('https://screen-leash.github.io/')

USER_NAME = getpass.getuser()
file_path = os.path.realpath(__file__)

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    bat_path = os.path.join(startup_folder, "open.bat")
    with open(bat_path, "w+") as bat_file:
        bat_file.write(f'start "" "{file_path}"')

add_to_startup(file_path)