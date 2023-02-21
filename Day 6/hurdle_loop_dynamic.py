def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_down():
    turn_right()
    move()
    turn_right()
   
def jump():
    move()
    while wall_on_right():
        jump()
    
while not at_goal():
    while front_is_clear():
        move()
    turn_left()
    jump()
    turn_down()
    while not wall_in_front():
        move() 
    turn_left()
    
