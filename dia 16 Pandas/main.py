import pandas as pd
import numpy as np

data = pd.read_csv("weather.csv")
temperature=[]
temperature.append(data["temp"])
#print(temperature)

data_dict = data.to_dict()
#print(data.to_dict())
#print (data_dict['temp'])

temp_list = data["temp"].to_list()
s=sum(temp_list)/len(temp_list) #Manipulação utilizando propriedades do python
media = np.mean(temp_list) #Utilizando Numpy
pd_media = data["temp"].mean() #Utilizando series
pd_max = data["temp"].max() #Valor máximo da coluna Temperatura
#print(f"Media da temperatura de todos os dias é: {pd_media}")
#print(f"Máxima da temperatura de todos os dias é: {pd_max}")

condition = data["condition"]
#print(data.condition)

#Data in row
#print (data[data.day == "Monday"]) 

print (data[data.temp == max(data.temp)]) #Challenge
print (data[data.temp == data.temp.max()]) #Challenge

monday = data[data.day == "Monday"]
print (f"Fahrenheit: {monday.temp*9/5+32}")

#Create DF

dict_new = {"students":["AMY","sissok","Angela"],
    "scores":[76,56,65]
}
df = pd.DataFrame(dict_new)
df.to_csv("novo_csv.csv")
print(df)

squirrel = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_hectare = squirrel.Hectare
make=pd.DataFrame(squirrel_hectare)

