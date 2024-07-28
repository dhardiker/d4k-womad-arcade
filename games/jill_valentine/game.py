# @name Name of my Amazing Example Game
# @author Jane & John Smith
import pgzrun
import random
import sys

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

ship2 = Actor('playership1_red')
ship2.x = 270
ship2.y = 550

gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

gem2 = Actor('gemred')
gem2.x = random.randint(20, 780)
gem2.y = 0

score = 0
game_over = False

def update():
  global score, game_over

  if keyboard.escape:
    exit()
    sys.exit()
  if keyboard.left:
    ship.x = ship.x - 5
  if keyboard.right:
    ship.x = ship.x + 5
  if keyboard.a:
    ship2.x = ship2.x - 5
  if keyboard.d:
    ship2.x = ship2.x + 5

  gem.y = gem.y + 4 + score / 5
  if gem.y > 600:
    game_over = True
  if gem.colliderect(ship):
    gem.x = random.randint(20, 780)
    gem.y = 0
    score = score + 1
  if gem.colliderect(ship2):
    gem.x = random.randint(20, 780)
    gem.y = 0
    score = score + 1
    if gem2.colliderect(ship2):
     gem2.x = random.randint(20, 780)
    gem2.y = 0
    score = score + 2

def draw():
  screen.fill((80,0,70))
  if game_over:
    screen.draw.text('Game Over', centerx=WIDTH/2, top=200, color=(255,255,255), fontsize=150)
    screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=320, color=(255,255,255), fontsize=50)
  else:
    gem.draw()
    gem2.draw()
    ship.draw()
    ship2.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line