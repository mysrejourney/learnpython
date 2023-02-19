# Get the smiley inputs
row_1 = ['😀', '😃', '😄']
row_2 = ['🥰', '😘', '😗']
row_3 = ['😒', '😞', '😔']
map = [row_1, row_2, row_3]

print(map)

position = input("Where do you want to put the treasure?: ")

# digits = int(int(position) / 10)
# reminder = int(position) % 10
digits = int(position[0])
reminder = int(position[1])

print(f"Digits : {digits} and Reminder : {reminder}")

map[reminder - 1] [digits - 1] = 'X'

print(f"{map}")