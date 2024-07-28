import pgzrun
import random
import sys

WIDTH = 800
HEIGHT = 600

ship_images = ['playership1_blue', 'playership1_green', 'playership1_orange', 'playership1_red']
ship_image_selected = False
ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = random.randint(20, 780)
gem.y = 0

score = 0
game_over = False

def update():
  global score, game_over, ship_image_selected

  if keyboard.escape:
    exit()
    sys.exit()
  if keyboard.up:
    current_ship_image_index = ship_images.index(ship.image)
    previous_ship_image_index = current_ship_image_index - 1 if current_ship_image_index > 0 else len(ship_images) - 1
    ship.image = ship_images[previous_ship_image_index]
  if keyboard.down:
    current_ship_image_index = ship_images.index(ship.image)
    next_ship_image_index = current_ship_image_index + 1 if current_ship_image_index < len(ship_images) - 1 else 0
    ship.image = ship_images[next_ship_image_index]
  # The button labelled 'select' on the arcade machine is mapped to 'a' on our keyboard
  if keyboard.a:
    ship_image_selected = True
    gem.y = 0
    score = 0
    game_over = False

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
    score = score + 1

def draw():
  screen.fill((80,0,70))
  if not ship_image_selected:
    screen.draw.text('Select your spaceship image', centerx=WIDTH/2, top=200, color=(255,255,255), fontsize=50)
    screen.draw.text('<up & down to change / select to choose>', centerx=WIDTH/2, top=250, color=(255,255,255), fontsize=30)
    ship.draw()
  elif game_over:
    screen.draw.text('Game Over', centerx=WIDTH/2, top=200, color=(255,255,255), fontsize=150)
    screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=320, color=(255,255,255), fontsize=50)
  else:
    gem.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line