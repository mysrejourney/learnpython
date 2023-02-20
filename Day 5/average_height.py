# Get the student heights
student_heights = input("Enter the student heights: ").split()

# Convert the student height from str to int
for n in range (0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Print student height in int format
print(student_heights)

# 156 178 165 171 187

sum = 0
count = 0
# Loop through all values

for height in student_heights:
  # print(height)
  sum += height
  count += 1
# print(sum)
# print(count)

# Calculate the average value
average = round(sum/count)

# print(f"Average: {average}")
print(f"Average: round({sum}/{count})")
