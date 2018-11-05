import random
import turtle as t

t.bgcolor('yellow')

# Characters
player = t.Turtle()
player.shape('square')
player.color('red')
player.speed(0)
player.penup()
player.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), \
    (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False
text_turtle = t.Turtle()
# ERROR: how to do bottom
text_turtle.write('Press SPACE to start', align='center',\
    font=('Ariel', 16))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    pass

def game_over():
    pass

def display_score(current_score):
    pass

def place_leaf():
    pass

def start_game():
    global game_started
    if game_started:
        return
    game_started = True