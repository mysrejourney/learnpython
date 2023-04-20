# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temp = []
#     for row in data:
#         # print(row)
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#
#     print(temp)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))
# print(f"Average of temp is {sum(temp_list) / len(temp_list)}")
# print(data["temp"].max())

#Get the column

# print(data["weather"])
# print(data.weather)

# Get rows
# print(data[data.day == "Monday"])
# print(data[data.temp.max() == data.temp])

# monday = data[data.day == "Monday"]
# print(monday.weather)
# print(monday.temp * (9/5) + 32)


# # Create dataframe from scratch
# data_dict = {
#     "students" : ["Sats", "Adhi", "Praba"],
#     "scores" : [67, 89, 93]
# }
#
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("student.csv")

str = "satheesh pandian"
print(str.title())