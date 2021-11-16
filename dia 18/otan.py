new_item = [1,2,3]
new_list=[n+1 for n in new_item]
print(new_list)

name = "Ramon"
new_name = [letter for letter in name]


new_range=[n*2 for n in range(1,5)]
print(new_range)


names = ["Ramon", "Beth", "Neto", "Dave", "stewie", "Fallen", "Coldzera"]
short_names = [name for name in names if len(name)<5 ]
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)

result = [n for n in numbers if n%2==0]
print(result)

with open ('file1.txt') as file1:
    file_1_data = file1.readlines()
with open ('file2.txt') as file2:
    file_2_data = file2.readlines()

result = [int(item) for item in file_1_data if item in file_2_data]
print(result)