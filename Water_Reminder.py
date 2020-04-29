from tkinter import Tk
from tkinter import Label
from tkinter import Button
import time

timer = (45*60)
def drink_water():
    root = Tk()
    Label(root, text="Drink water and Stand Up..").pack()
    Button(root, text="Quit", command=root.destroy).pack()
    root.mainloop()
    return "Well Done!"
if __name__ == "__main__":
    while True:
        time.sleep(timer)
        drink_water()