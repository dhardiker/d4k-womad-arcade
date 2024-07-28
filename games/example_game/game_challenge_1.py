import pgzrun
import random
import sys

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

score = 0
lives = 3

def update():
  global score, lives

  if keyboard.escape:
    exit()
    sys.exit()
  if keyboard.left:
    ship.x = ship.x - 5
  if keyboard.right:
    ship.x = ship.x + 5

  gem.y = gem.y + 4 + score / 5
  if gem.y > 600:
    gem.x = random.randint(20, 780)
    gem.y = 0
    lives = lives - 1
  if gem.colliderect(ship):
    gem.x = random.randint(20, 780)
    gem.y = 0
    score = score + 1

def draw():
  screen.fill((80,0,70))
  if lives <= 0:
    screen.draw.text('Game Over', centerx=WIDTH/2, top=200, color=(255,255,255), fontsize=150)
    screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=320, color=(255,255,255), fontsize=50)
  else:
    gem.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
    screen.draw.text('Lives: ' + str(lives), (15,35), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line