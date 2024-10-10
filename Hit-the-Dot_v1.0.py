# a121_catch_a_turtle.py
#-----import statements-----
import random
import turtle as trtl

#-----game configuration----
score = 0
time_left = 3
time_up = False
counter_interval = 1000
score_font = "Audiowide", 20, "normal"

#-----initialize turtle-----

#This is the actual target, in case you couldnt tell by the name :)
target = trtl.Turtle(shape="circle",)
target.penup()
target.speed(0)
target.color("red")

#Pen is the turtle that writes the score
pen = trtl.Turtle(visible=False)
pen.penup()
pen.goto(-250, 250)
pen.pendown()

#Timekeeper is the turtle that writes the clock.
timekeeper = trtl.Turtle(visible=False)
timekeeper.penup()
timekeeper.goto(250, 250)
timekeeper.pendown()

#-----game functions--------
def update_score():
    global score

    score += 1
    pen.undo()
    pen.write("Score: " + str(score), font=score_font)

#The clock looks a little weird when it resets; find a way to fix that later
def target_clicked(x, y):
    global time_left, time_up
    if time_up == False:
        change_pos()
        update_score()
        time_left = 3
        timekeeper.clear()
        timekeeper.write(time_left, font=score_font)
        time_left -= 1

#Function to change the target's position
def change_pos():
    global x_pos, y_pos
    random.seed()
    x_pos = random.randint(-240, 240)
    y_pos = random.randint(-240, 240)
    target.goto(x_pos, y_pos)

#This funtion handles the entire clock.
def clock():
    global time_left, time_up
    timekeeper.clear()
    if time_left <= 0:
        timekeeper.write("Time is up!", font=score_font)
        time_up = True
    else:
        timekeeper.write(time_left, font=score_font)
        time_left -= 1
        timekeeper.getscreen().ontimer(clock, counter_interval)

#This is supposed to be a way to make a penalty when te user clicks on the background and misses the turtle, but it doesn't work very well. ¯\_(ツ)_/¯ I'll fix it later.
def test(x, y):
    global time_left
    if time_left == False:
        time_left -= 1
        timekeeper.clear()
        timekeeper.write(time_left, font=score_font)

#-----events----------------
for side in range(4):
    pen.forward(510)
    pen.right(90)

pen.write("START!", font=score_font)
running = True

clock()

target.onclick(target_clicked)

wn = trtl.Screen()
#wn.onclick(test)
wn.mainloop()
