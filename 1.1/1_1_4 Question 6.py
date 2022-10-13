#   a114_divisible.py

# get two numbers from user
x = int(input("gimme your first number:"))
y = int(input("gimme your second number please:"))
# loop while the numbers are not divisible (the remainder is 0)
while x % y != 0:
  # inform user of result 
  print("Hey those dont work together")
  # gather user input again
  x = int(input("gimme your first number:"))
y = int(input("gimme your second number please:"))
# inform user of result 
print("your numbers",x,"and:",y,"are evenly divisible.")
