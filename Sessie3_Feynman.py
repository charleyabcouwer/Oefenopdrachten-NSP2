from turtle import Turtle

# Turtle drawing

# create instance of class Turtle
master_oogway = Turtle("turtle")

# use forward() and left() to create a Feynman diagram

master_oogway.forward(50)
master_oogway.left(30)
master_oogway.forward(50)
master_oogway.right(30)
master_oogway.forward(50)
master_oogway.left(30)
master_oogway.forward(50)
master_oogway.right(30)
master_oogway.forward(50)
master_oogway.left(130)
master_oogway.forward(50)
master_oogway.left(30)
master_oogway.forward(100)

master_oogway.screen.mainloop()

# Method __intit__(self)

class Turtle:
    def __init__(self):
        master_oogway = Turtle()

    def forward(self, distance):
        self.forward(50)

    def left(self, angle):
        # turn turtle counterclockwise
        # by angle in degrees
        self.left(30)