import turtle

win = turtle.Screen()
win.title ("Pong by Rocky")
win.bgcolor("black")
win.setup(width = 800 , height = 600)
win.tracer(0)

score_A = 0
score_B = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid= 5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid= 5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4

#Pen (score)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:"+str(score_A)+ " Player B: "+str(score_B) , align="center" , font=("Courier" , 24, "normal"))



# Function
#Paddle a up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

#Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w" )

#Paddle a down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
win.listen()
win.onkeypress(paddle_a_down, "s" )


#Paddle b up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

#Keyboard binding
win.listen()
win.onkeypress(paddle_b_up, "Up" )

#Paddle b down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
win.listen()
win.onkeypress(paddle_b_down, "Down" )

#Main game loop
while True:
    win.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball . xcor() > 390:
        ball.goto(0 , 0)
        ball.dx*= -1
        score_B += 1
        pen._clear()
        pen.write("Player A:"+str(score_A)+ " Player B: "+str(score_B) , align="center" , font=("Courier" , 24, "normal"))

    if ball . xcor() < -390:
        ball.goto(0 , 0)
        ball.dx*= -1
        score_A += 1
        pen._clear()
        pen.write("Player A:"+str(score_A)+ " Player B: "+str(score_B) , align="center" , font=("Courier" , 24, "normal"))

    #Paddle adn ball collisions
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx*= -1
    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx*= -1 
     






    