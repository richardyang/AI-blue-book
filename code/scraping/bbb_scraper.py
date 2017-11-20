import os
import urllib
import urllib2
import re
import time
import string
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
		for i in range(0, 39017):
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
		for i in range(0, 71347):
			#print i
			if i in range(20000, 80000, 20000):
				print "20000 examples processed! Time for a break."
				time.sleep(600)
			link = listings[i]
			make = link.split('&')[1].split('=')[1].rstrip()
			model = link.split('&')[2].split('=')[1].rstrip()
			page = urllib2.urlopen(link)
			soup = BeautifulSoup(page, 'html.parser')

			# Find and store the picture
			img = soup.find("img", {"id": "contentBody_imgBikeImage"})
			#print img['src']

			# Make the filepath
			filepath = "data/"+make + "/" + model + "/"
			if not os.path.exists(filepath):
					os.makedirs(filepath)
			
			# Save the image, if one exists
			if img.has_attr('alt'):
				# Convert to ascii and remove all punctuation
				ascii_img_alt = img['alt'].encode('ascii', 'ignore')
				img_alt = str(ascii_img_alt).translate(None, string.punctuation)
				imgpath = filepath + img_alt + ".jpg"
				# Handle all the random quirks
				try:
					urllib.urlretrieve(img['src'], imgpath)
				except Exception as e:
					print "Error encountered"
					pass
			

			# Save the Product Details text
			with open(filepath+make+"-"+model+"-"+"details.txt", "w") as det:
				details = soup.find('div', attrs={'class': 'row bvg-product-details'})
				det.write(details.text.encode('ascii','ignore'))

			# Find and write the MSRP to csv
			name = soup.find('div', attrs={'class': 'value-name'}).text.encode('ascii','ignore').strip()
			table = soup.findAll('div', attrs={'class': 'col-xs-6'})
			msrp = table[11].text.strip()
			file.write(name+","+make+","+model+","+re.sub(r'[^\w]', '', msrp)+"\n")
			file.flush()





def main():
	#brands = getBrands()
	#getIDs(brands)
	#getModels(brands)
	#getListings()
	exportData()


if __name__ == '__main__':
	main()