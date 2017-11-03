import urllib2
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
WIP: don't run this yet
'''
def getModels(brands):
	iters = 0
	links = []
	for v in brands.values():
		# For testing, don't send too many HTTP requests
		if iters > 10:
			break
		page_link = 'https://www.bicyclebluebook.com/BicycleDatabase.aspx?make='+str(v)
		print page_link
		page = urllib2.urlopen(page_link)
		soup = BeautifulSoup(page, 'html.parser')
		for link in soup.findAll('a'):
			href = link.get('href')
			print href
			if not href is None:
				if 'model' in href:
					links.append(href)
		iters +=1
	print links

def main():
	brands = getBrands()
	getIDs(brands)
	print brands
	#models = getModels(brands)



if __name__ == '__main__':
	main()