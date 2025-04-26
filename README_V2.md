# CloudInterp
Interpolate satellite cloud images into smooth animations. 

**CloudInterp** is a Python tool designed to interpolate satellite cloud images and generate smooth transition animations. By processing a time series of satellite imagery, it creates continuous `.gif` or `.mp4` videos, ideal for meteorological visualization, scientific communication, or educational use.
Now, We can use **OpenCV** to interpolate between images. The core role is PyScript.

## Quick Start
 Python Version = 3.9
### 🛠 Launch http server

```bash
cd PyScript
python http_server.py
```

### 🚀 Open Browser
#### Type url on browser
```bash
http://127.0.0.1:8080/interp.html
```
#### Select first image from `images` file folder.
#### Select second image from `images` file folder.
#### Click `interp` button

### Effect
We can see that the cloud move slowly. Without interpolation, the clouds will jump abruptly.

## Next Step
Use some complex method and make the effect natural.
