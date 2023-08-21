from tkinter import *
from Archive.MiR_Mission_Control_V1 import *
#import readPLCTag

window = Tk()
window.title('MiR Rest Commands')
window.geometry("500x500")

btn1 = Button(window, text = "Swap Pallet", command = postMission)
btn1.place(x=10, y=10)

btn2 = Button(window, text = "Get Missions", command = getMissions)
btn2.place(x=10, y=50)

#btn3 = Button(window, text = "PLC Value", command = getValue)
#btn3.place(x=10, y=90)

window.mainloop()