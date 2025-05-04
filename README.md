# SporeSight 
**Real-Time Identification of Pollen Development Stages Using Computer Vision Techniques**  
  
Authored by **Ariezel M. Bautista** and **Dr. Val Randolf M. Madrid**

## Installation
Description`
```bash



```

## Usage
Description
```python

rtsp://192.168.7.1:554/axis-media/media.amp?streamprofile=Quality

yolo export model=model.pt format=onnx dynamic=True opset=16
    
docker build -t triton-with-opencv .

docker run --rm -p 8000:8000 -p 8001:8001 -p 8002:8002 -v ${PWD}/model_repository:/models triton-with-opencv tritonserver --model-repository=/models --log-verbose=1 

```



