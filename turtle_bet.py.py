from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

t = [Turtle() for i in range(5)]
color = ["red", "green", "blue", "brown", "orange"]


def start():
    y = -100
    idx = 0
    for i in t:
        i.speed(10)
        i.color(color[idx])
        idx += 1
        i.shape("turtle")
        i.penup()
        i.goto(-230, y)
        y += 50


bet = screen.textinput("Your bet", "Choose a color: red, green, blue, brown, orange")


def race():
    flag = True
    while flag:
        x = random.choice(t)
        x.forward(10)
        if x.xcor() == 230:
            flag = False
            if bet == x.color()[0]:
                print(f"You win the bet, {x.color()[0]} turtle won.")
            else:
                print(f"You lose the bet, {x.color()[0]} turtle won.")
            return ()


start()
race()


screen.exitonclick()
