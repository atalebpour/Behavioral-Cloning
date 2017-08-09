**Behavioral Cloning** 

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/Model.png "Model Visualization"
[image2]: ./examples/placeholder.png "Grayscaling"
[image3]: ./examples/placeholder_small.png "Recovery Image"
[image4]: ./examples/placeholder_small.png "Recovery Image"
[image5]: ./examples/placeholder_small.png "Recovery Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

---
***The project includes the following files:***

* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* README.md summarizing the results

***Submission also includes functional code.*** Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

***Model Architecture and Training Strategy***

The model consists of six convolution layers with 5x5, 3x3, and 1x1 filter sizes and depths between 24 and 128 (model.py lines ). The model is a modified version of the model introdced by NVIDIA to control their automated vehicle. The convolution layers are connected to three fully connected layers with 100, 50, 10, and 1 neurons.

Images were normalized and cropped (to increase the calibration speed). The model also utilizes a maxpooling layer and a dropout layer to reduce overfitting. 

The model was trained and validated on a diverse dataset (collected from multiple people) to ensure that the model was not overfitting. The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

The model used an adam optimizer, so the learning rate was not tuned manually.

****Training data****

Training data was chosen to keep the vehicle driving on the road. The data was collected from multiple drivers to diversify the training data. A combination of center, righ, and left side cameras were used to calibrate the data.

****Validation****

The simulator was run after each calibration to see how well the vehicle stays around the track. There is only one spot that the vehicle fells off the track (the first curve). Additional data was collected from that curve to improve the model.

At the end of the process, the vehicle is able to drive autonomously around the track without completely leaving the road.

****Final Model Architecture****

The final model architecture is as follows:

![alt text][image1]


****Creation of the Training Set & Training Process****

Data from multiple drivers were used to reduce the bias towards one single driver. Each driver did multiple laps around the track.
After the collection process, the total of 100708 number of data points were collected. 
