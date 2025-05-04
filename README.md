# SporeSight 
**Real-Time Identification of Pollen Development Stages Using Computer Vision Techniques**  
  
Authored by **Ariezel M. Bautista** and **Dr. Val Randolf M. Madrid**

## Installation
Description
```bash



```

## Usage
[1] Install the application requirements
```python
pip install -r requirements.txt
```

[2] Install [Docker](https://www.docker.com/products/docker-desktop/) to access the Triton Inference Server

[4] Run the following commands on the terminal.

```
docker build -t triton-with-opencv .
```

```
docker run --rm -p 8000:8000 -p 8001:8001 -p 8002:8002 -v ${PWD}/model_repository:/models triton-with-opencv tritonserver --model-repository=/models --log-verbose=1 
```

[!] This is the XPCAM1080PHB RTSP Link. This will be hardcoded in the application.
```python
rtsp://192.168.7.1:554/axis-media/media.amp?streamprofile=Quality
```





