# Balloon Pop Lab 4

## GITHUB REPOSITORY LINK FOR UPDATED CODE: 
https://github.com/BHOGALA-SRIKA/05_balloon_pop

## CHAT HISTORY LINK :
https://chatgpt.com/share/6ad0b75f-fd80-83e8-a476-bba3e906d2ad


## Project Overview

Balloon Pop is a Python game developed using Pygame. The player earns points by popping balloons before they escape from the screen. The game includes different balloon types, a lives system, a countdown timer, and a restart option.

## Features Implemented

### Task 1: Fix Balloon Click Detection
- Corrected the click-detection logic to compare the squared distance between the mouse click and the balloon's center against the squared radius.
- Clicking within a balloon's boundary correctly detects a hit.

### Task 2: Different Balloon Types
- Implemented normal, bonus, and penalty balloons.
- Different balloon types have distinct colors and scoring effects.
- Normal balloons award points, bonus balloons award additional points, and penalty balloons deduct points when popped.

### Task 3: Lives and Missed Balloons
- Implemented a three-life system.
- Missing a normal or bonus balloon costs one life.
- Missing a penalty balloon does not cost a life.
- Popping a penalty balloon deducts points but does not consume a life.

### Task 4: Timer and Restart
- Added a 30-second countdown timer.
- The game ends when the timer reaches zero or the player loses all lives.
- The final score is displayed when the game ends.
- Restarting begins a new round with the score, lives, and timer reset.

## Technologies Used

- Python
- Pygame

## How to Run

1. Clone or download this repository.
2. Open a terminal in the `balloon-pop` directory.
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the game:

   ```bash
   python main.py
   ```

## Project Structure

```text
05_balloon_pop/
├── README.md
└── balloon-pop/
    ├── main.py
    ├── requirements.txt
    └── game/
        ├── __init__.py
        ├── balloon.py
        ├── click_detection.py
        ├── game_engine.py
        └── renderer.py
```

## Submission Evidence

- Before-fix recording: https://github.com/BHOGALA-SRIKA/SE_LAB/blob/main/Lab4/before.mp4
- After-fix recording: https://github.com/BHOGALA-SRIKA/SE_LAB/blob/main/Lab4/after.mp4
- Chat/LLM history: https://github.com/BHOGALA-SRIKA/SE_LAB/blob/main/Lab4/SE%20Lab%204%20VibeCoding%20-%20Chat%20History%20(%20Balloon%20Pop).pdf

