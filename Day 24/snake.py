from turtle import Turtle

# TODO 2 - Create a snake body

""" Place the snake segments in their starting position """
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
""" Move the snake for 20 distance """
MOVE_DISTANCE = 20
""" Move the snake to the following direction with the respective angles """
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:  # Create snake class

    def __init__(self):
        self.segments = []  # Create an empty list to hold all snake segments together
        self.create_snake()  # Create the snake method which will create snake body
        """ Snake head is the main to move or change the direction """
        self.head = self.segments[0]  # snake's first segment considered as snake's head

    def create_snake(self):
        """ Create snake body """
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position: object) -> object:
        """ Creating the snake body by adding segments at the end of the snake tail """
        new_segments = Turtle()
        new_segments.shape("square")  # Creating snake using square turtle object
        new_segments.color("white")  # Giving white color for the turtle
        new_segments.penup()  # Taking penup, so it won't create a line while moving
        new_segments.goto(position)  # Move the snake to the starting position
        self.segments.append(new_segments)

    def extend_snake(self):
        """ Extending the snake when it eats food. The new segment should add always at the tail (end of the snake) """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ Move the third segment of the snake body to second position.
            Second to first position. First will move based on the instruction (may turn left/right/ or move forward)
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_position = self.segments[seg_num - 1].xcor()
            new_y_position = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_position, new_y_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):  # Move the snake upwards
        """ Make sure when snake is moving up, it should not come down when down key pressed """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):  # Move the snake downwards
        """ Make sure when snake is moving down, it should not come up when up key pressed """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):  # Move the snake right side
        """ Make sure when snake is moving right, it should not come left when left key pressed """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):  # Move the snake left side
        """ Make sure when snake is moving left, it should not come right when right key pressed """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  # snake's first segment considered as snake's head

