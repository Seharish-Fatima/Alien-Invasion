# 👾 Alien Invasion — BT21 vs. The Universe 👾

> A full-screen cosmic arcade shooter built in Python with the power of `pygame` and the aesthetic of intergalactic chaos.  
> Because saving Earth is basic. We’re saving the whole galaxy, baby.

---

## 🌟 What is Alien Invasion?

**Alien Invasion** is a nostalgic-yet-modern arcade-style shooter where you pilot a BT21 spaceship, fend off waves of aliens, and protect space from _utter doom_. It’s got bullets, fleets, scoreboards, and that sweet sweet “press play and vibe” energy.

Think:  
`Space Invaders + Python + BTS BT21 aesthetics = ✨ Peak Gaming ✨`

---

## 🚀 Features

- 🎮 Fullscreen gameplay with smooth `pygame` rendering
- 🛸 Endless waves of aliens trying to invade your sanity
- 🧠 Game state tracking (lives, scores, high score, game over logic)
- 🔫 Pew-pew bullet shooting action!
- 📈 Scoreboard with high-score tracking
- 🧪 Modular game design (OOP heaven)

---

## 🧩 Project Structure

Here's the cosmic control center breakdown:

```plaintext
Alien-Invasion/
│
├── main.py              # The Big Boss. Runs the whole game.
├── settings.py          # Game settings and tuning.
├── game_stats.py        # Tracking scores, lives, and game state.
├── scoreboard.py        # Displays your glorious space achievements.
├── button.py            # Handles the 'Play' button.
│
├── ship.py              # The BT21 spaceship. You are the captain now.
├── alien.py             # The enemies. Many. Angry. Green.
├── bt21.py              # Support visuals from the BT21 universe.
├── bullet.py            # Your weapon of cosmic destruction.
│
├── assets/              # Visuals (alien.bmp, ship.bmp, bt21.bmp, etc.)
└── README.md            # This glorious file.
```

## 🎮 How to Play

Before you dive in, make sure `pygame` is installed:

```bash
pip install pygame
```

# 🔥 Launch the Game

```bash
python main.py
```

## 🕹 Controls

- **← / →**: Move the BT21 spaceship left or right
- **SPACE**: Fire bullets (pew! pew!)
- **Q**: Quit the game (coward)

---

## 📊 Gameplay Mechanics

- **Game Loop**: Run via `main.py` inside a `while True:` loop that checks for input, updates objects, redraws screen. Smooth AF.
- **Alien Fleet**: Generated in a grid layout using `_create_fleet()` method. They descend... slowly but surely.
- **Bullet Firing**: Hit spacebar, and `Bullet` objects are added to a `pygame.sprite.Group()`.
- **Collisions**: If bullet meets alien, both go _bye-bye_ and your score goes _zoom-zoom_.
- **Lives**: You get 3. After that? Game over. Rage restart optional.

---

## 💅 Behind the Code (aka BTS but for Python devs)

- `Settings` class: Handles screen size, speed factors, ship limits, and more.
- `Ship` class: Draws + updates the player's ship. Handles movement.
- `Alien` class: Enemy logic — they march left-right-down like determined ants.
- `GameStats`: Tracks lives and whether game is active.
- `Scoreboard`: Because flexing your high score is a gamer’s right.

---

## ✨ BT21 Integration

This isn’t just your boring vanilla alien shooter.  
We got **Chimmy**. We got **Tata**.  
The BT21 family makes a cameo in the visual assets, loading your cosmic journey with cuteness and chaos.

---

## 🧠 Fun Facts

- **Fullscreen Mode**: Set with `pygame.display.set_mode((0,0), pygame.FULLSCREEN)`
- **Frame Rate**: Managed by `pygame.time.Clock()` — buttery smooth.
- **Aliens** don’t just go down. They multiply and adapt. Good luck.

---

## 💻 Requirements

- Python 3.x
- `pygame`

---

## 🤖 Future Upgrades (If You Wanna Go Pro)

- Power-ups & boss aliens
- Sound effects & background music
- Leaderboard system with JSON save
- Mobile controls via Kivy (if you're wild)
- Online multiplayer (bless your soul if you try)

---

## 🛸 Final Thoughts

This isn't just a project. It's a galactic **experience**.  
Built with code, chaos, and just a little too much coffee.  
Now go forth and **save the universe** — one alien at a time. 💥🌌

> “We don’t play games. We build universes.” — _Sash_

---

## 🧁 Credits

- Made with 💜 by **Seharish Fatima**
