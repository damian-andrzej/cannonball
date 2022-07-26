import time
import turtle
from champ import Champ
from turtle import Screen
from ball import Ball
from top_table import Top_table
from single_block import Single_block

gameon = True
blocks=[]
position_block_x= -370
position_block_y=280
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pegasus Breakout game")
#our main character :)
champ = Champ()

#number of respawns
#patch 2.2 26/07/2022
#functionality moved to top_table class : lives_down method

#blocks to destroy
for a in range(1):
    for x in range(2):
        bloczek = Single_block(position_block_x, position_block_y)
        position_block_x +=50
        blocks.append(bloczek)
    position_block_y -= 40
    position_block_x = -370

print(blocks)
#listener - controlls the paddle
turtle.listen()
turtle.onkey(champ.change_position_left,"Left")
turtle.onkey(champ.change_position_right,"Right")
#ball instance
ball=Ball()
top_table = Top_table()
top_table.show_table()
while gameon:
    ball.move()

    #collision with top wall
    if ball.ycor()>299:
        ball.bounce_block()
    #collision with bottom walls
    if ball.xcor()>390 or ball.xcor() < -390:
        ball.bounce()

    #collision with bottom wall
    if ball.ycor()<-295:
        ball.reset()
        top_table.live_down()
        top_table.show_table()
        #game over module
        if top_table.live_check() < 1:
            top_table.game_over()
            time.sleep(2)
            exit()


    #collision with the paddle
    if ball.distance(champ) < 50 and ball.ycor()< -250:
        ball.bounce_block()
    #collision with blocks
    counter = 0
    for object in blocks:
        if ball.distance(object)<40:
            ball.bounce_block()
            object.hideturtle()
            blocks.remove(object)   # remove object from list -> removes block that desapeared


    #if ball.ycor()




screen.exitonclick()