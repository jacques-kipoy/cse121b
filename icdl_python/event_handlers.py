import turtle # import the turtle library
screenr = turtle.Screen()  # Give the screen a reference 
pointer = turtle.Turtle() # give the turtle a reference

def h1():
    pointer.sety(pointer.ycor()+10) # move the poiniter 10 pixels up

def h2():
    pointer.sety(pointer.ycor()-10) # move the poiniter 10 pixels down

def h3():
    pointer.forward(10) # move the poiniter 10 pixels right

def h4():
    pointer.back(10) # move the pointer 10 pixels left

def h5():
    pointer.penup() # Stop drawing

def h6():
    pointer.pendown() # Start drawing

def h7():
    pointer.pencolor("black") # change the drawing color to black   

def h8():
    pointer.pencolor("white") #change the drawing color to white

def h9():
    pointer.left(180) # change the pointer direction by 180 degrees

def h10():
    pointer.color("red") # change pointer fill color

screenr.onkey(h1, "Up") # when the up arrow is pressed run h1 subroutine
screenr.onkey(h2, "Down") # when the Down arrow is pressed run h2 subroutine
screenr.onkey(h3, "Right") # when the right arrow is pressed run h3 subroutine
screenr.onkey(h4, "Left") # when the Left arrow is pressed run h4 subroutine
screenr.onkey(h5, "p") # when the letter p is pressed run h5 subroutine
screenr.onkey(h6, "d") # when the letter d is pressed run h6 subroutine
screenr.onkey(h7, "b") # when the letter b is pressed run h7 subroutine
screenr.onkey(h8, "w") # when the letter w is pressed run h8 subroutine
screenr.onclick(h9) # when the mouse is clicked run h9 subroutine
screenr.ontimer(h10, 5000) # when the timer times out run h10 subroutine
screenr.listen() # check to see if any event has happened

turtle.mainloop() # keep looping

