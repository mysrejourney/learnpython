height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

bmi_value = round(weight / height ** 2)
print(f"Your BMI value is {bmi_value}")
if bmi_value < 18.5:
    print("You are underweight")
elif bmi_value < 25:
    print("You are normal weight")
elif bmi_value < 30:
    print("You are over weight")
elif bmi_value < 35:
    print("You are Obese")
else:
    print("You are clinically Obese")


