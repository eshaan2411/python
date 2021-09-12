from flask import Flask
from flask.templating import render_template
import random
generated_num = random.choice([1,2,3,4,5,6,7,8,9])

app = Flask(__name__)

def align(function):
    def wrapper():
        return "<div style='text-align: center;'>" + function() + "</div>"
    return wrapper



@app.route('/')
@align
def home():
    return "<h1>Guess a number between 1-9</h1> " \
        "<img src='https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp'>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > generated_num:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < generated_num:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)
