import pgzrun
import random
import sys

score = 0
gameover = False
WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_red')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

def update():
  global score, gameover

  if keyboard.escape:
    exit()
    sys.exit()

  if keyboard.left:
    ship.x = ship.x - 5
  if keyboard.right:
    ship.x = ship.x + 5

  gem.y = gem.y + 4 + score/5
  if gem.y > 600:
    gameover= True
  if gem.colliderect( ship ):
    gem.x = random.randint(20, 780)
    gem.y = 0
    score = score + 1

def draw():
  screen.fill((80,0,70))
  if gameover:
    screen.draw.text('Game Over', centerx=WIDTH/2, top=200, color=(255,255,255), fontsize=150)
    screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=320, color=(255,255,255), fontsize=50)
  else:
    gem.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)


pgzrun.go() # Must be last line