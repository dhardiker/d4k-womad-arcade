import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership3_green')
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

def draw():
  screen.fill((80,0,70))
  gem.draw()
  ship.draw()

  gem.y = gem.y +n4
  if gem.y > 600:
    gem.y = 0

pgzrun.go() # Must be last line