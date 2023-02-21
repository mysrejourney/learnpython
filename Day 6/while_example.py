def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_down():
    turn_right()
    move()
 
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_down()
    turn_left()
    
while not at_goal():
    jump()