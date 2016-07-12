# your code goes here
import random

def alphabetize(filename):
    """Alphabetizes list of restaurants and ratings

    Takes text file and turns it into dictionary in order to print restaurant_name with
    its rating in alphabetical order
    """
    username = raw_input("Hi, what's your name? ")
    print "Hi %s!" % (username)

    file = open(filename)
    restaurants = {}
    line = []
    
    # loops through textfile, strips any hanging spaces, splits into a list based on ':'
    for tup in file:
        line = tup.rstrip()
        line = line.split(":")

        # loops through each list created from the outer for loop and inserts it into 
        # the dictionary
        for item in line:
            restaurants[line[0]] = line[1]

    #Generates a random restaurant, asks user for rating and changes rating within the 
    #dictionary. Does this until user types 'q' or 'Q'
    while True: 
        random_restaurant_tuple = random.choice(restaurants.items())   
        print "Let's look at a sample restaurant!"     
        print random_restaurant_tuple[0] + ": " + random_restaurant_tuple[1]

        new_rating = raw_input("What should the new rating be? ")
        restaurants[random_restaurant_tuple[0]] = new_rating
        if new_rating in ['q','Q']:
            break
        else:
            print "Success! You successfully changed the restaurant rating!"

    #Asks user to input another restaurant with a rating and adds to dictionary
    new_restaurant = raw_input("Another restaurant name? ")
    new_score = int(raw_input("Restaurant's rating? "))

    restaurants[new_restaurant] = new_score

    # loops through the dictionary and sorts it based on restaurant_name and prints out
    # restaurant name and rating as a string
    for restaurant_name, rating in sorted(restaurants.iteritems()):
        print "%s is rated at %s." % (restaurant_name, rating)


alphabetize('scores.txt')