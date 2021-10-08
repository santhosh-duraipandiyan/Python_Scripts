#importing modules

from bs4 import BeautifulSoup

import time

from time import sleep

import requests

import csv

import os

def makerequest(url):

	#making a request

	page = requests.get( url )

	#checking for 429 response

	if page.status_code == 429:

		print('429 error ! trying again after' + page.headers["Retry-After"] + 'seconds')

		time.sleep(int(page.headers["Retry-After"]))

		page = requests.get( url )

	return(page)

#function to get all repositories

def findRepos(uname):

	print('\ngetting all repositories.\n')

	#pagination
	
	tab = '1'

	cachetab = " "

	with open('gitrepo.csv', 'w', newline='', encoding='utf-8') as file:

				writer = csv.writer(file)

				writer.writerow(["repository name", "repository url"])

				while 1 == 1:

					if tab == '1':

						#making resuest

						url = "https://github.com/"+ uname +"?tab=repositories"

						page = makerequest(url)

					else :

						#making resuest

						url = tab

						page = makerequest(url)

					#parsing the response with beautifulsoup

					soup = BeautifulSoup( page.content , 'html.parser') 

					results = soup.findAll("a", {"itemprop" : "name codeRepository"})

					#checking if tab is empty

					if len(tab) == ' ' :

						print("\n> something went wrong please try again later.\n")

						break

					else :

						for result in results :

							repurl = str(result.get('href'))

							repname = str(result.text)

							repname = repname.strip()

							writer.writerow([repname, "https://github.com" + repurl])


						for link in soup.findAll('a', href=True, text='Next'):

							tab = link['href']

						#checking if we reached the end

						if cachetab == tab :

							print("\n> That’s it. You’ve reached the end of "+ uname +"’s repositories.\n")

							break

						else : 

							cachetab = tab

				print('\n> file location = ' + os.getcwd() + '\gitrepo.csv \n' )

#function to get all followers

def findFollowers(uname):

	print('\ngetting all followers.\n')

	#pagination
	
	tab = 1

	with open('gitfollowers.csv', 'w', newline='', encoding='utf-8') as file:

				writer = csv.writer(file)

				writer.writerow(["Username", "Url"])

				while 1 == 1:

					#making resuest

					url = "https://github.com/"+ uname +"?page=" + str(tab) + "&tab=followers"

					page = makerequest(url)

					#parsing the response with beautifulsoup

					soup = BeautifulSoup( page.content , 'html.parser') 

					results = soup.findAll("a", {"class" : "d-inline-block no-underline mb-1"})

					#checking if we reached the end

					if len(results) == 0 :
						
						end = str(soup.findAll("p", text = "That’s it.", attrs = {"class" : "mt-4"}))

						if end != "" :

							print("\n> That’s it. You’ve reached the end of "+ uname +"’s followers.\n")

							break
						 

					else :

							for result in results :

								userurl = str(result.get('href'))

								username = str(result.find('span', {"class" : "f4 Link--primary"}).text)

								writer.writerow([username, "https://github.com" + userurl])

							tab = tab + 1

				print('\nfile location = ' + os.getcwd() + '\gitfollowers.csv \n' )

#function to get all following

def findFollowing(uname):

	print('\ngetting all following.\n')

	#pagination
	
	tab = 1

	with open('gitfollowing.csv', 'w', newline='', encoding='utf-8') as file:

				writer = csv.writer(file)

				writer.writerow(["Username", "Url"])

				while 1 == 1:

					#making resuest

					url = "https://github.com/"+ uname +"?page=" + str(tab) + "&tab=following"

					page = makerequest(url)

					#parsing the response with beautifulsoup

					soup = BeautifulSoup( page.content , 'html.parser') 

					results = soup.findAll("a", {"class" : "d-inline-block no-underline mb-1"})

					#checking if we reached the end

					if len(results) == 0 :

						end = str(soup.findAll("p", text = "That’s it.", attrs = {"class" : "mt-4"}))

						if end != "" :

							print("\n> That’s it. You’ve reached the end of "+ uname +"’s following.\n")

							break

					else :

							for result in results :

								userurl = str(result.get('href'))

								username = str(result.find('span', {"class" : "f4 Link--primary"}).text)

								writer.writerow([username, "https://github.com" + userurl])

							tab = tab + 1

				print('\n> file location = ' + os.getcwd() + '\gitfollowing.csv \n' )

#function to get att stared

def findstarred(uname):

	print('\ngetting all starred.\n')
	
	#pagination
	
	tab = '1'

	cachetab = " "

	with open('gitstarred.csv', 'w', newline='', encoding='utf-8') as file:

				writer = csv.writer(file)

				writer.writerow(["Username", "Url"])

				while 1 == 1:

					if tab == '1':

						#making resuest

						url = "https://github.com/"+ uname +"?tab=stars"

						page = makerequest(url)

					else :

						#making resuest

						url = tab

						page = makerequest(url)

					#parsing the response with beautifulsoup

					soup = BeautifulSoup( page.content , 'html.parser') 

					results = soup.findAll("div", {"class" : "d-inline-block mb-1"})

					#checking if tab is empty

					if len(tab) == ' ' :

						print("\n> something went wrong please try again later.\n")

						break

					else :

						for result in results :

							userurl = str(result.find("a").attrs['href'])

							username = str(result.find('span', {"class" : "text-normal"}).text)

							writer.writerow([username, "https://github.com" + userurl])


						for link in soup.findAll('a', href=True, text='Next'):

							tab = link['href']

						#checking if we reached the end

						if cachetab == tab :

							print("\n> That’s it. You’ve reached the end of "+ uname +"’s starred.\n")

							break

						else : 

							cachetab = tab

				print('\n> file location = ' + os.getcwd() + '\gitstarred.csv \n' )

#main function

def main():

	#getting a git username

	uname = input("\nEnter the git username: ")

	#choosing the module

	print("\n\n> Press 1 to get the repositories.\n> Press 2 to get followers.\n> Press 3 to get following.\n> Press 4 to get stars.\n> Press 5 to get all.\n\n")

	module = input("Your choice: ")

	if module == '1':
		
		findRepos(uname)

	elif module == '2':

		findFollowers(uname)

	elif module == '3':

		findFollowing(uname)

	elif module == '4':

		findstarred(uname)

	elif module == '5':

		findRepos(uname)

		findFollowers(uname)

		findFollowing(uname)

		findstarred(uname)

	elif module > '6':

		print('please select the right option !')

		main()

main()