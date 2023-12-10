from src.game import Game
from tkinter import Tk
import json

#Turn Bot On or Off
try:
    with open("settings.json", 'r') as file:
        activateBot = json.load(file).get("activateBot", True)
except:
    activateBot = True


if __name__ == "__main__":
    root = Tk()
    game = Game(root, activateBot)
