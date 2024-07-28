import pgzrun
import random
import sys

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_green')
ship.x = 370
ship.y = 550

life = 3


gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

gem1 = Actor('gemred')
gem1.x = random.randint(20, 780)
gem1.y = 0

score = 0
game_over = False

def update():
  global score, game_over, life

  if keyboard.escape:
    exit()
    sys.exit()
  if keyboard.left:
    ship.x = ship.x - 5
  if keyboard.right:
    ship.x = ship.x + 5

  gem.y = gem.y + 4 + score / 5
  if gem.y > 600:
    life = life - 1
  if gem.colliderect(ship):
    gem.x = random.randint(20, 780)
    gem.y = 0
    score = score + 1
  if life == 0:
    game_over = True

  gem1.y = gem1.y + 4 + score / 5
  if gem1.colliderect(ship):
    gem1.x = random.randint(20, 780)
    gem1.y = 0
    life = life - 1
  if life == 0:
    game_over = True

def draw():
  screen.fill((80,0,70))
  if game_over:
    screen.draw.text('Game Over', centerx=WIDTH/2, top=200, color=(255,255,255), fontsize=150)
    screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=320, color=(255,255,255), fontsize=50)
  else:
    gem.draw()
    gem1.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line