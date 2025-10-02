# 2048 Game in Python with Pygame

This project is an implementation of the classic 2048 puzzle game using Python and Pygame.  
It demonstrates grid-based game logic, keyboard event handling, and graphical rendering.

<img width="448" height="527" alt="image" src="https://github.com/user-attachments/assets/febed523-6288-447b-a445-34fd920ce6fc" />
<img width="447" height="536" alt="image" src="https://github.com/user-attachments/assets/999b27e0-f4fb-43a8-8e65-6a865a7e10e5" />



---

## Features

- 4x4 grid with smooth tile rendering
- Random spawning of 2 and 4 tiles
- Tile merging mechanics (left, right, up, down)
- Score tracking
- Game over detection

---

## Project Structure

```
2048-pygame/
├── game.py          # game logic (grid, moves, merging, score)
├── gui.py           # graphical interface with Pygame
├── main.py          # entry point
├── requirements.txt # dependencies
└── README.md        # documentation
```

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/VictorGauthier123/2048_PYGAME.git
cd 2048_pygame
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
pygame
```

---

## Usage

Run the game with:

```bash
python main.py
```

Controls:
- Arrow keys (Up, Down, Left, Right) to move tiles.

The game ends when no more moves are possible.




