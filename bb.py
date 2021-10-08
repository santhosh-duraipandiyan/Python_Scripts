#importing modules

from bs4 import BeautifulSoup

import random

from random import randrange

from time import sleep

import requests

import time

import csv

import os

import re

# def LoadUpProxies():

# 	proxies = []

# 	proxyurl='https://sslproxies.org/'

# 	header = {
# 		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
# 	}
# 	response=requests.get(proxyurl,headers=header)

# 	soup=BeautifulSoup(response.content, 'html.parser')

# 	for item in soup.select('#proxylisttable tr'):

# 		try:

# 			proxies.append({'ip': item.select('td')[0].get_text(), 'port': item.select('td')[1].get_text()})

# 		except:

# 			print('')

# 	rnd=randrange(len(proxies))

# 	randomIP=proxies[rnd]['ip']

# 	randomPort=proxies[rnd]['port']

# 	ip = str(randomIP + ':' + randomPort)

# 	proxy = {

# 		"https" : ip

# 	}

# 	return(proxy)

#function to make requests

def makerequest(url):

	requrl = url

	user_agent_list = (

		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
		'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
		'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
		'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
		'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
		'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
		'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko'
	)

	user_agent = random.choice(user_agent_list)

	print(user_agent)

	header = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
				'accept-language': 'en-US,en;q=0.9',
				'cache-control': 'no-cache',
				'referer': 'https://www.google.com/',
				'user-agent': user_agent }

	#making a request

	time.sleep(randrange(5, 10))

	page = requests.get( requrl , headers = header)

	print("\nrequest made to :" + url + "\n")

	#checking for 429 response

	if page.status_code == 429:

		print ("Oops Google caught us!")

		time.sleep(randrange(150, 200))

		makerequest(requrl)

	return(page)

#Function to get all dorks

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

	with open('googledork.csv', 'w', newline='', encoding='utf-8') as file:

		writer = csv.writer(file)

		dorks = getdorks()

		for dork in dorks:

			writer.writerow(["Dork :" + dork])

			#pagination
			
			tab = '1'

			cachetab = " "

			while 1 == 1:

				if tab == '1':

					#making resuest

					url = 'https://google.com/search?q=' + dork

					page = makerequest(url)

				else :

					#making resuest

					url = tab

					page = makerequest(url)

				#parsing the response with beautifulsoup

				soup = BeautifulSoup( page.content , 'html.parser') 

				# print(soup)

				#finding all the h3 tags

				h3 = tuple(soup.find_all("h3"))

				#finding all the anchor tags

				anchor = tuple(soup.find_all("a"))

				#comparing them to get the right url's

				temp = []

				for i in h3 :

					for j in anchor :

						if i in j:

							temp.append(j)

				#checking if tab is empty

				if len(tab) == '' :

					print("\n> something went wrong please try again later.\n")

					break

				else :

					for i in temp :

						# print ("\nhttps://www.google.com" + i.get('href') + "\n")

						writer.writerow([i.get('href')])

					#getting the pagination url

					paginationurl = str(soup.find("a", {"id" : "pnnext"}))

					print('this is paginationurl :' + paginationurl)

					if paginationurl == 'None' :

						print('\n end of results !\n')

						break

					else :

						tab = "https://www.google.com/" + str(soup.find("a", {"id" : "pnnext"}).get('href'))

					#checking if we reached the end

					if cachetab == tab :

						print("\n> That’s it. You’ve reached the end of the results.\n")

						break

					else : 

						cachetab = tab

			print('\n> file location = ' + os.getcwd() + '\googledork.csv \n' )
	 
	

main()


