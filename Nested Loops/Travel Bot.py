print("Welcome, I am you tour bot, Built With UAserver AI")
season = str(input("What Season Would you like to travel in?: "))
budget = str(input("Give Me Your Budget (low , medium or high): "))
continents = str(input("Which Continent would you like to visit?: "))
if budget == "low":
    if continents == "Europe":
        if season == "Summer" or season == "Spring":
            print("Europe is a great place to go to")
        else:
            print("Europe is not a good place to visit in winter.")
    elif continents == "Asia":
        if season == "Summer" or season == "Spring":
            print("Asia Is not The Best Place to go to if you don't have a pool because it is hot(Except Vitnam).")
        elif season == "Winter" or season == "Autumn":
            print("Asia Is A ood Place to go to in the winter as it is lower teprature (Around 15 Degrees to 20 degrees)")
    elif continents in["North America", "South America", "America"]:
        if season == "Summer" or season == "Spring":
            print("America Is A Good Place To Visit In Summer or Spring!")
        elif season == "Autumn" or season == "Winter":
            print("It's A little Cold In America in winter")
elif budget == "medium":
    if continents == "Europe":
        if season == "Summer" or season == "Spring":
            print("Europe is a great place to go to")
        else:
            print("Europe is not a good place to visit in winter.")
    elif continents == "Asia":
        if season == "Summer" or season == "Spring":
            print("Asia Is not The Best Place to go to if you don't have a pool because it is hot(Except Vitnam).")
        elif season == "Winter" or season == "Autumn":
            print("Asia Is A ood Place to go to in the winter as it is lower teprature (Around 15 Degrees to 20 degrees)")
    elif continents in["North America", "South America", "America"]:
        if season == "Summer" or season == "Spring":
            print("America Is A Good Place To Visit In Summer or Spring!")
        elif season == "Autumn" or season == "Winter":
            print("It's A little Cold In America in winter")
    elif continents == "Austrailia" or continents == "Oceana":
        if season == "Summer" or season == "Spring":
            print("Austrailia Is Most Dessert!, Why'd you choose in the hot times")
        elif season == "Autumn" or season == "Winter":
            print("Ahhh, It Will Be Perfet to go to Austrailia or Oceana now :)")
elif budget == "high":
    if continents == "Europe":
        if season == "Summer" or season == "Spring":
            print("Europe is a great place to go to")
        else:
            print("Europe is not a good place to visit in winter.")
    elif continents == "Asia":
        if season == "Summer" or season == "Spring":
            print("Asia Is not The Best Place to go to if you don't have a pool because it is hot(Except Vitnam).")
        elif season == "Winter" or season == "Autumn":
            print("Asia Is A ood Place to go to in the winter as it is lower teprature (Around 15 Degrees to 20 degrees)")
    elif continents in["North America", "South America", "America"]:
        if season == "Summer" or season == "Spring":
            print("America Is A Good Place To Visit In Summer or Spring!")
        elif season == "Autumn" or season == "Winter":
            print("It's A little Cold In America in winter")
    elif continents == "Austrailia" or continents == "Oceana":
        if season == "Summer" or season == "Spring":
            print("Austrailia Is Most Dessert!, Why'd you choose in the hot times")
        elif season == "Autumn" or season == "Winter":
            print("Ahhh, It Will Be Perfet to go to Austrailia or Oceana now :)")
    elif continents == "Antartica":
        if season in["Spring", "Summer", "Autumn", "Winter"]:
            print("Antarica Is Way too cold to go to!")
    elif continents == "Antartic" or continents == "Artic":
        if season in["Spring", "Summer", "Autumn", "Winter"]:
            print("🥶Brr, The Artics Is Way Too Cold!")
