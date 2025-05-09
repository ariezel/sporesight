# SporeSight 
**Real-Time Identification of Pollen Development Stages Using Computer Vision Techniques**  
  
Authored by **Ariezel M. Bautista** and **Dr. Val Randolf M. Madrid**

## Installation
[1] Clone the repository
```
git clone https://github.com/ariezel/sporesight.git
```
>Please ensure to have Python installed before running this code

[2] Install the requirements
```python
pip install -r requirements.txt
```

[3] Download the appropriate **ONNX model** from this [GDrive](https://drive.google.com/file/d/1sQwGXEBRTgwTPM9AR27Exm4nQ-WUKxmy/view?usp=drive_link) and prepare a **classes.txt** file containing the list of classes

[!] This is the RTSP Link of the WiFi camera. This must hardcoded in the application.
```python
rtsp://192.168.7.1:554/axis-media/media.amp?streamprofile=Quality
```
> For testing purposes, the stream URL is currently set to **0**

## Usage
[1] Run the following command ``` python main.py ``` (in Windows) or ```python3 main.py``` (in MacOS)

[2] Provide **[model_name].onnx**, **classes.txt**, and your preferred **confidence score** in the **Configuration Section**

[3] Start the camera in the **Camera View Section** before pressing the Detect button

[4] Detections made can be reviewed, saved, and discarded. The detected images and a text file containing the inferences will be saved in the _./detections_ folder.

[5] The **Analytics Section** will show all detections made (or detections present in the _./detections_ folder) 



