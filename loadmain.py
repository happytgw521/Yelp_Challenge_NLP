from dbloader import MongoLoad

def main():
	loader = MongoLoad()
	loader.execute("yelpdb", "/Users/hellrambler/Documents/yelp_challenge/yelp_dataset")

	return 0

main()
