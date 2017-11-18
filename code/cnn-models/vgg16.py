'''
Feature extraction using VGG16
'''
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os

data_path = "data/"
output_path = "features/"
if not os.path.exists(output_path):
	os.makedirs(output_path)
model = VGG16(weights='imagenet', include_top=False)


with open("bikes_filtered.csv", "r") as file:
	i = -1
	for data_point in file:
		i += 1
		index, name, msrp = data_point.split(",")
		img_path = data_path+index+'.jpg'
		img = image.load_img(img_path, target_size=(224, 224))
		x = image.img_to_array(img)
		x = np.expand_dims(x, axis=0)
		x = preprocess_input(x)
		features = model.predict(x)
		# print(features.shape) # (1,7,7,512) 512 7x7 feature maps
		
		# Reshape features into 2D tensor
		# https://datascience.stackexchange.com/questions/16444/feature-extraction-for-a-pretrained-model-in-keras
		reshaped_features = features.reshape(1, 512*7*7)
		if i % 100 == 0:
			print(i)
		# filename = output_path+index+".txt"
		# np.savetxt(filename, reshaped_features)