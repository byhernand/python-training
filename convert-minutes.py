# Convert minutes into seconds

def convert():
  user_input = input("⌛️ How many minutes do you want to convert?")
  minutes = int(user_input)
  result = minutes * 60
  print(minutes, "minutes equals", result, "seconds")

convert()