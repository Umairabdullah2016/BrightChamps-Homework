try:
  while True:
    table = int(input("Enter a number: "))
    multiplier = 0
    answer = 0
    for i in range(20):
      multiplier += 1
      answer += table
      print(table, "×", multiplier, "=", answer)
except ValueError as  e:
  print("This Is Not A Number, if it is a decimal number, remove the decimal point")