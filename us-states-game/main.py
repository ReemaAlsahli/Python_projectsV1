import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state = pandas.read_csv("50_states.csv")
list_state = state.state.to_list()
guess_state = []
count_state = 0
while len(guess_state) < 50:
    answer = turtle.textinput(title=f"{ len(guess_state)}/50 State current", prompt="what's another state name?").title()
    if answer == "Exit":
        missing_state = [ state for state in list_state if state not in guess_state ]
        # for state in list_state:
        #     if state not in guess_state:
        #         missing_state.append(state)
        data = pandas.DataFrame(missing_state)
        data.to_csv("missing_state")
        break

    elif answer in list_state:
        guess_state.append(answer)
        x = int(state[state.state == answer].x)
        y = int(state[state.state == answer].y)
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x, y)
        new_state.write(answer, font=("Arial", 12, "normal"))





screen.exitonclick()