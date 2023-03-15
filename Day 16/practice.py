# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("Cornflowerblue")
# timmy.penup()
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

names = ["Pikachu", "Squirtle", "Charmander"]
number = []
table = PrettyTable()
# print(table)
for num in range(3):
    number.append(num)
table.add_column("S.No", number)
table.add_column("Pokeman Name", names)
table.add_column("Type",["Electric", "Water", "Fire"])
# table.align["Pokeman Name"] = "l"
# table.align["Type"] = "l"
table.align = "r"
print(table)