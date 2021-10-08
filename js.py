#importing modules

from bs4 import BeautifulSoup

import time

from time import sleep

import requests

import csv

import os

#function to make requests

def makerequest(url):

	#making a request

	page = requests.get( url )

	#checking for 429 response

	if page.status_code == 429:

		print('429 error ! trying again after' + page.headers["Retry-After"] + 'seconds')

		time.sleep(int(page.headers["Retry-After"]))

		page = requests.get( url )

	return(page)

#function to import js url's in a given url

def jsurl(url):
	
	page = makerequest(url)

	soup = BeautifulSoup(page.content , 'html.parser')

	print(soup.prettify())

	jsurl =  soup.find_all('script')

	print(jsurl.prettify())

	return(jsurl)


#main function

def main():

	inputurl = input('\nEnter the url : ')

	scrappedurls = jsurl(inputurl)

	print(scrappedurls)

main()