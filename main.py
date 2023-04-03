import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



def get_mouse_click_cor(x,y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_cor)

#An alternative to screen.exitonclick()
turtle.mainloop()