import math
def paint_calc(height, width, coverage):
    calculation = (height * width) / coverage
    return math.ceil(calculation)

test_h = float(input("Enter your wall height: "))
test_w = float(input("Enter your wall width: "))
coverage = int(input("Enter your coverage: "))
# print(paint_calc(test_h,test_w,coverage))
print(paint_calc(height=test_h, coverage=coverage, width=test_w))