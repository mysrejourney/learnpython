# Get the height
height = input("Enter your height in m: ")
# Get the weight
weight = input("Enter your weight in kg: ")

# Calculate BMI = weight / (height) ** 2
bmi = round(float(weight) / float(height) ** 2)

# print the output BMI
print("BMI value is "+ str(bmi))
