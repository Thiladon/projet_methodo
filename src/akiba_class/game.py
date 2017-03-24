import tkinter as tk   # python3
#import Tkinter as tk   # python
from .player import *
import math as Math

class Game(tk.Tk):

    def __init__(self, parent):
        self.canvas = tk.Canvas(parent, width = 234, height = 234, bg="#b15f01")
        self.canvas.bind("<Button-1>", self.key)
        self.canvas.pack()
        self.canvas.place(bordermode="outside", height=234, width=234, x=32, y=64)
        self.canvas.update()
        self.setConsole(parent)

        self.board =[[1,1,0,0,0,2,2],[1,1,0,3,0,2,2],[0,0,3,3,3,0,0],[0,3,3,3,3,3,0],[0,0,3,3,3,0,0],[2,2,0,3,0,1,1],[2,2,0,0,0,1,1]]

        self.players = []
        self.run(parent)

    def key(self, event):
        # print("clicked at", event.x, event.y)
        self.tile = self.isCase(event)
        if self.tile != False:
            print("{'x': " + str(self.tile['x']) + ", 'y': " + str(self.tile['y']) + "}")
        
    def addPlayers(self, parent, name):
        newObj = Player(parent=self, controller=parent, name=name)
        self.players.append(newObj)

    def setConsole(self, parent):
        self.console = tk.Toplevel(parent)
        self.console.resizable(width=False, height=False)
        self.console.geometry("200x328")
        self.console.scrollbar = tk.Scrollbar(self.console, orient="vertical")
        self.console.scrollbar.pack(fill="y", side="right", expand="FALSE")
        self.consoleLabel = []

    def updateConsole(self, parent, message="message"):
        newLabel = tk.Label(self.console, text=message)
        newLabel.pack(side="top", fill="x", pady=10)

        self.consoleLabel.append(newLabel)
        self.console.update()

    def drawBoard(self, parent):
        print(self.canvas.winfo_height())
        for i in range(0,9,1):
            self.canvas.create_line(1 + (33*i), 1, 1 + (33*i), self.canvas.winfo_height())
            self.canvas.create_line(1, 1 + (33*i), self.canvas.winfo_width(), 1 + (33* i))
        
    def run(self, parent):
        self.drawBoard(parent)

    def isCase(self, event):
        condition = [35,68,101,134,167,200,233]
        obj = {}
        if event.x <= 2 or event.x in condition or event.y <= 2 or event.y in condition:
            return False
        else:
            obj["x"] = Math.floor(((event.x - 3)/33))
            obj["y"] = Math.floor(((event.y - 3)/33))
            return obj
