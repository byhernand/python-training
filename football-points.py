# Create a function that takes the number of wins, draws and losses
# and calculates the numberof points a football team has obtained so far.

def football_points():
  wins = int(input("🏆 Wins: "))
  draws = int(input("🤝 Draws: "))
  losses = int(input("❌ Looses: "))

  # Error handling
  if wins < 0 or draws < 0 or losses < 0:
    print("‼️ Only positive numbers, try again.")
    return

  score = (wins * 3) + (draws * 1) + (losses * 0)
  print(f"‣ The score is {score}")


# Run
football_points()