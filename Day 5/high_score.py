# Get the user input
student_score = input("Enter the score with comma seperated : "). split(", ")

# Convert the inputs from str to int
for n in range(0, len(student_score)):
  student_score[n] = int(student_score[n])
# print the input in int format
print(student_score)

max_score = 0

# Loop through student score
for score in student_score:
  # Compare the current score with max score
  if max_score < score:
     max_score = score

# Print the max score
print(max_score)
