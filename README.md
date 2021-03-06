# Natural-Image-Classifier
This is a Deep Learning Python Web Application that will be used to identify the category of the image which is uploaded by the user.
The app can predict images belonging to the categories such as Airplane ,Car, Cat ,Dog , Flower ,Fruit , Motorbike and Person.
The web app is built using Flask Framework ; deployed in cloud using Heroku and is based on the working of Convolutional Neural Network

# Dataset and Modelling

We will be building a model that should be able to classify the image as Airplane ,Car, Cat ,Dog , Flower ,Fruit , Motorbike ,Person.
The model needs to be trained on the images of the above mentioned categories in order to learn the features of each category's image.
Here we are using images for the purpose of training  around 4376 images of Airplane ,Car, Cat ,Dog , Flower ,Fruit , Motorbike ,Person and around 1300 images as  test data for  the model to check its performance. We will be using a deep learning model to identify the category of the image.

Here we will be using Convolution Neural network where the model we will be building will have Convolution layers to extract features , Max Pooling layer to reduce spatial size,Batch Normalization layer and Dense layer to avoid overfitting.

We train this model on 30 epochs and then check for the accuracy and along with that plot the graph to check its performance. The model is achieving 87% accuracy on test samples.

After the computation and metrics we will save the model as a pickle file. The pickle will be useful when Flask Framework is used in order to predict which category the image uploaded by the user will belong to.

# Deployment
Then GUI was designed by the help of HTML/CSS and  bulit upon Flask Framework.

Programming Language used was Python.

The app was deployed in web with the help of Heroku.

![kisspng-flask-python-web-framework-bottle-microframework-django-5b3d0ba62504c0 3512153115307273341516](https://user-images.githubusercontent.com/76935226/140600271-dc46a85c-1f1e-406e-9231-4e8dd43cdf8f.jpg)
![image](https://user-images.githubusercontent.com/76935226/140600298-11b355f2-f0f1-453a-a860-a984817597b5.png)
![Heroku](https://user-images.githubusercontent.com/76935226/150635269-942c1bb7-f006-4e79-91d7-3894f9c44086.png)
![0_py5zo1OGahLBVM-o](https://user-images.githubusercontent.com/76935226/150635279-2fe7e103-ac79-4f91-a427-bf47508bd6c6.gif)


# Check out the App
https://naturalimage.herokuapp.com/

![Screenshot (148)](https://user-images.githubusercontent.com/76935226/140600398-4837be8f-1861-418b-be4e-a48c47a9b927.png)
![Screenshot (149)](https://user-images.githubusercontent.com/76935226/140600400-c47e9982-9fd6-4ce4-a002-381e764f1639.png)











