import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.title("Twórz podcast") #Controls the window title.
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        buttons=['Uzupełnij arkusz danymi', 'Przygotuj katalogi robocze', 'Podziel podcast','Przygotuj płytę', 'Scal']
        self.fct=['00_Uzupełnij arkusz z danymi','01_Przygotuj katalogi robocze','02_Podziel podcast','03_Przygotuj płytę','04_Scal']
        self.buttons = {}
        for floor,nme in enumerate(buttons):
            self.buttons[floor] = tk.Button(self, width=30, text=nme, 
                command = lambda f=floor: self.pressed(f),fg='red')
            self.buttons[floor].grid(row=floor, column = 0)

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                    command=root.destroy).grid(row =floor+1 , column = 0)

    def pressed(self, index):
        print("number pressed", index)
        self.buttons[index].configure(fg="orange")
        q=self.fct[index]
        fc=__import__(q)
        fc.r()
        self.buttons[index].configure(fg="green")


root = tk.Tk()
app = Application(master=root)
app.mainloop()