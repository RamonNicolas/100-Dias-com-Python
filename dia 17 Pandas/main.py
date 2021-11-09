import pandas as pd
import numpy as np

data = pd.read_csv("weather.csv")
temperature = []
temperature.append(data["temp"])
# print(temperature)

data_dict = data.to_dict()
# print(data.to_dict())
#print (data_dict['temp'])

temp_list = data["temp"].to_list()
# Manipulação utilizando propriedades do python
s = sum(temp_list)/len(temp_list)
media = np.mean(temp_list)  # Utilizando Numpy
pd_media = data["temp"].mean()  # Utilizando series
pd_max = data["temp"].max()  # Valor máximo da coluna Temperatura
#print(f"Media da temperatura de todos os dias é: {pd_media}")
#print(f"Máxima da temperatura de todos os dias é: {pd_max}")

condition = data["condition"]
# print(data.condition)

#Data in row
#print (data[data.day == "Monday"])

# print (data[data.temp == max(data.temp)]) #Challenge
# print (data[data.temp == data.temp.max()]) #Challenge
#
#monday = data[data.day == "Monday"]
#print (f"Fahrenheit: {monday.temp*9/5+32}")
#
# Create DF
#
# dict_new = {"students":["AMY","sissok","Angela"],
#    "scores":[76,56,65]
# }
#df = pd.DataFrame(dict_new)
# df.to_csv("novo_csv.csv")
# print(df)

#squirrel = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#grey = len(squirrel[squirrel["Primary Fur Color"] == "Gray"])
#Cinnamon = len(squirrel[squirrel["Primary Fur Color"] == "Cinnamon"])
#Black = len(squirrel[squirrel["Primary Fur Color"] == "Black"])
#
#print(grey, Black, Cinnamon)
#
#data_dict = {
#    "Fur Color": ["Gray", "Cinnamon", "Black"],
#    "Count": [grey, Cinnamon, Black]
#}
#df = pd.DataFrame(data_dict)
#df.to_csv('Squirels.csv')

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)