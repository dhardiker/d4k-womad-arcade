import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen')
gem.x = 350
gem.y = 0

def update():
  if keyboard.left:
    ship.x = ship.x - 5
  if keyboard.right:
    ship.x = ship.x + 5

  gem.y = gem.y + 4
  if gem.y > 600:
    gem.y = 0
  if gem.colliderect(ship):
    gem.y = 0

def draw():
  screen.fill((80,0,70))
  gem.draw()
  ship.draw()

pgzrun.go() # Must be last line