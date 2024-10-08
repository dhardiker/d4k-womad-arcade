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

gem = Actor('gemgreen')
gem_images = ['gemblue', 'gemgreen', 'gemred', 'gemyellow']
gem.images = gem_images
gem.x = random.randint(20, 780)
gem.y = 0

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

  gem.y = gem.y + 4 + score / 5
  if gem.y > 600:
    game_over = True
  if gem.colliderect(ship):
  
    gem.x = random.randint(20, 780)
    gem.y = 0
    if gem.image == 'gemblue':
      score = score + 1
    elif gem.image == 'gemgreen':
      score = score + 2
    elif gem.image == 'gemred':
      score = score + 3
    elif gem.image == 'gemyellow':
      score = score + 4
    gem.image = random.choice(gem_images)

def draw():
  screen.fill((80,0,70))
  if game_over:
    screen.draw.text('Game Over', centerx=WIDTH/2, top=200, color=(255,255,255), fontsize=150)
    screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=320, color=(255,255,255), fontsize=50)
  else:
    gem.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line