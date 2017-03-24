import tkinter as tk   # python3
#import Tkinter as tk   # python
from akiba_class.game import *

TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        # Empêche le redimensionnement et met la fenetre en 648*328

        self.resizable(width=False, height=False)
        self.geometry("648x328")
        
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.update()

        self.frames = {}
        self.frames["MainPage"] = MainPage(parent=container, controller=self)
        self.frames["GameWindow"] = GameWindow(parent=container, controller=self)
        self.frames["OptionsWindow"] = OptionsWindow(parent=container, controller=self)

        self.frames["MainPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["GameWindow"].grid(row=0, column=0, sticky="nsew")
        self.frames["OptionsWindow"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):

        # On place la page appelé en haut du tas, afin que ce soit celle affiché.
        
        frame = self.frames[page_name]
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        frame_init(self, parent, controller)
        label = tk.Label(self, text="Jeu du Akiba", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        self.update()

        # On instancie les widgets.
        
        onePlayer       = tk.Button(self, text="1 Joueur", command=lambda: self.playOnClick(parent, controller, 1))
        twoPlayer       = tk.Button(self, text="2 Joueurs", command=lambda: self.playOnClick(parent, controller, 2))
        optionButton    = tk.Button(self, text="Options", command=lambda: controller.show_frame("OptionsWindow"))
        quitButton      = tk.Button(self, text="Quitter", command=lambda: controller.destroy())

        # On place les widgets.
        
        onePlayer.pack()
        onePlayer.place(bordermode="outside", height=40, width=164, x=(calc(pos="x", container=parent) - 92), y=(calc(pos="y", container=parent) - 50))
        twoPlayer.pack()
        twoPlayer.place(bordermode="outside", height=40, width=164, x=(calc(pos="x", container=parent) + 92), y=(calc(pos="y", container=parent) - 50))
        optionButton.pack()
        optionButton.place(bordermode="outside", height=40, width=164, x=calc(pos="x", container=parent), y=(calc(pos="y", container=parent) + 20))
        quitButton.pack()
        quitButton.place(bordermode="outside", height=40, width=164, x=calc(pos="x", container=parent), y=(calc(pos="y", container=parent) + 90))

    def playOnClick(self, parent, controller, nbPlayer):
        akiba = Game(controller.frames["GameWindow"])

        for i in range(25):
            print(i)
            akiba.addPlayers(controller.frames["GameWindow"], "Joueur-" + str(i+1))

        # On instancie le l'affichage de GameWindow après l'initialisation complète des widgets propre à cette objet.
            
        controller.show_frame("GameWindow")
            

class GameWindow(tk.Frame):

    def __init__(self, parent, controller):
        frame_init(self, parent, controller)


class OptionsWindow(tk.Frame):

    def __init__(self, parent, controller):
        frame_init(self, parent, controller)
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("MainPage"))
        button.pack()

def calc(container, pos="x", height=40, width=164):
    if pos == "x":
        print((container.winfo_width()/2) - (width/2))
        return ((container.winfo_width()/2) - (width/2))
    elif pos == "y":
        print((container.winfo_height()/2) - (height/2))
        return ((container.winfo_height()/2) - (height/2))
    else:
        return 0

def frame_init(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
