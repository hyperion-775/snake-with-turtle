import turtle
import time
import random

#presets at the beginning
delay = .1
score = 0
high_score = 0

#creating a screen
display_screen = turtle.Screen()
display_screen.title("Snake Game")
display_screen.bgcolor("black")

#making the snake head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("white")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "Stop"

#making the apples
apples = turtle.Turtle()
shapes = random.choice(["square", "triangle", "circle"])
apples.speed(0)
apples.shape(shapes)
apples.color("red")
apples.penup()
apples.goto(0, 100)

#making the pen 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
#adjust per ui screen size
pen.goto(0, 220)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))

# assigning key directions
def group():
    if snake_head.direction != "down":
        snake_head.direction = "up"
 
 
def godown():
    if snake_head.direction != "up":
        snake_head.direction = "down"
 
 
def goleft():
    if snake_head.direction != "right":
        snake_head.direction = "left"
 
 
def goright():
    if snake_head.direction != "left":
        snake_head.direction = "right"
 
 
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y+20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y-20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x-20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x+20)
 
 
         
display_screen.listen()
display_screen.onkeypress(group, "w")
display_screen.onkeypress(godown, "s")
display_screen.onkeypress(goleft, "a")
display_screen.onkeypress(goright, "d")
 
segments = []
 
 
 
# Main Gameplay
while True:
    display_screen.update()
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "Stop"
        colors = "red"
        shapes = random.choice(["square", "circle"])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if snake_head.distance(apples) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        apples.goto(x, y)
 
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"
            colors = "red"
            shapes = random.choice(["square", "circle"])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
 
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
 
display_screen.mainloop()
