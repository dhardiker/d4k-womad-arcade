# @name Amazing Example Game with Scores
# @author Orlando
import pgzrun
import sys
import random
import os
import time

WIDTH = 800
HEIGHT = 600

# Create a new flag to track the game state
start_screen = True
game_over = False
end_screen = False

# Create Actors for the start screen instructions
star_icon = Actor('star')
asteroid_icon = Actor('asteroid')
boost_icon = Actor('boost')
upgrade_icon = Actor('upgrade')  # New upgrade item

# Position the instruction icons
star_icon.x = 100
star_icon.y = 200

asteroid_icon.x = 100
asteroid_icon.y = 300

boost_icon.x = 100
boost_icon.y = 400

upgrade_icon.x = 100  # Initial position
upgrade_icon.y = 500  # Initial position

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('star')
gem.x = random.randint(20, 780)
gem.y = 0

speed_boost = Actor('boost')
speed_boost.x = random.randint(20, 780)
speed_boost.y = -1000  # Start off-screen

asteroid = Actor('asteroid')
asteroid.x = random.randint(20, 780)
asteroid.y = -1000  # Start off-screen

upgrade = Actor('upgrade')  # New upgrade item
upgrade.x = random.randint(20, 780)
upgrade.y = -1000  # Start off-screen

score = 0
highscore_saved = False  # New flag to track if highscore has been saved

HIGHSCORE_FILE = "highscores.txt"
highscores = []

speed_boost_active = False
speed_boost_end_time = 0
normal_speed = 5
boosted_speed = normal_speed * 1.5
speed_multiplier = 1.0  # New speed multiplier

def load_highscores():
    global highscores
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            highscores = [int(line.strip()) for line in file.readlines()]
    highscores = sorted(highscores, reverse=True)[:5]

def save_highscore(new_score):
    global highscores
    highscores.append(new_score)
    highscores.sort(reverse=True)
    highscores = highscores[:5]
    with open(HIGHSCORE_FILE, "w") as file:
        for score in highscores:
            file.write(f"{score}\n")

def restart_game():
    global start_screen, game_over, end_screen, score, highscore_saved
    global speed_boost_active, speed_boost_end_time, speed_multiplier
    start_screen = False
    game_over = False
    end_screen = False
    score = 0
    highscore_saved = False
    speed_boost_active = False
    speed_boost_end_time = 0
    speed_multiplier = 1.0
    gem.x = random.randint(20, 780)
    gem.y = 0
    speed_boost.x = random.randint(20, 780)
    speed_boost.y = -1000
    asteroid.x = random.randint(20, 780)
    asteroid.y = -1000
    upgrade.x = random.randint(20, 780)
    upgrade.y = -1000

def update():
    global score, game_over, highscore_saved, speed_boost_active, speed_boost_end_time
    global start_screen, end_screen, speed_multiplier

    if keyboard.escape:
        exit()
        sys.exit()

    if end_screen:
        if keyboard.up:
            restart_game()
        elif keyboard.escape:
            exit()
            sys.exit()
        return

    if start_screen:
        if keyboard.left or keyboard.right or keyboard.up or keyboard.down:
            start_screen = False
    else:
        speed = boosted_speed if speed_boost_active else normal_speed
        speed *= speed_multiplier  # Apply speed multiplier

        if keyboard.left:
            ship.x -= speed
        if keyboard.right:
            ship.x += speed

        gem.y += 4 + score / 5
        speed_boost.y += 4 + score / 5
        asteroid.y += 6 + score / 10
        upgrade.y += 4 + score / 5  # Make the upgrade move with the same speed as other items

        if gem.y > 600:
            game_over = True
            if not highscore_saved:
                save_highscore(score)
                highscore_saved = True
            end_screen = True

        if gem.colliderect(ship):
            gem.x = random.randint(20, 780)
            gem.y = 0
            score += 1

        if speed_boost.colliderect(ship):
            speed_boost.x = random.randint(20, 780)
            speed_boost.y = -1000
            speed_boost_active = True
            speed_boost_end_time = time.time() + 5

        if speed_boost_active and time.time() > speed_boost_end_time:
            speed_boost_active = False

        if upgrade.colliderect(ship):
            upgrade.x = random.randint(20, 780)
            upgrade.y = -1000
            speed_multiplier *= 1.1  # Increase speed multiplier by 10%

        if random.randint(1, 250) == 1 and speed_boost.y == -1000:
            speed_boost.x = random.randint(20, 780)
            speed_boost.y = 0

        if random.randint(1, 333) == 1 and upgrade.y == -1000:  # Randomly spawn upgrade item
            upgrade.x = random.randint(20, 780)
            upgrade.y = 0

        if asteroid.colliderect(ship):
            game_over = True
            if not highscore_saved:
                save_highscore(score)
                highscore_saved = True
            end_screen = True

        if asteroid.y > 600:
            asteroid.x = random.randint(20, 780)
            asteroid.y = -100

def draw():
    if start_screen:
        screen.fill((10, 40, 40))

        # Draw the start screen text
        screen.draw.text('Highscore: ' + str(max(highscores, default=0)), centerx=WIDTH/2, top=150, color=(255,255,255), fontsize=50)
        screen.draw.text('Move joystick or press arrow keys to start', centerx=WIDTH/2, top=10, color=(255,255,255), fontsize=30)
        
        # Draw the left column instructions
        star_icon.draw()
        screen.draw.text('Collect', (star_icon.x + 80, star_icon.y - 10), color=(255,255,255), fontsize=30)
        
        asteroid_icon.draw()
        screen.draw.text('Avoid', (asteroid_icon.x + 80, asteroid_icon.y - 10), color=(255,255,255), fontsize=30)
        
        boost_icon.draw()
        screen.draw.text('Speed Boost', (boost_icon.x + 80, boost_icon.y - 10), color=(255,255,255), fontsize=30)
        
        upgrade_icon.draw()  # Draw the new upgrade item
        screen.draw.text('Speed Upgrade', (upgrade_icon.x + 80, upgrade_icon.y - 10), color=(255,255,255), fontsize=30)
        
    elif end_screen:
        screen.fill((0, 0, 0))
        screen.draw.text('Game Over', centerx=WIDTH/2, top=150, color=(255,255,255), fontsize=100)
        screen.draw.text('Final Score: ' + str(score), centerx=WIDTH/2, top=300, color=(255,255,255), fontsize=50)
        screen.draw.text('Highscores:', centerx=WIDTH/2, top=400, color=(255,255,255), fontsize=50)
        for i, highscore in enumerate(highscores):
            screen.draw.text(f"{i+1}. {highscore}", centerx=WIDTH/2, top=450 + i*30, color=(255,255,255), fontsize=30)
        screen.draw.text('Press UP to restart or ESC to exit', centerx=WIDTH/2, top=10, color=(255,255,255), fontsize=30)
        
    else:
        screen.fill((40,0,35))
        gem.draw()
        ship.draw()
        speed_boost.draw()
        asteroid.draw()
        upgrade.draw()  # Draw the new upgrade item
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
        
        # Draw speed boost progress bar
        if speed_boost_active:
            remaining_time = speed_boost_end_time - time.time()
            bar_length = int((remaining_time / 5) * 100)
            screen.draw.filled_rect(Rect((15, 50), (bar_length, 20)), (0, 0, 255))
        
        # Display the current speed multiplier
        multiplier_color = (255, 165, 0) if speed_boost_active else (255, 255, 255)  # Orange if boost active
        screen.draw.text(f'Speed Multiplier: {speed_multiplier:.1f}x', (15, 80), color=multiplier_color, fontsize=20)

load_highscores()
pgzrun.go()