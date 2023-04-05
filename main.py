import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_cor(x,y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_cor)

data = pandas.read_csv("50_states.csv")

states_list = data['state'].to_list()

correct_state_guesses = []
while len(correct_state_guesses) != 50:
    answer_state = screen.textinput(title=f"{len(correct_state_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        # states_to_learn = []
        # for state in states_list:
        #     if state not in correct_state_guesses:
        #         states_to_learn.append(state)
        # states_to_learn_data = pandas.DataFrame(states_to_learn)
        # states_to_learn_data.to_csv("states_to_learn.csv")
        states_to_learn = [state for state in states_list if state not in correct_state_guesses]
        print(states_to_learn)
        break
    if answer_state in states_list:
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        #if wanting to use state_data instead of answer_state for state's name
        # t.write(state_data.state.item())
        t.write(answer_state)
        correct_state_guesses.append(answer_state)
