# SporeSight 
**Real-Time Identification of Pollen Development Stages Using Computer Vision Techniques**  
  
Authored by **Ariezel M. Bautista** and **Dr. Val Randolf M. Madrid**

## Installation
[1] Install the application requirements
```python
pip install -r requirements.txt
```

[2] Install [Docker](https://www.docker.com/products/docker-desktop/) to access the Triton Inference Server

[3] Download the model (model.onnx) from this [GDrive](https://drive.google.com/file/d/1sQwGXEBRTgwTPM9AR27Exm4nQ-WUKxmy/view?usp=drive_link) and put the YOLOV5 model inside model_repository/yolov5/1/
```
├───model_repository
│   └───yolov5
│       └───1
            └───[INSERT HERE]
```
- Please ensure that model names are renamed to *model.file_extension* as per Triton Inference Server requirements
- Configuration files must be edited depending on the model used


[4] Run the following commands on the terminal.

```
docker build -t triton-with-opencv .
```

```
docker run --rm -p 8000:8000 -p 8001:8001 -p 8002:8002 -v ${PWD}/model_repository:/models triton-with-opencv tritonserver --model-repository=/models --log-verbose=1 
```

[!] This is the XPCAM1080PHB RTSP Link. This is hardcoded in the application.
```python
rtsp://192.168.7.1:554/axis-media/media.amp?streamprofile=Quality
```

## Installation
Description
```bash

```





