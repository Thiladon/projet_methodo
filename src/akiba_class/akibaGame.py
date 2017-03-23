import tkinter as tk   # python3
#import Tkinter as tk   # python
from .character import *

class AkibaGame(tk.Tk):

    def __init__(self, parent):
        self.canvas = tk.Canvas(parent, width = 232, height = 232, bg="#b15f01")
        self.canvas.pack()
        self.canvas.place(bordermode="outside", height=232, width=232, x=32, y=64)
        self.setConsole(parent)

        self.characters = []
        self.run(parent)
        
    def addCharacters(self, parent):
        newObj = Character(parent=self, controller=parent, name="test")
        self.characters.append(newObj)

    def setConsole(self, parent):
        self.console = tk.Toplevel(parent)
        self.consoleLabel = []
        # label = tk.Label(self.console, text="test")
        # label.pack(side="top", fill="x", pady="10")
        # self.console.update()

    def updateConsole(self, parent, message="message"):
        newLabel = tk.Label(self.console, text=message)
        newLabel.pack(side="top", fill="x", pady=10)

        self.consoleLabel.append(newLabel)
        self.console.update()

    def drawBoard(self, parent):
        for i in range(0,9):
            self.canvas.create_line(2 + 33*i, 2, 2 + 33*i, 232)
        
    def run(self, parent):
        self.drawBoard(parent)
        self.addCharacters(parent)
