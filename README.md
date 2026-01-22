# Project-25---U.S.-States-Game

This project is a U.S. geography guessing game where users attempt to name all 50 states.

Each correct answer is rendered directly onto a U.S. map, reinforcing visual learning.

**Purpose of the Project**

This project was designed to:

Combine data-driven logic (Pandas) with visual UI (Turtle)

Practice working with CSV datasets

Reinforce user input validation

Create an interactive educational experience

Introduce learning feedback via exported data

**How the Game Works**

A U.S. map image is displayed as the background

The user is prompted to guess a state name

If the guess is correct:

The state name is written at its correct map location

The score increments

If the user types Exit:

A CSV file (states_to_learn.csv) is generated

The file contains all states not yet guessed

The game ends when all 50 states are guessed or the user exits

**Key Concepts Practiced**

Turtle graphics positioning and text rendering

Pandas DataFrame filtering

List comprehensions for comparison logic

Normalizing user input (.title())

File output for learning reinforcement

**File Structure**

├── main.py              # Main game loop, user input handling, and state validation

├── 50_states.csv        # Dataset containing U.S. state names with x/y map coordinates

├── state.gif            # Background image of the U.S. map used by Turtle

├── states_to_learn.csv  # Auto-generated list of states not guessed before exiting

**Design Decisions**

CSV-driven coordinates keep logic clean and scalable

Turtle handles only rendering, not data logic

Missed states are exported instead of just ending the game

Minimal UI keeps focus on learning
