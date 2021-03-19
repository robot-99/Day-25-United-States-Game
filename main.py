import turtle
import pandas
from pandas import DataFrame

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
# score = 0
guessed_states = []

data = pandas.read_csv("./50_states.csv")
all_states = data.state.tolist()

while len(guessed_states) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="Guess a state").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        penbooi = turtle.Turtle()
        penbooi.hideturtle()
        penbooi.penup()
        state_data = data[data.state == answer_state]
        penbooi.goto(int(state_data.x), int(state_data.y))
        penbooi.write(answer_state)
# states to learn

states_to_learn = [set(all_states) - set(guessed_states)]
homework = DataFrame(states_to_learn, columns=['state'])
homework.to_csv('./states_to_learn.csv')
