# your code goes here
def alphabetize(filename):
    """Alphabetizes list of restaurants and ratings

    Takes text file and turns it into dictionary in order to print restaurant_name with
    its rating in alphabetical order
    """

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
    # loops through the dictionary and sorts it based on restaurant_name and prints out
    # restaurant name and rating as a string
    for restaurant_name, rating in sorted(restaurants.iteritems()):
        print "%s is rated at %s." % (restaurant_name, rating)

alphabetize('scores.txt')