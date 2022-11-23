#import modules
import turtle
import time
import random

#Full path: r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\
#Relative path r"Ping Pong\\Assets\\""
def main():
    # Add new shapes to turtle shape list
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\Ball.gif",shape=None) #Use the relative path
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\PaddleA.gif",shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\PaddleB.gif",shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\Exit_Icon.gif", shape=None)

    #Setting up the screen
    wn = turtle.Screen()
    wn.title("Ping Pong")
    wn.bgcolor('Black')
    wn.setup(width=800, height=600)
    wn.tracer(0)

    #Score
    scoreA = 0
    scoreB = 0

    #Exit button
    ExitButton = turtle.Turtle()
    ExitButton.penup()
    ExitButton.speed(0)
    ExitButton.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\Exit_Icon.gif")
    ExitButton.pencolor("white")
    ExitButton.setx(0)
    ExitButton.sety(-325)
    ExitButton.shapesize(1.5, 3)
    ExitButton.goto(0, -325)

    #drawing a border
    Border = turtle.Turtle()
    Border.color("white")
    Border.hideturtle()
    Border.penup()
    Border.goto(400,300)
    Border.pendown()
    Border.goto(400,-300)
    Border.goto(-400,-300)
    Border.goto(-400,300)
    Border.goto(400,300)

    #Paddle A
    paddleA = turtle.Turtle()
    paddleA.speed(0)
    paddleA.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\PaddleA.gif")
    paddleA.color("White")
    paddleA.shapesize(stretch_wid=5, stretch_len=1)
    paddleA.penup()
    paddleA.goto(-350, 0)

    #Paddle B
    paddleB = turtle.Turtle()
    paddleB.speed(0)
    paddleB.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\PaddleB.gif")
    paddleB.color("White")
    paddleB.shapesize(stretch_wid=5, stretch_len=1)
    paddleB.penup()
    paddleB.goto(350, 0)

    #Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\Ball.gif")
    ball.color("White")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2
    ball.dy = 2

    #ScoreA
    ScoreA = turtle.Turtle()
    ScoreA.speed(0)
    ScoreA.color("white")
    ScoreA.penup()
    ScoreA.hideturtle()
    ScoreA.goto(-200, 265)
    ScoreA.write("Player A: 0", align="center", font=("Courier", 24, "bold"))

    #ScoreB
    ScoreB = turtle.Turtle()
    ScoreB.speed(0)
    ScoreB.color("white")
    ScoreB.penup()
    ScoreB.hideturtle()
    ScoreB.goto(200, 265)
    ScoreB.write("Player B: 0", align="center", font=("Courier", 24, "bold"))

    #Function
    def Quit(x,y):
        if (x > -30 and x < 30) and (y < -310 and y > -340):
            wn.bye()

    def paddleA_up():
        if paddleA.ycor() + 25 < 270:
            y = paddleA.ycor()
            y += 25
            paddleA.sety(y)

    def paddleA_down():
        if paddleA.ycor() - 25 > -270:
            y = paddleA.ycor()
            y -= 25
            paddleA.sety(y)

    def paddleB_up():
        if paddleB.ycor() + 25 < 270:
            y = paddleB.ycor()
            y += 25
            paddleB.sety(y)

    def paddleB_down():
        if paddleB.ycor() - 25 > -270:
            y = paddleB.ycor()
            y -= 25
            paddleB.sety(y)

    #Keyboard binding
    wn.listen()
    wn.onkeypress(paddleA_up, "w")
    wn.onkeypress(paddleA_down, "s")
    wn.onkeypress(paddleB_up, "Up")
    wn.onkeypress(paddleB_down, "Down")

    #Main game loop
    while True:
        wn.bgpic(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\CityBG.gif")
        wn.onclick(Quit)
        wn.update()

        #Moving the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        #Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            
        if ball.xcor() > 390:
            ball.goto(0,0)
            direction = random.randint(1,10)
            ball.dx = 2
            if direction <= 5:
                ball.dx *= -1
            else:
                ball.dx *= 1
            scoreA += 1
            ScoreA.clear()
            ScoreA.goto(-200, 265)
            ScoreA.write("Player A:"+str(scoreA), align="center", font=("Courier", 24, "bold"))

        if ball.xcor() < -390:
            ball.goto(0,0)
            direction = random.randint(1,10)
            ball.dx = 2
            if direction <= 5:
                ball.dx *= -1
            else:
                ball.dx *= 1
            scoreB += 1
            ScoreB.clear()
            ScoreB.goto(200, 265)
            ScoreB.write("Player B:"+str(scoreB), align="center", font=("Courier", 24, "bold"))

        #Paddle and ball collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() +40 and ball.ycor() > paddleB.ycor() -40):
            ball.setx(340)
            ball.dx *= -1.2

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() +40 and ball.ycor() > paddleA.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1.2

def StartUp():
    wn = turtle.Screen()
    wn.title("Ping Pong")
    wn.bgcolor('Black')
    wn.setup(width=800, height=600)
    wn.tracer(0)

    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\Start_Icon.gif", shape=None)

    Border = turtle.Turtle()
    Border.color("white")
    Border.hideturtle()
    Border.penup()
    Border.goto(400,300)
    Border.pendown()
    Border.goto(400,-300)
    Border.goto(-400,-300)
    Border.goto(-400,300)
    Border.goto(400,300)

    StartButton = turtle.Turtle()
    StartButton.penup()
    StartButton.speed(0)
    StartButton.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\Start_Icon.gif")
    StartButton.pencolor("white")
    StartButton.shapesize(1.5, 3)
    StartButton.goto(0,0)

    def Start(x,y):
        if (x > -30 and x < 30) and (y < 15 and y > -15):
            wn.clear()
            StartButton.clear()
            StartButton.hideturtle()
            Border.clear()

            main()

    while True:
        wn.bgpic(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Ping Pong\\Assets\\CityBG.gif")
        wn.update()
        wn.onclick(Start)

StartUp()