sum = 0

for number in range(0, 101):
  if number % 2 == 0:
     sum += number

print(sum)

sum = 0
for number in range(2, 101, 2):
  sum += number

print(sum)
