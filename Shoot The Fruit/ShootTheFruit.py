import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

Score = 0
Time = 30
game_over = False

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")


def draw():
    screen.fill("green")
    apple.draw()
    orange.draw()
    pineapple.draw()
    screen.draw.text("Score: " + str(Score), color="black", topleft=(10, 10))
    screen.draw.text("Time: " + str(Time), color="black", topleft=(10, 580))
    if game_over:
        screen.fill("yellow")
        screen.draw.text("Final Score: " + str(Score), color="black", topleft=(325, 310))
        screen.draw.text("GAME OVER", color="red", topleft=(250, 250), fontsize=60)
    

    
def place_fruits():
    #Apple
    apple.x = randint(10, 800)
    apple.y = randint(20, 600)
    #Orange
    orange.x = randint(10, 800)
    orange.y = randint(20, 600)
    #Pineapple
    pineapple.x = randint(10, 800)
    pineapple.y = randint(20, 600)
    

def on_mouse_down(pos):
    global Score
    if game_over == False:
        if apple.collidepoint(pos):
            print("Awesome Apple! +5")
            place_fruits()
            Score += 5
        elif orange.collidepoint(pos):
            print("Good Orange! +1")
            place_fruits()
            Score += 1
        elif pineapple.collidepoint(pos):
            print("Great Pineapple! +3")
            place_fruits()
            Score += 3
        else:
            print("You missed! -5")
            Score -= 5
            place_fruits()

def update_time():
    global Time
    global game_over

    if Time:
        Time -= 1
    else:
        game_over = True


place_fruits()
clock.schedule_interval(update_time, 1.0)
clock.schedule_interval(place_fruits, 2.5)

pgzrun.go()
