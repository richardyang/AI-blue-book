import numpy as np
import cv2
from bs4 import BeautifulSoup
import os

path = os.getcwd()+"/imagenet-bicycle-boundingbox/"
imgpath = os.getcwd()+"/imagenet-bicycle/"

for filename in os.listdir(path):
	print filename
	with open(path+filename) as file:
		soup = BeautifulSoup(file, features="xml")

		# Find and write the image file name
		name = soup.find("filename")
		# Find all the bounding boxes
		_xmin = soup.findAll("xmin")
		_xmax = soup.findAll("xmax")
		_ymin = soup.findAll("ymin")
		_ymax = soup.findAll("ymax")

		# For every bounding box, there are guaranteed to be four sides
		# So we can just count one side to see how many bounding boxes there are
		for i in range(len(_xmin)):
			top = int(_ymin[i].string)
			left = int(_xmin[i].string)
			bottom = int(_ymax[i].string)
			right = int(_xmax[i].string)
			
			img = cv2.imread(imgpath+name.string+".JPEG")
			cv2.rectangle(img,(top,left),(bottom,right),(0,255,0),5)
			cv2.imshow('image',img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()