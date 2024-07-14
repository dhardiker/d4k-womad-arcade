# @name Name of my Amazing Example Game
# @author Jane & John Smith
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

def draw():
  ship.draw()

pgzrun.go() # Must be last line