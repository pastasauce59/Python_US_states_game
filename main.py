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
ny = data[data.state == "New York"]

states_list = data['state'].to_list()
x_list = data['x'].to_list()
y_list = data['y'].to_list()

correct_state_guesses = []
while len(correct_state_guesses) != 50:
    answer_state = screen.textinput(title=f"{len(correct_state_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state in states_list:
        state_index = states_list.index(answer_state)
        state_x_cor = x_list[state_index]
        state_y_cor = y_list[state_index]
        turtle.penup()
        turtle.write(answer_state, True)
        turtle.goto(-state_x_cor, -state_y_cor)
        correct_state_guesses.append(answer_state)

#An alternative to screen.exitonclick()
turtle.mainloop()
