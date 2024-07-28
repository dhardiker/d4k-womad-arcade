import pgzrun
import random
import sys

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_orange')
ship.x = 370
ship.y = 550

gem = Actor('gemblue')
gem.x = random.randint(20, 780)
gem.y = 0

score = 0
game_over = False

def update():
  global score, game_over

  if keyboard.escape:
    exit()
    sys.exit()
  if keyboard.a:
    ship.x = ship.x - 7.5
  if keyboard.d:
    ship.x = ship.x + 7.5

  gem.y = gem.y + 4 + score / 5
  if gem.y > 600:
    game_over = True
  if gem.colliderect(ship):
    gem.x = random.randint(20, 780)
    gem.y = 0
    score = score + 1

fail_sentences= [
  'skill issue: sad',
  'take the lll',
]
fail_sentence = random.choice(fail_sentences)

def draw():
  screen.fill((164,0,44))
  if game_over:
    screen.draw.text (fail_sentence, centerx=WIDTH/2, top=200, color=(255,255,255), fontsize=150)
    screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=320, color=(255,255,255), fontsize=50)
  else:
    gem.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line