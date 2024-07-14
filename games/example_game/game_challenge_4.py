import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem_images = ['gemblue', 'gemgreen', 'gemyellow', 'gemred']
gems = []
gem_ticks = 0
gem_creation_rate = 30   # 60 frames = 1 second

score = 0
lives = 3   # Need to switch to lives because we have multiple gems

def update():
  global score, lives, gem_ticks

  gem_ticks = gem_ticks + 1
  if gem_ticks % gem_creation_rate == 0:  # % is the modulus operator, it returns the remainder of the division
    gem_ticks = 0
    gem = Actor(random.choice(gem_images))
    gem.x = random.randint(20, 780)
    gem.y = 0
    gems.append(gem)

  if keyboard.left:
    ship.x = ship.x - 10   # Speed up the ship because we have multiple gems
  if keyboard.right:
    ship.x = ship.x + 10   # Speed up the ship because we have multiple gems

  for gem in gems:    
    gem.y = gem.y + 4 + score / 5 
    if gem.y > 600:
      gems.remove(gem)
      lives = lives - 1
    if gem.colliderect(ship):
      gems.remove(gem)
      score = score + 1

def draw():
  screen.fill((80,0,70))
  if lives <= 0:
    screen.draw.text('Game Over', centerx=WIDTH/2, top=200, color=(255,255,255), fontsize=150)
    screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=320, color=(255,255,255), fontsize=50)
  else:
    for gem in gems:
      gem.draw()
    ship.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
    screen.draw.text('Lives: ' + str(lives), (15,35), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line