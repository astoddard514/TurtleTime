# https://www.youtube.com/watch?v=_auZ8TTkojQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=11

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code')
root.iconbitmap() # file location in parenthesis

frame = LabelFrame(root, text="this is my frame . . .", padx=50, pady=50) # padding inside of frame
frame.pack(padx=10, pady=10) # padding outside of frame

b = Button(frame, text="Don't click here")
b.grid(row=0, column=0) # can only mix pack and grid when frames are involved


root.mainloop()
