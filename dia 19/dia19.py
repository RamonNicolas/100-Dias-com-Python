# Dictionay Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items}
# new_dict = {new_key:new_value for (key,value) in dict.items if test}
import random

names = ["Ramon", "Beth", "Neto", "Dave", "stewie", "Fallen", "Coldzera"]
student_score = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (
    student, score) in student_score.items() if score >= 60}
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)
#Celsius to Fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 35,
    "Wednesday": 15,
    "Thursday": 5,
    "Friday": 22,
    "Saturday": 22,
    "Sunday": 29,
}

weather_f = {day: (temp*9/5)+32 for (day, temp) in weather_c.items()}
print(weather_f)

#short_names = [name for name in names if len(name)<5 ]
#long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)
#
#numbers = [1,1,2,3,5,8,13,21,34,55]
#squared_numbers = [n*n for n in numbers]
# print(squared_numbers)
#
#result = [n for n in numbers if n%2==0]
# print(result)
#
# with open ('file1.txt') as file1:
#    file_1_data = file1.readlines()
# with open ('file2.txt') as file2:
#    file_2_data = file2.readlines()
#
#result = [int(item) for item in file_1_data if item in file_2_data]
# print(result)

#new_item = [1,2,3]
#new_list=[n+1 for n in new_item]
# print(new_list)
#
#name = "Ramon"
#new_name = [letter for letter in name]
#
#
#new_range=[n*2 for n in range(1,5)]
# print(new_range)
