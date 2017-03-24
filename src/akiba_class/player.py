import tkinter as tk   # python3
#import Tkinter as tk   # python

class Player(tk.Tk):

    def __init__(self, parent, controller, name):
        self.info = "Je suis " + name
        self.pions = []
        parent.updateConsole(parent=controller, message=name + " added")

        
