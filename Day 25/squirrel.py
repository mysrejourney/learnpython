import pandas
data = pandas.read_csv("squirrel_data.csv")
# print(data.count())
gray = len(data[data["Primary Fur Color"] == "Gray"])
print(gray)
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon)
black = len(data[data["Primary Fur Color"] == "Black"])
print(black)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray, cinnamon, black]
}
#
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("squirrel_count.csv")
pandas.DataFrame(data_dict).to_csv("squirrel_count.csv")