target = int(input("Enter a number between 0 to 100. This will be the limit the computer will add to: ")) # Enter a number between 0 and 1000


total = 0
for number in range (2, (target + 1), 2):
  total += number

print(total)