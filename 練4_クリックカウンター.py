# クリックカウンター
from tkinter import *
window = Tk()
count = 0
def click():
    global count
    count += 1
    if count % 10 == 0:
        print(count,'回')
click1 = Button(window, text='クリック', command=click)
click1.pack()
