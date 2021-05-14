import random

Chinese_cuisine = ["Sweet & Sour Chicken", "Kung pao chicken and noodles", "Lo Mein"]
Colombian_cuisine = ["Locro soup", "Valluna", "Tamales"]
Czech_cuisine = ["Vepřo knedlo zelo", "Uzené", "Svíčková na smetaně"]
Louisiana_cuisine = [" jambalaya", "Crawfish", "Gumbo"]
def what_to_eat():
    place = input("Where would you like to eat this fine afternoon?" + "\n" + "1) Chinese Cuisine" + "\n" + "2) Colombian Cuisine" + "\n" + "3) Czech Cuisine" + "\n" + "4) Louisiana Cuisine" + "\n" + "5) Random" + "\n" + "Enter 1-5: ")
    if place == "1":
        print("\n" + "Ok! Let me find you something to eat... one second.")
        print("You should eat: " + random.choice (Chinese_cuisine))
    elif place == "2":
        print("\n" + "Ok! Let me find you something to eat... one second.")
        print("You should eat: " + random.choice (Colombian_cuisine))
    elif place == "3":
        print("\n" + "Ok! Let me find you something to eat... one second.")
        print("You should eat: " + random.choice (Czech_cuisine))
    elif place == "4":
        print("\n" + "Ok! Let me find you something to eat... one second.")
        print("You should eat: " + random.choice (Louisiana_cuisine))
    elif place == "5":
        random_number = random.randint(1,4)
        #print("Number generated: " + str(random_number))
        print("\n" + "Random? Alright, let me find you something to eat... one second.")
        if random_number == 1:
            print("You should eat: " + random.choice (Chinese_cuisine))
        elif random_number == 2:
            print("You should eat: " + random.choice (Colombian_cuisine))
        elif random_number == 3:
            print("You should eat: " + random.choice (Czech_cuisine))
        elif random_number == 4:
            print("You should eat: " + random.choice (Louisiana_cuisine))
    else:
        print("Please input 1 through 5 only")

what_to_eat()