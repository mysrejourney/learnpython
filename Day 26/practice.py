# numbers = [2, 4, 6, 8, 9]
# new_odd_numbers = [item for item in numbers if item % 2 == 0]
# print(new_odd_numbers)
#
# name = "Satheesh Pandian"
# new_name = [item for item in name]
# print(new_name)

# numbers = [item * 2 for item in range(1, 5)]
# print(numbers)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_name = [item.upper() for item in names if len(item)  > 4 ]
# print(new_name)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)
#
# with open("file1.txt") as file1:
#     data = file1.readlines()
#     print(data)
# with open("file2.txt") as file2:
#     data1 = file2.readlines()
#     print(data1)
#
# new_list  = [int(item) for item in data if item in data1]
# print(new_list)
#
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_score = {student:random.randint(1, 100) for student in names}
# print(student_score)
# # for (key,value) in student_score.items():
# #     print(key)
# #     print(value)
# passed_student = {key:value for (key,value) in student_score.items() if value > 60}
# print(passed_student)


# # sentence = "What is the Airspeed Velocity of an Unladen Swallow"
# sentence = "What"
# print(sentence.split())
# sentence_length = {item:len(item) for item in sentence.split()}
# print(sentence_length)
# weather_c = {
#     "Monday" : 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
# print(weather_f)

student_dict = {
    "student": "Satheesh",
    "score": 90
}

for (key, value) in student_dict.items():
    print(key, value)
    # print(value)
# import pandas
# new_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
# # print(new_dict)
#
# # for (key, value) in new_dict.items():
# #     print(value)
#
# for(index, row) in new_dict.iterrows():
#     print(row.letter, row.code)