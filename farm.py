# In this challenge, a farmer is asking you to tell him how many legs
# can be counted among all his animals. The farmer breeds three species:
# • chickens = 2 legs
# • cows = 4 legs
# • pigs = 4 legs


def countLegs():
  chickens = int(input("🐔 Number of chickens: "))
  cows = int(input("🐮 Number of cows: "))
  pigs = int(input("🐷 Number of pigs: "))

  chickenLegs = chickens * 2
  cowLegs = cows * 4
  pigLegs = pigs * 4
  totalLegs = chickenLegs + cowLegs + pigLegs

  print("\n‣ Total legs on the farm: ", totalLegs)


countLegs()