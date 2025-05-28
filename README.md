# Door-and-Window
Detecting doors and windows in blueprints

## Repository Structure
```Test``` ,
```Train``` and
```Valid```
folders have ```Images``` For storing the .jpg images and ```Labels``` For storing label classes of the images.


```app.py``` Is used for the backend tasks such as loading the model, accepting images and running the detection model on the image.

```best.pt``` Contains the trained weights of the YOLOv8 model that is used to detect doors and windows on sample images.

```data.yaml``` Is used for configuration of files.

```requirements.txt``` Is used by Render to setup requirements needed to run the ```app.py```


## Labelling

Bounding boxes have been annotated with two classes: **door** and **window** as mentioned in the ```classes.txt```

![ImageLabelling](https://github.com/user-attachments/assets/81fa327e-cc17-4296-805f-6b22fbb87f0d)

### Annotation

The annotation has been done as follows:
![Annotation](https://github.com/user-attachments/assets/a428991d-58ae-4f2e-a91e-bac1d03b21a7)


### Classes

The classes used are:

![Classes](https://github.com/user-attachments/assets/c62831ff-0e2b-40b0-bed5-98d8210c6dfa)

## Training

The model used here is ```YOLOv8``` and the training console after running 50 epochs looks like:

![Training](https://github.com/user-attachments/assets/27e1533d-ed77-4371-91b3-f36eb0412269)

### Setup for running it online

[Link to website](https://doors-and-windows-pfk1.onrender.com/docs)

Click the dropdown beside ```POST/detect``` and hit the ```Try it out``` button. Upload the **.jpg** or **.png** image and click ```Execute```. The result is displayed in JSON format.

### For curl

Run:
```curl -X 'POST' \
  'https://doors-and-windows-pfk1.onrender.com/detect' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@20.png;type=image/png'
```
Replace ```image/png``` with the path of the image

