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

****Validation*****

The simulator was run after each calibration to see how well the vehicle stays around the track. There is only one spot that the vehicle fells off the track (the first curve). Additional data was collected from that curve to improve the model.

At the end of the process, the vehicle is able to drive autonomously around the track without completely leaving the road.

**** Final Model Architecture ****

The final model architecture is as follows:

![alt text][image1]







Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)

![alt text][image1]

####3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![alt text][image2]

I then recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle would learn to .... These images show what a recovery looks like starting from ... :

![alt text][image3]
![alt text][image4]
![alt text][image5]

Then I repeated this process on track two in order to get more data points.

To augment the data sat, I also flipped images and angles thinking that this would ... For example, here is an image that has then been flipped:

![alt text][image6]
![alt text][image7]

Etc ....

After the collection process, I had X number of data points. I then preprocessed this data by ...


I finally randomly shuffled the data set and put Y% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was Z as evidenced by ... I used an adam optimizer so that manually training the learning rate wasn't necessary.

