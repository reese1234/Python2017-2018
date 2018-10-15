import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0

for dot in range(0, 10):
    Dot = Actor("dot")
    Dot.pos = randint(20, WIDTH - 20), \
        randint(20, HEIGHT - 20)
    dots.append(Dot)

def draw():
    screen.fill("green")
    number = 1
        
    for dot in dots:
        screen.draw.text(str(number), \
                         (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

def on_mouse_down(pos):
    global next_dot
    global lines

    # Correct dot pressed
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot += 1

        # 10th correct dot pressed
        if next_dot == 10:
            clock.schedule(restart, 3.0)   

    # Wrong dot pressed
    else:
        clock.schedule(restart, 3.0)

def restart():
    global lines
    
    lines = []
    next_dot = 0
    
    for dot in dots:
        dot.pos = randint(20, WIDTH - 20), \
            randint(20, HEIGHT - 20)
        draw()
    

pgzrun.go()
