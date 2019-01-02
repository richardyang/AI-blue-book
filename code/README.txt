ThePriceIsRight: Predicting Prices with Product Images README
Authors: Edward Chou, Richard Yang, Steven Chen

============Dependencies============:
Python 3.5
NumPy: https://github.com/numpy/numpy
Matplotlib: https://github.com/matplotlib/matplotlib
scikit-learn: https://github.com/scikit-learn/scikit-learn
TensorFlow: https://github.com/tensorflow/tensorflow
Keras: https://github.com/keras-team/keras
Keras-vis: https://github.com/raghakot/keras-vis
Jupyter Notebooks: https://github.com/jupyter/jupyter

============Setup============:
After installing the required dependencies, create a new directory structure as follows, and extract the contents of code.zip and data.zip.
--ThePriceIsRight/
----code/
------Contents of code.zip
----datasets/
------Contents of data.zip

============Files============:
All of our code for this project is documented in IPython notebooks to make reading our code and reproducing our experiments easier. All of the output from our code should come attached with these notebooks. To run a notebook, first launch Jupyter, navigate to our code directory, and click a notebook to start it. 

The Main.ipynb file explains in detail what each of our notebooks accomplish. We briefly highlight what each notebook is in this README. 
scraping/ - This directory contains the code and output for our Bicycle Blue Book scraper.
Average_Baseline.ipynb - Produces the baseline regression model mentioned in our final report.

For the bikes dataset:
Bikes_Linear_Regression_CNN_Features.ipynb - Linear regression model using CNN-extracted features
Bikes_Linear_Regression_HOG_Features.ipynb - Linear regression model using HOG features
Bikes_SVM.ipynb - Price segment classification model using SVM
Bikes_TransferLearning_MobileNet.ipynb - Transfer learning model by fine-tuning MobileNet (CS229)
Bikes_TransferLearning_VGG16_Classification.ipynb - Transfer learning model for classification by fine-tuning VGG16 (CS229)
Bikes_TransferLearning_VGG16_Regression.ipynb - Transfer learning model for regression by fine-tuning VGG16 (CS229)
Bikes_Visualization_SaliencyMap_CAM.ipynb - Saliency map and class activation map visualization techniques for CNN models (CS229)
Bikes_Visualization_Sliding_Window.ipynb - Sliding window visualization technique for CNN models (CS229)

For the cars dataset:
Cars_Linear_Regression_CNN_Features.ipynb - Linear regression model using CNN-extracted features
Cars_Linear_Regression_HOG_Features.ipynb - Linear regression model using HOG features
Cars_SVM.ipynb - Price segment classification model using SVM
Cars_TransferLearning_MobileNet.ipynb - Transfer learning model by fine-tuning MobileNet (CS229)
Cars_TransferLearning_VGG16_Classification.ipynb - Transfer learning model for classification by fine-tuning VGG16 (CS229)
Cars_TransferLearning_VGG16_Regression.ipynb - Transfer learning model for regression by fine-tuning VGG16 (CS229)
Cars_Visualization_SaliencyMap_CAM.ipynb - Saliency map and class activation map visualization techniques for CNN models (CS229)
Cars_Visualization_Sliding_Window.ipynb - Sliding window visualization technique for CNN models (CS229)

CDF_Plots.ipynb - Generates the CDF plots for prices in our dataset
Clean_Bikes.ipynb - Preprocessing for the bikes dataset
Clean_Cars.ipynb - Preprocessing for the cars dataset
Filter_Bikes.ipynb - Additional preprocessing for the bikes dataset
Hyperparameter_Tuning_CNN_ResNet.ipynb - Hyperparameter tuning for CNN models (CS229)
Main.ipynb - Description of our project, and the main notebook to guide readers through
New_Network.ipynb - Implementation of our novel architecture, "PriceNet" (CS229)
New_Network_Classification.ipynb - PriceNet for classification (CS229)
*.npy - These are Numpy array files to store our experiment variables. We store our train/test set splits to remain consistent across all our models, and also the features extracted from HOG/CNN, and the principal components of those features after running PCA. 