from turtle import *

state = {'turn': 0}

def spinner():
    "Draw fidget spinner."
    clear()
    angle = state['turn'] / 10
    left(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    left(120)
    forward(100)
    dot(120, 'red')
    back(100)
    left(120)
    forward(100)
    dot(120, 'red')
    back(100)
    left(120)
    update()

def animate():
    "Animate fidget spinner."
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)

def flick():
    "Flick fidget spinner."
    state['turn'] += 50
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()
