'''
Converts ImageNet bounding box XML file to dlib XML file
'''
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET
from xml.dom import minidom
import os

problematic_images = [
"n02834778_10669.JPEG",
"n02834778_10735.JPEG",
"n02834778_11107.JPEG",
"n02834778_1175.JPEG",
"n02834778_11766.JPEG",
"n02834778_12225.JPEG",
"n02834778_1248.JPEG",
"n02834778_1709.JPEG",
"n02834778_3065.JPEG",
"n02834778_3182.JPEG",
"n02834778_3400.JPEG",
"n02834778_3678.JPEG",
"n02834778_3801.JPEG",
"n02834778_41144.JPEG",
"n02834778_4188.JPEG",
"n02834778_4305.JPEG",
"n02834778_458.JPEG",
"n02834778_5502.JPEG",
"n02834778_5671.JPEG",
"n02834778_6818.JPEG",
"n02834778_7195.JPEG",
"n02834778_7536.JPEG",
"n02834778_8394.JPEG",
"n02834778_875.JPEG",
"n02834778_8979.JPEG",
"n02834778_9221.JPEG",
"n02834778_9569.JPEG",
"n02834778_9954.JPEG"]

root = ET.Element("dataset")
images = ET.SubElement(root, "images")
path = os.getcwd()+"/imagenet-bicycle-boundingbox/"

for filename in os.listdir(path):
	print filename
	with open(path+filename) as file:
		soup = BeautifulSoup(file, features="xml")

		# Find and write the image file name
		name = soup.find("filename")
		if name.string+".JPEG" in problematic_images:
			continue
		imagefile = ET.SubElement(images, "image", file=name.string+".JPEG")
		
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
			width = int(_xmax[i].string)-int(_xmin[i].string)
			height = int(_ymax[i].string) - int(_ymin[i].string)
			#attrs = {'top': top, 'left': left, 'width': width, 'height': height}
			box = ET.SubElement(imagefile, "box")
			box.set("top", str(top))
			box.set("left", str(left))
			box.set("width", str(width))
			box.set("height", str(height))

xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open("imagenet-bicycle/training.xml", "w") as f:
	f.write(xmlstr)