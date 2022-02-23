# Animal Recognition Website Application

This project is a website application of 16 different animal recognition.
The system contains two parts: designing a website, training a Convolutional 
Neural Network (CNN) network, and making connections between the website and trained CNN.

First, a basic webpage is designed, containing 16 different animal images to 
inform the user about the used animal classes.
There are also two buttons for uploading images and making prediction.

<img src="/images/image1.png" width="400">

Then, a CNN is trained with the dataset that contains 16 different animal images.
Finally, the trained CNN and the designed webpage are connected to each other 
to transfer the uploaded images.

The application runs as in the following:
* The user uploads an image to the website.
* The trained CNN use it as an input image and makes a prediction.
* The predicted result returns to the webpage for visualization.

<img src="./images/image2.png" width="400">

# Website Design
Webpage file `index.html` is located in the `templates` folder if you would like to modify the webpage.

# Training
In order to train the network, you need to have a dataset consisting of animal images.
A few datasets in Kaggle are utilized to train the model.
You can do a new training using `training.ipynb`.
Make sure the model name is `saved_model.h5` when you save the model.

# Testing
In order to test your custom images, [download]() the pre-trained model.

You can run the code by following command:
    
    python website.py

