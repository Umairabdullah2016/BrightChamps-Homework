weight = float(input("Enter Your Weight (in KG) : "))
height = float(input("Enter Your Height (In centimetre) : "))


# heightIn_m = height / 100 # 1m = 100cm
# BMI = weight / (heightIn_m ** 2)

BMI = weight / ((height/100)**2)

print(f"The Body Mass Index is {BMI}")
if BMI < 18.4:
    print("underweight")
elif BMI < 24.9:
    print("You Are Healthy")
elif BMI  < 29.9:
    print("You Are Overweight")
elif BMI < 34.9:
    print("You Are Extreamely overweighted")
elif BMI < 39.9:
    print("You are obese")
else:
    print("You The Several Obese (The Most Biggest A Python Program Has Ever Seen!)")
