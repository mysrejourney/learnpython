# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit" + " pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(2)

# -------------------------------------------------------------- #
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         total_likes = total_likes + 0
# print(total_likes)

# ---------------------------------------------------

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
# print(data)
""" Converting dataframe into dictionary by loop through all items in dataframe"""
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

""" phonetic_dict should look like this 
{'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie'}
"""
# print(phonetic_dict)

""" Get the user input word and convert them into upper case as phonetic_dict has key values as upper case """


def generate_phonetic():
    word = input("Enter your input word: ").upper()

    try:
        """ Loop through the word and get the corresponding value of phonetic_dict and save as a list """
        output_list = [phonetic_dict[item] for item in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()