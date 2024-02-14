# Create a function that takes the age in years and returns the age in days.

def calc_age():
  age = input("Your age: ")
  result = int(age) * 365
  print(f"‣ You've been alive for about {result} days.")

calc_age()