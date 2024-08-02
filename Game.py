import turtle as t


score_a= 0
score_b= 0
win = t.Screen()
win.setup(800,600)
win.bgcolor("blue")
win.title("Pong Game")
win.tracer(0)


#left paddle
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-380,0)

#right paddle
right_paddle=t.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(380,0)

#ball
ball=t.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 0.125
ball.dy = 0.125

#score
pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0",align="center",font=("Ariel",20,"normal"))



#moving paddles
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor() + 20)
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor() - 20)
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 20)
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 20)

win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')
win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')


while True:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #ball collision with wall
    #top wall
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    #bottom wall
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    #right wall
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.goto(0,260)
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=("Ariel",20,"normal"))
    #left wall
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write("Player A:{} Player B:{}".format(score_a, score_b), align="center", font=("Ariel", 20, "normal"))


    #collision with the paddles
    if ball.xcor()>360 and ball.ycor()<right_paddle.ycor()+50 and ball.ycor()>right_paddle.ycor()-50 and ball.dx>0:
        ball.dx *= -1
    if ball.xcor()<-360 and ball.ycor()<left_paddle.ycor()+50 and ball.ycor()>left_paddle.ycor()-50 and ball.dx<0:
        ball.dx *= -1









