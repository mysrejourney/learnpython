""" Importing required module """
import pandas
""" Converting CSV to Pandas Dataframe"""
data = pandas.read_csv("nato_phonetic_alphabet.csv")
""" data should look like this 
   letter      code
0       A      Alfa
1       B     Bravo
2       C   Charlie
"""
print(data)
""" Converting dataframe into dictionary by loop through all items in dataframe"""
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

""" phonetic_dict should look like this 
{'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie'}
"""
print(phonetic_dict)

""" Get the user input word and convert them into upper case as phonetic_dict has key values as upper case """
word = input("Enter your input word: ").upper()

""" Loop through the word and get the corresponding value of phonetic_dict and save as a list """
output_list = [phonetic_dict[item] for item in word]
print(output_list)

