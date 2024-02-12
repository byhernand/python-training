# Convert minutes into seconds

def convert():
  userInput = input("⌛️ How many minutes do you want to convert?")
  minutes = int(userInput)
  result = minutes * 60
  print(minutes, "minutes equals", result, "seconds")

convert()