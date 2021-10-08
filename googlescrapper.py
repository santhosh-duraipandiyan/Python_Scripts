#importing modules

from googlesearch import search 

from bs4 import BeautifulSoup

def googlesearch(query):

	results = ()
	
	for temp in search(query) :

		results = results.append(temp)

	print(results)

def getdorks():
	
	#getting dorks

	dorks = ()
		
	# Using readlines()

	file = open('bb_dorks.txt', 'r')

	Lines = file.readlines()

	dorks = tuple(Lines)

	file.close()

	return(dorks)

#main function

def main():

	dorks = getdorks()

	for dork in dorks:
		
		results = googlesearch(dork)

		for i in results :

			print(i)	
main()