 # Turtle time game for kids

# Learning resources: 
# https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=1
# https://www.youtube.com/watch?v=lETQ3mvuzkQ

import tkinter
from PIL import Image, ImageTk
import turtle


# Set up screen
root = Tk()
root.title('Turtle Time')
root.geometry('1550x880+100+100')
root.config(bg= '#333366')

# Set up shape functions and tool dashboard functions
class Shapes:

    def formula(sides):
        tansy.pendown()
        angle = 360/sides
        for side in range(sides):
            tansy.forward(100)
            tansy.left(angle)

    def triangle():
        Shapes.formula(3)
    def square():
        Shapes.formula(4)
    def pentagon():
        Shapes.formula(5)
    def hexagon():
        Shapes.formula(6)
    def septagon():
        Shapes.formula(7)
    def octogon():
        Shapes.formula(8)

    def circle():
        tansy.pendown()
        radius = 50
        tansy.circle(radius)

    def ellipse():
        tansy.pendown()
        tansy.seth(-45)
        radius = 100
        for i in range(2):
            tansy.circle(radius, 90)
            tansy.circle(radius//2, 90)

    def star(): 
        tansy.pendown()
        for i in range(5):
            tansy.forward(100)
            tansy.right(144)

    def spiral():
        tansy.pendown()
        tansy.speed(0)
        side = 200
        for i in range(100):
            tansy.forward(side)
            tansy.left(360/5)
            side = side-4
            
    def spirograph(): 
        tansy.pendown()
        tansy.speed(0)
        for i in range(6):
            for color in ('purple', 'red', 'pink',
                          'green', 'blue', 'indigo'):
                tansy.color(color)          
                tansy.circle(50)
                tansy.left(10)

    def spiral_web():
        tansy.pendown()
        tansy.speed(0)
        
        colors = ['purple', 'red', 'pink',
                  'green', 'blue', 'indigo']

        # make spiral_web
        for x in range(200):
            tansy.pencolor(colors[x%6]) # setting color
            tansy.width(x/100 + 2) # setting width
            tansy.forward(x) # moving forward
            tansy.left(59) # moving left
    
class Custom:

    def custom_draw():
        tansy.pendown()
        for i in range(int(custom_sides.get())):
            tansy.forward(int(custom_length.get()))
            tansy.right(int(custom_angle.get()))


class Controls:

    def set_color():
        tansy.pencolor(colorbox.get())
        tansy.color(colorbox.get())

    def penup():
        tansy.penup()
    def pendown():
        tansy.pendown()

    def forward():
        tansy.forward(100)
    def backward():
        tansy.backward(100)

    def rotate_left():
        tansy.left(30)
    def rotate_right():
        tansy.right(30)

    def clear_canvas():
        tansy.clear()
        tansy_default()

    def get_turtle():
        tansy.setpos(0, 0)
        tansy_default()

# Button styling

ft= 'Helvetica 15 bold'
btn_style= ttk.Style()
btn_style.configure('TButton', background= 'black', forground= 'black', font=ft)
ft2 = 'Helvetica 10 bold'
    
# Canvas
canvas_frame = LabelFrame(root, text="TURTLE TIME", font= 'Helvetica 30 bold', padx=25, pady=25, background= '#340f4f', fg= "white", labelanchor= 'n') # padding inside of frame
canvas_frame.grid(column= 0, row=0, rowspan= 3, padx= 50, pady= 50)

canvas = Canvas(canvas_frame, width= 700, height= 625)
canvas.grid(row=0, column=0, padx=25, pady=25)

clear_btn= ttk.Button(canvas, style= 'TButton', text="Clear Canvas", command = Controls.clear_canvas)
clear_btn.place(x= 550, y= 575)

get_turtle_btn= ttk.Button(canvas, style= 'TButton', text="Get Turtle", command = Controls.get_turtle)
get_turtle_btn.place(x= 400, y= 575)

# Create turtle
tansy= turtle.RawTurtle(canvas)
def tansy_default():
    tansy.shape("turtle")
    tansy.resizemode("auto")
    tansy.width(3)
    tansy.color("green")
tansy_default()

# Draw a Shape Frame
draw_a_shape = LabelFrame(root, text="DRAW A SHAPE", font= 'Helvetica 15 bold', padx=25, pady=25, background= '#340f4f', fg= "white", labelanchor= 'n') # padding inside of frame
draw_a_shape.grid(column= 1, row=0, padx = 12, pady= 50 )

triangle_btn= ttk.Button(draw_a_shape, text= 'Triangle', style= 'TButton', command = Shapes.triangle)
square_btn= ttk.Button(draw_a_shape, text= 'Square', style= 'TButton', command = Shapes.square)
circle_btn= ttk.Button(draw_a_shape, text= 'Circle', style= 'TButton', command = Shapes.circle)
ellipse_btn= ttk.Button(draw_a_shape, text= 'Ellipse', style= 'TButton', command = Shapes.ellipse)
pentagon_btn= ttk.Button(draw_a_shape, text= 'Pentagon', style= 'TButton', command = Shapes.pentagon)
hexagon_btn= ttk.Button(draw_a_shape, text= 'Hexagon', style= 'TButton', command = Shapes.hexagon)
septagon_btn= ttk.Button(draw_a_shape, text= 'Septagon', style= 'TButton', command = Shapes.septagon)
octagon_btn= ttk.Button(draw_a_shape, text= 'Octagon', style= 'TButton', command = Shapes.octogon)
star_btn= ttk.Button(draw_a_shape, text= 'Star', style= 'TButton', command = Shapes.star)
spirograph_btn= ttk.Button(draw_a_shape, text= 'Spirograph', style= 'TButton', command = Shapes.spirograph)
spiral_web_btn= ttk.Button(draw_a_shape, text= 'Spiral Web', style= 'TButton', command = Shapes.spiral_web)
spiral_btn= ttk.Button(draw_a_shape, text= 'Spiral', style= 'TButton', command = Shapes.spiral)

triangle_btn.grid(row= 1, column=1, padx=5, pady=5)
square_btn.grid(row= 2, column=1, padx=5, pady=5)
circle_btn.grid(row= 3, column=1, padx=5, pady=5)
ellipse_btn.grid(row= 4, column=1, padx=5, pady=5)
pentagon_btn.grid(row= 1, column= 2, padx=25, pady=5)
hexagon_btn.grid(row= 2, column= 2, padx=25, pady=5)
septagon_btn.grid(row= 3, column= 2, padx=25, pady=5)
octagon_btn.grid(row= 4, column= 2, padx=25, pady=5)
star_btn.grid(row= 1, column= 3, padx=5, pady=5)
spirograph_btn.grid(row= 2, column= 3, padx=5, pady=5)
spiral_web_btn.grid(row= 3, column= 3, padx=5, pady=5)
spiral_btn.grid(row= 4, column= 3, padx=5, pady=5)

# Custom Shape Frame

custom_shape = LabelFrame(root, text="BUILD A SHAPE", font= 'Helvetica 15 bold', padx=25, pady= 25, background= '#340f4f', fg= "white", labelanchor= 'n') # padding inside of frame
custom_shape.grid(column= 1, row=1, padx = 12)

# need to add labels for these input boxes
custom_sides = Entry(custom_shape, font= ft, width= 30)  
custom_sides.grid(row= 0, column= 0, padx=10, pady=10)
custom_sides.insert(0, "Choose # of sides: 0-100 ") 

custom_length = Entry(custom_shape, font= ft, width= 30)  
custom_length.grid(row= 1, column= 0, padx=10, pady=10)
custom_length.insert(0, "Choose length of lines: 0-300")

custom_angle = Entry(custom_shape, font= ft, width= 30)  
custom_angle.grid(row= 2, column= 0, padx=10, pady=10)
custom_angle.insert(0, "Choose angle: 0-360")

draw_custom_shape_btn = ttk.Button(custom_shape, text= "Draw shape", style= 'TButton', command= Custom.custom_draw)
draw_custom_shape_btn.grid(row= 0, column= 1, padx=10, pady=10)

angles_image = Image.open(r"C:/Users/angel/Desktop/Coding/Turtle game/TurtleTime/Images/Angles.jpg")
resize_angles_image = angles_image.resize((128, 100))
angles = ImageTk.PhotoImage(resize_angles_image)

angles_reference = ttk.Label(custom_shape, image= angles)
angles_reference.place(relx= .721, rely= .3)

# Controls Frame

controls = LabelFrame(root, text="CONTROLS", font= 'Helvetica 15 bold',  background= '#340f4f', fg= "white", labelanchor= 'n', padx= 25, pady= 25) # padding inside of frame
controls.grid(column= 1, row=2, padx = 12, pady= 50)


colors= ['red', 'purple', 'yellow',
        'pink', 'blue', 'lightblue', 
        'brown', 'white', 'orange', 
        'green']

colorbox= ttk.Combobox(controls, values= colors)
colorbox.config(font= ft, width= 8)
colorbox.set('Colors')
colorbox.grid(row= 0, column= 0, padx= 5, pady= 10)
colorbox['state']= 'readonly'

set_color_btn= ttk.Button(controls, text= "Set Color", width= 9, command= Controls.set_color)
set_color_btn.grid(row= 1, column= 0)


penup_btn= ttk.Button(controls, text= 'Pen Up', style= 'TButton', width= 9, command= Controls.penup)
pendown_btn= ttk.Button(controls, text= 'Pen Down', style= 'TButton', width= 9, command= Controls.pendown)
foward_btn= ttk.Button(controls, text= 'Forward', style= 'TButton', width= 10, command= Controls.forward)
backward_btn= ttk.Button(controls, text= 'Backward', style= 'TButton', width= 10, command= Controls.backward)

penup_btn.grid(row= 0, column= 1, padx= 25, pady=10)
pendown_btn.grid(row= 1, column= 1, padx= 25, pady= 10)
foward_btn.grid(row= 0, column=3, padx=5, pady= 10)
backward_btn.grid(row= 1, column=3, padx= 5, pady= 10)


left_turn_arrow = Image.open(r"C:/Users/angel/Desktop/Coding/Turtle game/TurtleTime/Images/LeftRotateArrow.png")
resize_left_arrow = left_turn_arrow.resize((30, 30))
left_arrow = ImageTk.PhotoImage(resize_left_arrow)

right_turn_arrow = Image.open(r"C:/Users/angel/Desktop/Coding/Turtle game/TurtleTime/Images/RightRotateArrow.png")
resize_right_arrow = right_turn_arrow.resize((30, 30))
right_arrow = ImageTk.PhotoImage(resize_right_arrow)

left_turn_btn = ttk.Button(controls, image= left_arrow, command= Controls.rotate_left)
left_turn_btn.grid(row= 0, rowspan= 2,  column= 2, padx= 5)
right_turn_btn = ttk.Button(controls, image= right_arrow, command= Controls.rotate_right)
right_turn_btn.grid(row= 0, rowspan= 2, column= 4, padx= 5)


root.mainloop()







