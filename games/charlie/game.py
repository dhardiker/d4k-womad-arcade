# @name Zombie Star Dodge
# @author Charlie

# Add rocks that the player must avoid, falling from the sky every 3-5 seconds
# Add a game over screen when the player collides with a rock or the countdown reaches 0

import pgzrun
import math
import random

WIDTH = 800
HEIGHT = 600

score = 0

countdown_frames = 300  # 60 frames per second == 5 seconds
countdown = countdown_frames

player = Actor('attack4')
player.x = 400
player.y = 545

star = Actor('star_gold')

def place_star():
  global countdown
  star.x = random.randint(20, 780)
  star.y = random.randint(20, 580)
  countdown = countdown_frames - ((score / 5) * 60)

place_star()

def update():
  global countdown
  countdown = countdown - 1
  if countdown == 0:
    exit()
  
  if keyboard.left and player.x > 45:
    player.x = player.x - 5
  if keyboard.right and player.x < 755:
    player.x = player.x + 5
  if keyboard.up and player.y > 50:
    player.y = player.y - 5
  if keyboard.down and player.y < 545:
    player.y = player.y + 5
  
  if player.colliderect(star):
    global score
    score = score + 1
    place_star()

def draw():
  screen.fill((0,102,102))
  screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
  screen.draw.text('Countdown: ' + str(math.ceil(countdown / 60)) + ' seconds', (15,40), color=(255,255,255), fontsize=30)
  star.draw()
  player.draw()

pgzrun.go() # Must be last line