# Tic-Tac-Toe Game with AI Bot

## Overview
This is a simple Tic-Tac-Toe game implemented in Python using the Tkinter library. The game allows two players to take turns making moves on a 3x3 board. Additionally, there is an AI bot available that follows the min-max algorithm to play against the user.

## Requirements
- Python 3.x
- Tkinter (usually included in standard Python installations)

## Setup:

1. Create a virtual environment using the latest release of virtualenv:

``` bash
> pip install virtualenv --upgrade
> virtualenv venv
```

_If there are problems with installing tkinter:_
- Install tkinter package. Ex: Homebrew:
``` bash
> brew install python-tk
```
- Then create the virtual environment as follows:
```
> virtualenv venv --system-site-packages
```

2. Access the virtual environment `./venv`
``` bash
> source ./venv/bin/activate
```

## Features
- **Player vs Player Mode:** Two players can take turns making moves.
- **Player vs AI Bot Mode:** The AI bot uses the minimax algorithm to make intelligent moves.
- **Interactive GUI:** The game features a graphical user interface with clickable cells on the board.
- **Winner Detection:** The game detects and announces the winner or a tie.

## AI Bot (MinMax Algorithm)
The AI bot uses the min-max algorithm to determine the best move. The algorithm recursively explores all possible moves to find the optimal strategy for both players. The AI assigns scores to each possible move and selects the move with the highest score when playing as 'O'. When playing as 'X', it selects the move with the lowest score.

## How to Play 
1. Choose the game mode in `./settings.json`:
```json
{
    "activateBot" : true
}
```
2. Run the script using the command: `python main.py`.
3. Click on an empty cell to make a move.
4. The game will detect and announce the winner or a tie.

## AI Bot Implementation (`ai_bot.py`)
The `ai_bot.py` file contains the implementation of the AI bot using the min-max algorithm. The `XO_bot` class in this file provides methods for making moves and evaluating the game state.

Feel free to explore the code, experiment with different strategies, or enhance the game with additional features. Enjoy playing Tic-Tac-Toe against your friend or challenge the AI bot!
