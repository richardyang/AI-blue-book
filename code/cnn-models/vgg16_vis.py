from keras.utils import plot_model
from keras.applications.vgg16 import VGG16

model = VGG16(weights='imagenet', include_top=False)
plot_model(model, to_file='model.png')