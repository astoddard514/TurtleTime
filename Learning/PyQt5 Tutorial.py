# https://www.youtube.com/watch?v=Vde5SH8e1OQ

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# create a class to link everything to clicked
class MyWindow(QMainWindow): # MyWindow is-a QMainWindow (inheritance)
    def __init__(self): # init method that will run whenever we create an instance of MyWindow
        super(MyWindow, self).__init__() # parent constructor
        self.setGeometry(200, 200, 300, 300) # (xpos, ypos, width, height)
        self.setWindowTitle("Tech with Tim!")
        self.initUI() # call the function below

    def initUI(self): # this is where all the stuff we want in our window goes
        self.label = QtWidgets.QLabel(self) # label variable, self = MyWindow
        self.label.setText("My first label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self) # button variable
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked) # connects our button to the clicked function, do not need parenthesis

    def clicked(self):
        self.label.setText("you pressed the button") # connects the clicked function we had below earlier, to the label within the whole class
        self.update() # call function below to help labels maintain an appropriate size for text set

    def update(self):
        self.label.adjustSize()


# create a function to find application
def window():
    app = QApplication(sys.argv) 
    win = MyWindow() # could also import and use QWidget
    win.show()
    sys.exit(app.exec_()) # make sure the window will exit when we ask it to

window() 