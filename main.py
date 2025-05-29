def start():
    greet = input("Vacation Calculator 0.1 \n Where would you like to travel? \n Avaliable Options: \n > San Franciso \n > San Deigo \n > Los Angeles \n > Las Vegas \n > Anaheim ")

    thing = ["\n Accommodation,\n Food,\n Transportation,\n Activites,\n Misc "]

    price = 0
    if greet.lower == "san franciso":
        price = str("~3000+")
        print(thing, "Total Cost: ", price)
    elif greet.lower == "san deigo":
        price = str("~2500+")
        print(thing, "Total Cost: ", price)
    elif greet.lower == "los angeles":
        price = str("~4000+")
        print(thing, "Total Cost: ", price)
    elif greet.lower == "las vegas":
        price = str("~1500+")
        print(thing, "Total Cost: ", price)
    elif greet.lower == "Anaheim":
        price = str("~5000+")
        print(thing, "Total Cost: ", price)
    else:
        price = 0 
        print("Not an Option")
        return start()
    return start()
