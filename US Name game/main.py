import turtle
import pandas as pd
import timer

data = pd.read_csv('50_states.csv')
states = list(data.state)
x_coordinates = list(data.x.astype(float))
y_coordinates = list(data.y.astype(float))


screen = turtle.Screen()
screen.title("US: States Name Guess Quiz")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.hideturtle()
t.penup()

# Get inputs.
score = 0
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{score}/50 States Correct.", prompt="What's your guess?").title()
    if guess not in guessed_states:
        if guess == "Exit":
            break
        if guess in states:
            print("State found at index: ", states.index(guess))
            pos = states.index(guess)
            score+=1
            t.goto(x = x_coordinates[pos], y = y_coordinates[pos])
            t.write(guess)
            guessed_states.append(guess)         


# Informing player about the states he/she did not guess.
states_left = [i for i in states if i not in guessed_states]
print(states_left)

# Get the co-ordinates of the states. (Already collected in file named "50_states.csv")
# def click(x, y):
#     print(x, y)
# turtle.onscreenclick(click)
