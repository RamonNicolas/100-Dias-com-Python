student_dict = {
    "student":["Ramon", "Beth", "Neto"],
    "score": [56,99,78]
}
#Loop in dicts
#for (key,value) in student_dict.items():
#        print(value)

import  pandas as pd

student_df = pd.DataFrame(student_dict)
print(student_df)

#Loop rows of a data frame
for (index,row) in student_df.iterrows():
    if row.score > 60:
        print(f"This student {row.student} your note is {row.score}, you're aproved")
    else:
        print(f"This student {row.student}, you're not aproved")


nato = pd.read_csv('nato_phonetic_alphabet.csv')


print(nato.to_dict())
phonetic = {row.letter:row.code for (index,row) in nato.iterrows()}
print(phonetic)
name = input('Digite seu nome').upper()
name_phonetic = [phonetic[letter] for letter in name ]
print(name_phonetic)