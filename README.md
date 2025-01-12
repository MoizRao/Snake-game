# Python Snake Game 🐍

A classic Snake arcade game implementation using Python and Pygame. The game features smooth controls, progressive difficulty, and object-oriented design.

## Overview

This Snake game puts players in control of a growing snake that must eat food while avoiding collisions with walls and itself. The game progressively becomes more challenging as your score increases, with the snake moving faster after each successful food collection.

## Features

- Smooth snake movement and controls
- Progressive difficulty scaling
- Score tracking
- Collision detection (walls and self)
- Pause functionality
- Custom graphics for snake and food
- Semi-transparent background
- Game over display with final score

## Technical Implementation

### Dependencies
- Python 3.x
- Pygame module

### Object-Oriented Design
The game implements two main classes:
- `Snake`: Manages snake properties and behavior
  - Movement logic
  - Body growth
  - Self-collision detection
  - Direction control
  
- `Game`: Controls game state and rendering
  - Game loop management
  - Food generation
  - Score tracking
  - Display handling
  - Event processing

### Required Files
- `block.png`: Snake body segment image
- `ball.png`: Food item image
- `snake_bg.jpg`: Background image

## Controls

- **Arrow Keys**: Control snake direction
  - ↑: Move Up
  - ↓: Move Down
  - ←: Move Left
  - →: Move Right
- **P**: Pause game
- **C**: Continue game when paused
- **ESC**: Exit game

## Game Mechanics

1. Snake starts with initial length of 10 segments
2. Each food item eaten:
   - Increases score by 1 point
   - Adds 3 segments to snake length
   - Slightly increases game speed
3. Game ends if snake:
   - Hits the walls
   - Collides with itself

## Installation & Running

1. Ensure Python 3.x is installed
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Place required image files in game directory
4. Run the game:
   ```bash
   python main.py
   ```

## Technical Features

- Property decorators for direction control
- Array manipulation for snake movement
- Random food placement with collision checking
- Dynamic speed adjustment based on score
- Custom collision detection algorithms
- Event-driven input handling
