# @name Name of my Amazing Example Game
# @author Jane & John Smith
import pgzrun
import sys
import random

WIDTH = 800
HEIGHT = 600
ROUND_MULTIPLIER = 1.05
SHIP_BOUNDARY = 10
GEM_BOUNDARY = 30
MAX_ROUND_SPEED = 20
BG_COLOUR = (80,0,70)
TEXT_COLOUR = (255, 255, 255)

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550
ship.speed = 5

gem = Actor('gemgreen')
gem.x = random.randint(GEM_BOUNDARY, WIDTH - GEM_BOUNDARY)
gem.y = 0
gem.speed = 3.6

asteroid = Actor('asteroid')
asteroid.scale = 3
asteroid.x = random.randint(GEM_BOUNDARY, WIDTH - GEM_BOUNDARY)
asteroid.y = -100
asteroid.speed_x = 0.3
asteroid.speed_y = 2
asteroid.dir = random.choice([-1, 1])

score = 0
game_over = False

def update():
  global score, game_over

  if keyboard.escape:
    exit()
    sys.exit()
  if keyboard.left:
    if ship.left > SHIP_BOUNDARY:
      ship.x = ship.x - ship.speed * ROUND_MULTIPLIER ** ((score + 1) if score < MAX_ROUND_SPEED else MAX_ROUND_SPEED)
  if keyboard.right:
    if ship.right < WIDTH - SHIP_BOUNDARY:
      ship.x = ship.x + ship.speed * ROUND_MULTIPLIER ** ((score + 1) if score < MAX_ROUND_SPEED else MAX_ROUND_SPEED)

  gem.y = gem.y + gem.speed * ROUND_MULTIPLIER ** ((score + 1) if score < MAX_ROUND_SPEED else MAX_ROUND_SPEED)
  #if gem.y > HEIGHT:
  #  game_over = True
  if gem.colliderect(ship):
    gem.x = random.randint(GEM_BOUNDARY, WIDTH - GEM_BOUNDARY)
    gem.y = 0
    score = score + 1

  if score > MAX_ROUND_SPEED:
    asteroid.x = asteroid.x + asteroid.speed_x * ROUND_MULTIPLIER ** ((score + 1) if score < MAX_ROUND_SPEED else MAX_ROUND_SPEED) * asteroid.dir
    asteroid.y = asteroid.y + asteroid.speed_y * ROUND_MULTIPLIER ** ((score + 1) if score < MAX_ROUND_SPEED else MAX_ROUND_SPEED)
    if asteroid.y > HEIGHT:
      asteroid.y = -100
      asteroid.dir = random.choice([-1, 1])
    if asteroid.colliderect(ship):
      game_over = True

def draw():
  screen.fill(BG_COLOUR)
  if game_over:
    screen.draw.text('Game Over', centerx=WIDTH/2, top=200, color=TEXT_COLOUR, fontsize=150)
    screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=320, color=TEXT_COLOUR, fontsize=50)
  else:
    gem.draw()
    asteroid.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=TEXT_COLOUR, fontsize=30)

pgzrun.go() # Must be last line