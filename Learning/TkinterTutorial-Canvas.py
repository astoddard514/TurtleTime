# https://www.youtube.com/watch?v=HrK9Kmz3_9A&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=68
# https://www.pythontutorial.net/tkinter/tkinter-window/


from tkinter import *

root = Tk()
root.title('Codemy.com - Canvas')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

my_canvas = Canvas(root, width=300, height=200, bg="white")
my_canvas.pack(pady=20)

# Items on canvas start from the base in order of code (Lines then rectangle on top)

# Create Line
# my_canvas.create_lint(x1, y1, x2, y2, fill="color")
my_canvas.create_line(0, 100, 300, 100, fill="red")
my_canvas.create_line(150, 0, 150, 200, fill="red")

# Create Rectangle
# my_canvas.create_rectangle(x1, y1, x2, y2, fill="red")
# Rectangle x1 y1: Top Left
# Rectangle x2, y2: Bottom Right
# Tkinter connects the coordinates with rectangle lines
my_canvas.create_rectangle(150, 0, 150, 200, fill="red")

# Create Oval
# Oval x1 y1: Top Left
# Oval x2, y2: Bottom Right
my_canvas.create_oval(50, 150, 250, 50, fill="cyan")

root.mainloop()