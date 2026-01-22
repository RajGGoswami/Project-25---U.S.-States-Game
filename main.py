# Day 25 - U.S. States Game
# An interactive geography quiz that places correctly guessed
# U.S. states directly onto a map using Turtle graphics and Pandas.

import turtle
import pandas as pd

# Font configuration for rendering state names on the map
FONT = ("Arial", 8, "normal")

# ----------------------------
# Screen & UI setup
# ----------------------------

# Create the main game window
screen = turtle.Screen()
screen.title("Raj's US States Game")

# Load and display the U.S. map image as the background
image = "state.gif"
screen.bgpic(image)

# Configure the turtle used only for writing state names
# (no drawing paths or animations)
turtle.penup()
turtle.ht()

# --------------------------------------------------
# Developer utility (commented out)
# Used during setup to capture x/y coordinates
# for each state when creating the CSV file
# --------------------------------------------------
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# ----------------------------
# Game state tracking
# ----------------------------

# Stores all states correctly guessed by the user
guessed_states = []

# Load state names and their x/y map coordinates
data = pd.read_csv("50_states.csv")

# Convert state column into a list for fast membership checks
state_list = data['state'].to_list()

# ----------------------------
# Main game loop
# ----------------------------
# Continues until all 50 states are guessed
while len(guessed_states) < 50:

    # Prompt the user for a state name and normalize capitalization
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Guess another state's name?"
    ).title()

    # Exit condition:
    # - Stops the game
    # - Generates a CSV file listing unguessed states
    if answer_state == "Exit":
        missed_states = [
            state for state in state_list
            if state not in guessed_states
        ]
        states_to_learn = pd.DataFrame(missed_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    # Process valid guesses only:
    # - Must be a real state
    # - Must not already be guessed
    if answer_state not in guessed_states and answer_state in state_list:
        guessed_states.append(answer_state)

        # Look up the map coordinates for the guessed state
        state_data = data[data["state"] == answer_state]

        # Move the turtle to the state's position and label it
        turtle.goto(
            int(state_data.x.item()),
            int(state_data.y.item())
        )
        turtle.write(answer_state, align="center", font=FONT)

# Keep the window open until the user clicks
screen.exitonclick()
