import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# def get_mouse_click_cor(x,y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_cor)

data = pandas.read_csv("50_states.csv")
# ny = data[data.state == "New York"]

states_list = data['state'].to_list()
# print(states_list)


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
if answer_state in states_list:
    state = data[data.state == answer_state]
    # turtle.goto(state.x, state.y)
    # turtle.write(state.state)
    print(state)

#An alternative to screen.exitonclick()
turtle.mainloop()
