import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

# screen
win = turtle.Screen()
win.title("Snake Game by @Fərid Gülüm")
win.bgcolor("green")
win.setup(width=600, height=600)
win.tracer(0)  ##

# turtle head

head = turtle.Turtle()
head.speed()
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.shape("square")
pen.speed(0)
pen.ht()
pen.goto(0, 260)
pen.write("Score : 0   High Score : 0", align="center", font=("Roboto", 22, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard binding
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")
# Main game loop
while True:
    win.update()
    # Things dealing with food collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Hide segment elements
        for segment in segments:
            segment.goto(1000, 1000)
        # Clear the segments list
        segments.clear()
        delay = 0.1
        # Reset the score
        score = 0
        # Reset the delay
        delay = 0.1
        pen.clear()
        pen.write(f"Score : {score}  High Score : {high_score}", align="center", font=("Roboto", 22, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # Add a new segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.speed(0)
        new_segment.color("grey")
        segments.append(new_segment)
        delay -= 0.001

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score : {score}  High Score : {high_score}", align="center", font=("Roboto", 22, "normal"))
    # segments joining together
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # segments joining with head

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    for segment in segments:
        if segment.distance(head) < 20:
            head.goto(0, 0)
            head.direction = "stop"
            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset the score
            score = 0
            # Reset the delay
            delay = 0.1

    time.sleep(delay)
# loop to keep screen open

win.mainloop()

# head direction, win tracer
