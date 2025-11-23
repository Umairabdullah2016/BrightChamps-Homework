#Step One, Ask the user to input()
a = input("Enter Any word and this file will reverse it: ")
#step 2
ending_number = len(a)
print(f"There are {ending_number} characters in {a}")
pandilrome_converter= a[::-1]
print(f"The Inverted word Is {pandilrome_converter}")
capital_a = a.capitalize()
if pandilrome_converter == a:
    capital_a = a.capitalize()
    print(f"{capital_a} Is A Pandilrome Word! ")
else:
    print(f"{capital_a} is not a Pandilrome word.")
