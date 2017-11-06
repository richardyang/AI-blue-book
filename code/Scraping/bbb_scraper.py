import os
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
from collections import defaultdict

index_url = 'https://www.bicyclebluebook.com/SearchBikes.aspx'
page = urllib2.urlopen(index_url)
soup = BeautifulSoup(page, 'html.parser')

'''
Returns a dictionary of bicycle brands from the SearchBikes page
'''
def getBrands():
	data = set([])
	for column in soup.findAll('div', attrs={'class':'col-md-3 col-xs-6'}):
		data = data | set(column.text.splitlines())
	# Remove the empty string
	data = filter(None, data)
	return defaultdict.fromkeys(data, '')

'''
Fills the dictionary with IDs for each brand in BBB database
'''
def getIDs(brands):
	# This is a really inefficient way to find all the IDs
	for link in soup.findAll('a'):
		for brand in brands.keys():
			if brand in link.text:
				# Only care about the IDs, can strip the rest of the URL
				stripped = link.get('href').split("=")
				if len(stripped) == 2:
					brands[brand] = stripped[1]

'''
Writes the link to a model page to models.txt
'''
def getModels(brands):
	# Crawl the brand pages to get the models page of each brand
	with open("models.txt", "w") as file:
		for v in brands.values():
			page_link = 'https://www.bicyclebluebook.com/BicycleDatabase.aspx?make='+str(v)
			page = urllib2.urlopen(page_link)
			soup = BeautifulSoup(page, 'html.parser')
			for link in soup.findAll('a'):
				href = link.get('href')
				if not href is None:
					if 'model' in href:
						print href
						file.write("https://www.bicyclebluebook.com"+href+"\n")
						file.flush()

'''
Writes the link to a listing page to listings.txt
Takes a long time to run
'''
def getListings():
	# Crawl the model pages to get the individual listing pages
	# Write all the links to a file
	searchLinks = open("models.txt").readlines()
	#print len(searchLinks) #39017
	with open("listings.txt", "a") as file:
		for i in range(1000, 5000): # Done with this iter, increment next time
			link = searchLinks[i]
			page = urllib2.urlopen(link)
			soup = BeautifulSoup(page, 'html.parser')
			for url in soup.findAll('a'):
				href = url.get('href')
				if not href is None:
					if 'SearchListingDetail' in href:
						#print href
						file.write("https://www.bicyclebluebook.com"+href+"\n")
						file.flush()

def exportData():
	listings = open("listings.txt").readlines()
	#print len(listings)
	with open("msrp.csv", "a") as file:
		for i in range(0, 1000):
			link = listings[i]
			make = link.split('&')[1].split('=')[1].rstrip()
			model = link.split('&')[2].split('=')[1].rstrip()
			page = urllib2.urlopen(link)
			soup = BeautifulSoup(page, 'html.parser')

			# Find and store the picture
			img = soup.find("img", {"id": "contentBody_imgBikeImage"})
			#print img['src']
			if img.has_attr('alt'):
				if not os.path.exists(make+"/"+model):
					os.makedirs(make+"/"+model)
				img_alt = img['alt'].replace("/", "")
				filepath = make + "/" + model + "/" + img_alt + ".jpg"
				urllib.urlretrieve(img['src'], filepath)

			# Find and write the MSRP to csv
			table = soup.findAll('div', attrs={'class': 'col-xs-6'})
			msrp = table[11].text.strip()
			print make+","+model.rstrip()+","+re.sub(r'[^\w]', '', msrp)
			file.write(make+","+model+","+re.sub(r'[^\w]', '', msrp)+"\n")



def main():
	#brands = getBrands()
	#getIDs(brands)
	#getModels(brands)
	
	getListings()
	#exportData()


if __name__ == '__main__':
	main()