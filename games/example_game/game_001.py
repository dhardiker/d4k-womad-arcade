import pgzrun

WIDTH = 800
HEIGHT = 600

def update():
  if keyboard.escape:
    exit()
    sys.exit()

pgzrun.go() # Must be last line