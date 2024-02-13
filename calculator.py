print("🧮 Minimal Calculator")

a = int(input("Number One: "))
b = int(input("Number Two: "))
operation = input("Operation: \n1 → Sum \n2 → Subtraction \n3 → Multiplication \n4 → Division \n")

result = None

if operation == "1":
  result = a + b
elif operation == "2":
  result = a - b
elif operation == "3":
  result = a * b
elif operation == "4":
  result = a / b
else:
  print("❌ No valid option")

print("👉🏼 Your result is", result)