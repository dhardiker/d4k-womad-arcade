import curses
import subprocess
import os

def get_game_files(game_path):
    # Search for files named "game.py" in the specified game path
    game_files = []
    for root, dirs, files in os.walk(game_path):
        for file in files:
            if file == "game.py":
                game_files.append(os.path.join(root, file))
    return game_files

def parse_game_metadata(game_file):
    name = "unknown"
    author = "unknown"
    try:
        with open(game_file, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    if '@name' in line:
                        name = line.split('@name', 1)[1].split(':', 1)[-1].strip()
                    elif '@author' in line:
                        author = line.split('@author', 1)[1].split(':', 1)[-1].strip()
                else:
                    break  # Stop reading after the comment block
    except Exception as e:
        pass
    return name, author

def launch_game(game_script):
    try:
        # Launch the game script in a separate process
        process = subprocess.Popen(["python", game_script])
        # Wait for the game process to complete
        process.wait()
    except Exception as e:
        pass

def main(stdscr, games):
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0
    visible_start = 0
    max_visible = 10

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        visible_end = min(visible_start + max_visible, len(games))
        for idx in range(visible_start, visible_end):
            game_path, game_display_name = games[idx]
            x = w // 2 - len(game_display_name) // 2
            y = h // 2 - (visible_end - visible_start) // 2 + (idx - visible_start)
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, game_display_name)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, game_display_name)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_row -= 1
            if current_row < 0:
                current_row = len(games) - 1
                visible_start = max(0, len(games) - max_visible)
            elif current_row < visible_start + max_visible // 2 and visible_start > 0:
                visible_start -= 1
        elif key == curses.KEY_DOWN:
            current_row += 1
            if current_row >= len(games):
                current_row = 0
                visible_start = 0
            elif current_row >= visible_start + max_visible // 2 and visible_start + max_visible < len(games):
                visible_start += 1
        elif key == ord(' '):
            game_script = games[current_row][0]
            stdscr.clear()
            stdscr.refresh()
            curses.endwin()
            launch_game(game_script)
            curses.wrapper(main, games)

if __name__ == "__main__":
    game_path = os.getenv("GAME_PATH")
    if game_path:
        games = get_game_files(game_path)
        if games:
            game_display_data = []
            for game_file in games:
                name, author = parse_game_metadata(game_file)
                dir_name = os.path.basename(os.path.dirname(game_file))
                display_name = f"{name} by {author} ({dir_name})"
                game_display_data.append((game_file, display_name))
            curses.wrapper(main, game_display_data)
        else:
            print("No games found in the specified GAME_PATH.")
    else:
        print("The environment variable GAME_PATH is not set.")
