# https://www.youtube.com/watch?v=Vde5SH8e1OQ

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# this is a function to define what happens with a button is clicked
def clicked():
    print("clicked")

# create a function to find application
def window():
    app = QApplication(sys.argv) 
    win = QMainWindow() # could also import and use QWidget
    win.setGeometry(200, 200, 300, 300) # (xpos, ypos, width, height)
    win.setWindowTitle("Tech with Tim!")

    label = QtWidgets.QLabel(win) # label variable
    label.setText("My first label")
    label.move(50, 50)

    b1 = QtWidgets.QPushButton(win) # button variable
    b1.setText("Click me")
    b1.clicked.connect(clicked) # connects our button to the clicked function

    win.show()
    sys.exit(app.exec_()) # make sure the window will exit when we ask it to

window() 
