import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemblue')
gem.x = random.randint(20, 780)
gem.y = 0

score = 999999999999

def update():
  global score

  if keyboard.escape:
    exit()
    sys.exit()
  
  if keyboard.left:
    ship.x = ship.x - 15
  if keyboard.right:
    ship.x = ship.x + 15

  gem.y = gem.y + 4
  if gem.y > 600:
    gem.x = random.randint(20, 780)
    gem.y = 0
  if gem.colliderect(ship):
    gem.x = random.randint(20, 780)
    gem.y = 0
    score = score + 111111111111

def draw():
  screen.fill((80,0,70))
  gem.draw()
  ship.draw()
  screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line