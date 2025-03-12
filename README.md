# Catch the Falling Objects Game

## Overview
"Catch the Falling Objects" is a simple 2D game built using Python and the Pygame library. The goal of the game is to control a basket (represented by a blue rectangle) to catch falling red blocks while avoiding to miss them. Every time the player catches a block, their score increases. If the player misses 5 blocks, the game ends.

## Features
- **Player Movement**: Use the left and right arrow keys to move the basket.
- **Falling Objects**: Red blocks fall from the top, and the player must catch them.
- **Score System**: Catching a block increases the score.
- **Game Over Condition**: If 5 blocks are missed, the game ends and shows a "Game Over" screen.
- **Difficulty Increase**: The speed of the falling objects increases as the player's score grows.

## Requirements
- Python 3.x
- Pygame Library

### Installing Pygame
If you don't have the Pygame library installed, you can install it using pip:

```bash
pip install pygame
