from tkinter import *

logs = Tk()
logs.title('Citplanētietis')
a = Canvas(logs, height=300, width=400)
a.pack()
kermenis = a.create_oval(100, 150, 300, 250, fill='green')
acs = a.create_oval(170, 70, 230, 130, fill='white')
zilite = a.create_oval(190, 90, 210, 110, fill='black')
mute = a.create_oval(150, 220, 250, 240, fill='red')
kakls = a.create_line(200, 150, 200, 130)
cepure = a.create_polygon(180, 75, 220, 75, 200, 20, fill='blue')

input()