import tkinter as tk   # python3
#import Tkinter as tk   # python

class Character(tk.Tk):

    def __init__(self, parent, controller, name):
        self.info = "Je suis " + name
        print(name + " : Character Added!" )
        parent.updateConsole(parent=controller, message="Character Added")
