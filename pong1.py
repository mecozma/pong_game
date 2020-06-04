import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech ")
wn.bgcolor("black")
wn.setup(width=800, height=600) 
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(-5)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
  #Ball  movement
ball.dx = 0.5
ball.dy = -0.5

#Game functions
  #Paddle A UP & DOWN functions
def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

  #Paddle B UP & DOWN functions
def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

#Keyboard binding
wn.listen()
  #Paddle A movement
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
  #Paddle B movement
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "l")

# Main game loop
while True:
  wn.update()
  #Move the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)
  
  #Border checking

    #Top border
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1

    #Bottom border
  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

    #Right border
  if ball.xcor() > 390:
    ball.goto(0,0)
    ball.dx *= -1
   
   #Left border
  if ball.xcor() < -390:
    ball.goto(0,0)
    ball.dx *= -1


