import turtle
import pandas

# # Returns Coordinates of Textbox
# def get_mouse_click_cor(x, y):
#     print(x, y)


# Creates Screen and Background Image
screen = turtle.Screen()
screen.title("Best Foreign 11 In Fenerbahce History ")
screen.addshape("fenerbahce-best-foreign-11.gif")

turtle.shape("fenerbahce-best-foreign-11.gif")

# # Detects Coordinates of Textbox
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

# Reads Dataset
dataset = pandas.read_csv("players.csv")

# Pulls players name to list
players = dataset.name.to_list()

# To Store Correct Answers
correct_answer = []

# Prompts User for Guessing 11 Times
while len(correct_answer) < 11:
    answer = screen.textinput(title=f"{len(correct_answer)}/11", prompt="What's the name of the player?").title()

    if answer == "exit" or answer == "Exit":
        unknowns_data = [player for player in players if player not in correct_answer]

        players_to_learn = pandas.DataFrame(unknowns_data)
        players_to_learn.to_csv("players_to_learn.csv")
        break

    if answer in players:
        correct_answer.append(answer)
        data = dataset[dataset.name == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data.x), int(data.y))
        t.write(answer, font=('Arial', 16, 'normal'), align="left")

screen.exitonclick()
