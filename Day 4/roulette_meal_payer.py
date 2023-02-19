import random
input_names = input("Give me everybody's name, seperated by a comma: ")
actual_names = input_names.split(", ")

print(actual_names)

length_of_names = len(actual_names)
print(f"length is {length_of_names}")

random_number = random.randint(0, length_of_names - 1)
print(f"random number generated is {random_number}")

print(f" {actual_names[random_number]} is chosen to pay the bill this time")

