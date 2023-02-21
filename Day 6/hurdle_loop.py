def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_down():
    turn_right()
    move()
    
for n in range(0,6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_down()
    turn_left()