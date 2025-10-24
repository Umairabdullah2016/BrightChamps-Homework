print("This, is a calculator")
msg1 = input("chose one of the following options: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n\n Choose: ")
if msg1 in["1", "Add", "add", "Addition", "addition"]:

  msg2 = float(input("Enter the first number: "))
  msg3 = float(input("Enter the second number: "))
  print(msg2, "+", msg3, "=", msg2 + msg3)
elif msg1 in["2", "Subtract", "subtract", "Subtraction", "subtraction"]:
  msg4 =  float(input("Enter the first number: "))
  msg5 = float(input("Enter the second number: "))
  print(msg4, "-", msg5, "=", msg4 - msg5)
elif msg1 in["3", "Multiply", "multiply", "Multiplication", "multiplication"]:
  msg6 = float(input("Enter the first number: "))
  msg7 = float(input("Enter the second number: "))
  print(msg6, "×", msg7, "=", msg6 * msg7)
elif msg1 in["4", "Divide", "divide", "Division", "division"]:
  msg8 = float(input("Enter the first number: "))
  msg9 = float(input("Enter the second number: "))
  print(msg8, "÷", msg9, "=", msg8 / msg9)
else:
  print("Invalid option")