
# Game Launcher

This script provides a terminal-based launcher for Pygame Zero games. It allows users to navigate through a list of available games using the keyboard, view game metadata, and launch the selected game. The script searches for `game.py` files within a directory specified by the `GAME_PATH` environment variable and displays game information extracted from comments within each `game.py` file (other files are ignored).

## Features

- Display a list of available games.
- Navigate the list using the up and down arrow keys.
- Highlight the currently selected game.
- Launch the selected game by pressing the space key.
- Automatically scroll through the list if there are more than 10 games.
- Wrap-around navigation: jump to the start of the list if navigating down from the last game and jump to the end of the list if navigating up from the first game.

## Game Metadata

The script extracts the following metadata from the comments at the top of each `game.py` file:

- `@name`: The name of the game.
- `@author`: The name of the author(s).

The display name for each game is formatted as:

```
{game-name} by {author} ({directory-name})
```

If the `@name` or `@author` tags are not found, "unknown" is used as the default value.

## Prerequisites

- Python 3.8
- Pygame Zero (`pip install pgzero`)
- Ensure the `curses` library is available (typically pre-installed on Unix-like systems)

## Usage

1. **Set the `GAME_PATH` Environment Variable**:

   Ensure the environment variable `GAME_PATH` is set to the directory containing your game directories. Each game directory should contain a `game.py` file.

   ```sh
   export GAME_PATH=/path/to/your/games
   ```

2. **Run the Launcher Script**:

   Execute the launcher script in a terminal:

   ```sh
   python launcher.py
   ```

3. **Navigate and Launch Games**:

   - Use the up and down arrow keys to navigate through the list of games.
   - The currently selected game will be highlighted.
   - Press the select button ('a' on the keyboard) to launch the selected game.
   - Once you exit the game, the launcher will reappear.

## Example Directory Structure

```
/path/to/your/games/
    ├── game1/
    │   └── game.py
    ├── game2/
    │   └── game.py
    └── game3/
        └── game.py
```

Each `game.py` file should contain comments with metadata tags (if available) like:

```python
# @name: Example Game
# @author: John Doe

import pgzrun

# Game code here...

pgzrun.go()
```

## Auto Start on Raspberry Pi OS

Use `raspi-config` to automatically login to the console, and then add the following to the `.bashrc`.

**Note: you probably want to change `/home/dhardiker/...` to the correct path**

```sh
# Add this script to your /home/dhardiker/.bashrc
# Start the D4K WOMAD Arcade Game Launcher
if [[ "$XDG_VTNR" == "1" && -z "$SSH_CONNECTION" ]]; then
    GAME_PATH=/home/dhardiker/d4k-womad-arcade/games python /home/dhardiker/d4k-womad-arcade/launcher/launcher.py
fi
```

The script should only run on TTY1 (the auto logged in TTY) and not any others you can get to with `Ctrl + Alt + F2` etc.
The script should not run over SSH connections.

## Notes

- The script assumes each game is in its own directory and the main game script is named `game.py`.
- The launcher dynamically finds, parses, and lists all `game.py` scripts within the specified `GAME_PATH` directory, displaying the game name and author if available.
