#importing modules

from bs4 import BeautifulSoup

import time

from time import sleep

import requests

import csv

import os

# https://www.packtpub.com/catalogsearch/result/?q=hacking&released=Available&page=1

def makerequest(url):

	#making a request

	header = {
					'cookie': '_ALGOLIA=2ad8b648-c043-4826-b2f0-ca040f7f5a1b; rmStore=amid:45060|adr:item|acs:false|dmid:8755; _gcl_au=1.1.1326775147.1628261762; _ga=GA1.2.463903949.1628261762; _hjid=58aad2ad-cf08-4304-be76-52cd6e473f80; _fbp=fb.1.1628261762340.1737523843; _gu=8b95f636-81ab-4362-849b-903f09973ead; geoip_store_code=in; _gid=GA1.2.1392520002.1629003107; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-banners-cache-storage=%7B%7D; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; __rmcp=1%2C2%2C3%2C4%2C5; packt_target=true; packt_performance=true; packt_required=true; packt_privacy=true; packt_gdpr=true; _gs=2.s(src%3Dhttps%3A%2F%2Fwww.packtpub.com%2F); _hjAbsoluteSessionInProgress=1; _hp2_ses_props.34805961=%7B%22r%22%3A%22https%3A%2F%2Fwww.packtpub.com%2Fcatalogsearch%2Fresult%2F%3Fq%3Dhacking%26released%3DAvailable%26page%3D1%22%2C%22ts%22%3A1629035417330%2C%22d%22%3A%22www.packtpub.com%22%2C%22h%22%3A%22%2Fcatalogsearch%2Fresult%2F%22%2C%22q%22%3A%22%3Fq%3Dhacking%26released%3DAvailable%26categories%3DSecurity%22%7D; form_key=Vfv41KXgylJ91rku; _gat_UA-284627-1=1; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample=0; PHPSESSID=812aeafa83e9a6b49ff6827e49d6c760; stc120495=env:1629035425%7C20210915135025%7C20210815142039%7C2%7C1100236:20220815135039|uid:1628261762135.753241726.4291582.120495.901263620.8:20220815135039|srchist:1100235%3A1%3A20210906145602%7C1100236%3A1629035425%3A20210915135025:20220815135039|tsa:1629035425858.1548798834.8168283.3088463433458193.:20210815142039; _gaexp=GAX1.2.aI4MSGUsQey6iewqehEa4A.18899.1; _gw=2.480013(sc~1%2Cs~qxvch9)u%5B%2C%2C%2C%2C%5Dv%5B~g5xj2%2C~1%2C~1%5Da(); mage-cache-sessid=true; private_content_version=1508cf650c0a337115bca0cb8b76a31f; section_data_ids=%7B%22cart%22%3A1629035444%7D; _hp2_id.34805961=%7B%22userId%22%3A%221947285496014670%22%2C%22pageviewId%22%3A%228038007834027121%22%2C%22sessionId%22%3A%225368604555267197%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D'
					 
					 }

	page = requests.get( url )

	#checking for 429 response

	if page.status_code == 429:

		print('429 error ! trying again after' + page.headers["Retry-After"] + 'seconds')

		time.sleep(int(page.headers["Retry-After"]))

		page = requests.get( url )

	return(page)

def geturls():
	
	#pagination
	
	tab = 1

	with open('packtpub.csv', 'w', newline='', encoding='utf-8') as file:

				writer = csv.writer(file)

				writer.writerow(["Name", "Price", "Release date", "Url"])

				while 1 == 1:

					url = "https://www.packtpub.com/security?released=Available&page=" + str(tab)

					page = makerequest(url)

					#parsing the response with beautifulsoup

					soup = BeautifulSoup( page.content , 'html.parser') 

					print(soup)

					results = soup.findAll("li", {"class" : "item product product-item"})

					# print(results)

					#checking if we reached the end

					if len(results) == 0 :
				
						break
						 

					else :

							for result in results :

								Link = str(result.find('a', {"class" : "product-item-link"}).get('href'))

								Name = str(result.find('a', {"class" : "product-item-link"}).text)

								# Author = str(result.find('div', {"class" : "author-names"}).text)

								Price = str(result.find('span', {"class" : "price"}).text)

								Release = str(result.find('div', {"class" : "date-of-publication"}).text)

								# print("Name : " + Name, "\nPrice : " + Price, "\nRelease : " + Release, "\nLink : " + Link)

								writer.writerow([Name, Price, Release , Link])

							tab = tab + 1

def main():

	print('\ngetting all books.\n')

	#pagination
	
	tab = 1

	with open('packtpub.csv', 'w', newline='', encoding='utf-8') as file:

				writer = csv.writer(file)

				writer.writerow(["Name", "Price", "Release date", "Url"])

				while 1 == 1:

					url = "https://www.packtpub.com/security?released=Available"

					page = makerequest(url)

					#parsing the response with beautifulsoup

					soup = BeautifulSoup( page.content , 'html.parser') 

					print(soup)

					results = soup.findAll("li", {"class" : "item product product-item"})

					# print(results)

					#checking if we reached the end

					if len(results) == 0 :
				
						break
						 

					else :

							for result in results :

								Link = str(result.find('a', {"class" : "product-item-link"}).get('href'))

								Name = str(result.find('a', {"class" : "product-item-link"}).text)

								# Author = str(result.find('div', {"class" : "author-names"}).text)

								Price = str(result.find('span', {"class" : "price"}).text)

								Release = str(result.find('div', {"class" : "date-of-publication"}).text)

								# print("Name : " + Name, "\nPrice : " + Price, "\nRelease : " + Release, "\nLink : " + Link)

								# writer.writerow([Name, Price, Release , Link])

							tab = tab + 1

				# print('\nfile location = ' + os.getcwd() + '\packtpub.csv \n' )

if __name__ == '__main__':
	main()