# Python Asteroids

A classic arcade-style space shooter game built with Pygame where players navigate through an asteroid field while trying to survive and destroy incoming asteroids.

## 🎮 Gameplay

- Control a triangular spaceship through a field of asteroids
- Shoot asteroids to break them into smaller pieces
- Avoid colliding with asteroids
- The game gets progressively more challenging as asteroids continue to spawn

## 🕹️ Controls

- `W` - Move forward
- `S` - Move backward
- `A` - Rotate left
- `D` - Rotate right
- `SPACE` - Shoot

## 🚀 Features

- Smooth spaceship movement and rotation
- Asteroids split into smaller pieces when shot
- Progressive difficulty with continuous asteroid spawning
- Physics-based movement
- Collision detection
- Clean, vector-style graphics

## 🛠️ Prerequisites

- Python 3.x
- Pygame 2.6.1

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/armymp/asteroids
```

2. Navigate to the project directory:
```bash
cd python-asteroids
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the game:
```bash
python main.py
```

## 🏗️ Project Structure

- `main.py` - Game initialization and main loop
- `player.py` - Player spaceship class and controls  
- `asteroid.py` - Asteroid object implementation
- `asteroidfield.py` - Asteroid spawning and management
- `shot.py` - Projectile implementation
- `circleshape.py` - Base class for circular game objects
- `constants.py` - Game constants and configuration

## 🎯 Game Mechanics

### Player
- The player controls a triangular spaceship
- Movement is momentum-based
- Can shoot projectiles to destroy asteroids 
- Shooting has a cooldown period

### Asteroids
- Spawn from the edges of the screen
- Move in random directions
- Split into smaller pieces when hit
- Different sizes provide variety in gameplay

## 🤝 Contributing

Feel free to fork the project and submit pull requests with improvements or bug fixes.

## 📝 License


MIT License

Copyright (c) 2024 armymp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.