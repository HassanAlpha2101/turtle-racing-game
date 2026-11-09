from turtle import Turtle , Screen
import random
def position(name ,z):
    name.goto(-230,-200+60*z)

screen = Screen()
user_ip=screen.textinput(title ="choose your bet", prompt="Which turtle will win the race")
print(user_ip)
screen.setup(width=500,height=400)
is_race_on = False
turtle_name =[]
colors = ["red","orange","yellow","green","blue","purple"]

for i in range(0,len(colors)):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    position(tim, i)
    turtle_name.append(tim)

if user_ip:
    is_race_on = True

while is_race_on:
    for turtle in turtle_name:
        randon_move = random.randint(1, 20)
        turtle.forward(randon_move)
        if turtle.xcor()>230:
            is_race_on = False
            the_winning_colour=turtle.pencolor()
            if the_winning_colour==user_ip:
                print(f"You Win! , the winning turtle is {the_winning_colour}")
            else:
                print(f"You Lose! , the winning turtle is {the_winning_colour}")
screen.exitonclick()

