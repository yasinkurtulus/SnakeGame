from turtle import Turtle
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.bodies=[]
        self.create_snake()
        self.head = self.bodies[0]


    def create_snake(self):
        for i in range(3):
            body = Turtle("square")
            body.color('white')
            body.speed(2)
            body.penup()
            body.setx(-i * 20)
            self.bodies.append(body)

    def extend(self):
        new_body = Turtle("square")
        new_body.color('white')
        new_body.speed(2)
        new_body.penup()
        new_body.goto(self.bodies[-1].position())
        self.bodies.append(new_body)

    def move(self):
        for body in range(len(self.bodies) - 1, 0, -1):
            x_position = self.bodies[body - 1].xcor()
            y_position = self.bodies[body - 1].ycor()
            self.bodies[body].goto(x_position, y_position)
        self.bodies[0].forward(MOVE_DISTANCE)
    def turn_left(self):
        if self.head.heading()!=RIGHT:
            self.bodies[0].setheading(LEFT)
    def turn_right(self):
        if self.bodies[0].heading()!=LEFT:
            self.bodies[0].setheading(RIGHT)
    def turn_up(self):
        if self.bodies[0].heading()!=DOWN:
            self.bodies[0].setheading(UP)
    def turn_down(self):
        if self.bodies[0].heading()!=UP:
            self.bodies[0].setheading(DOWN)
