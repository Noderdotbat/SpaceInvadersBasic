#Import everything
import turtle
import os
import math
import random

#Set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")
window.bgpic("space_invaders_background.gif")
turtle.setup(600, 600, None, None)

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to zero
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" % score
score_pen.write(scorestring, False, align="Left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
#player.setheading(90)


#Choose a number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []
#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    # Create the enemy
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(-x, y)

enemyspeed = 2


#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 40

#Define bullet state
#Ready - ready to fire
#Fire - bullet is firing
bulletstate = "ready"

#Move player
playerspeed = 15;

def move_left():
    x = player.xcor()
    x = x - playerspeed
    if(x < - 280):
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x = x + playerspeed
    if(x > 280):
        x = 280
    player.setx(x)
def fire_bullet():
    #Declare bulletstate as global if it needs change
    global bulletstate
    if(bulletstate == "ready"):
        bulletstate = "fire"
        #Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Game loop
while(True):

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x = x + enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if (enemy.xcor() > 280):
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y = y - 40
                e.sety(y)
            #Change enemy direction
            enemyspeed = enemyspeed * -1

        if (enemy.xcor() < -280):
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y = y - 40
                e.sety(y)
            #Change enemy  dierection
            enemyspeed = enemyspeed * -1

        # Check for a collision between the bullet and the enemy
        if (isCollision(bullet, enemy)):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(-x, y)
            #Update score
            score = score + 1
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="Left", font=("Arial", 14, "normal"))

        #Checks for collision between player and enemy
        if (isCollision(player, enemy)):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Move the bullet
    if(bulletstate == "fire"):
        y = bullet.ycor()
        y = y + bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has gone to the top
    if(bullet.ycor() > 275):
        bullet.hideturtle()
        bulletstate = "ready"

delay = input("Press Enter To Finish: ")
