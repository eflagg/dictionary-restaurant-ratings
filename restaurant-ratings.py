# your code goes here
def alphabetize(filename):
    file = open(filename)
    restaurants = {}
    line = []
    
    for tup in file:
        line = tup.rstrip()
        line = line.split(":")

        for item in line:
            restaurants[line[0]] = line[1]

    for restaurant_name, rating in restaurants.iteritems():
        print "%s is rated at %s." % (restaurant_name, rating)

alphabetize('scores.txt')