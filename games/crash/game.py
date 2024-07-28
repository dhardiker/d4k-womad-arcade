# @name Ruben and Lorcan's Arcade GAME
# @author Ruben & Lorcan
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
game_over = 3

def update():
  global score, game_over

  if keyboard.escape:
    exit()
    sys.exit()
  if keyboard.left:
    ship.x = ship.x - (5 + score/5)
  if keyboard.right:
    ship.x = ship.x + (5 + score/5)

  gem.y = gem.y + 4 + score / 5
  if gem.y > 600:
    game_over -= 1
    gem.y = 0
  if gem.colliderect(ship):
    gem.x = random.randint(20, 780)
    gem.y = 0
    score = score + 1

def flash():
  screen.fill((100,0,0))


def draw():
  screen.fill((0,0,100))
  if game_over == 0:
    screen.draw.text('Game Over', centerx=WIDTH/2, top=200, color=(255,255,255), fontsize=150)
    screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=320, color=(255,255,255), fontsize=50)
  else:
    gem.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
    screen.draw.text('Lives: ' + str(game_over), (710,10), color=(255,255,255), fontsize=30)



pgzrun.go() # Must be last line