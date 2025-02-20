# ProjCamSync

This repository provides python code to synchronize camera (GS3-U3-32S4C-C) and projector (DLP LightCrafter 4500). The main purpose is to hardware synchronization between camera and projector but it also provides camera capture code without trigger mode as well.

I have referred to several documents to implement these code and hardware-synchronize the prototypes.

- Cables to synchronize DLP projector (DLP LightCrafter 4500) [Synchronize projector](https://www.ti.com/lit/an/dlpa036b/dlpa036b.pdf?ts=1740016719227&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FDLPC350)

- Cables to synchronize camera (GS3-U3-32S4C-C) [Synchronize camera](https://www.teledynevisionsolutions.com/support/support-center/application-note/iis/configuring-synchronized-capture-with-multiple-cameras/)

- Spinnaker programmer's guide [Spinnaker guide](https://softwareservices.flir.com/Spinnaker/latest/_programmer_guide.html)


# Install

You need to previously install [SDK Spinnaker](https://www.teledynevisionsolutions.com/ko-kr/products/spinnaker-sdk/?model=Spinnaker%20SDK&vertical=machine%20vision&segment=iis) to run this code.

Also, refer to [DLP4500LightCrafter](https://github.com/shshin1210/DLP4500LightCrafter) to run ```main.py```.

Please make sure each files are placed as :

```
cam_pysping.py
cmaera.py
main.py
constants.py

pyrafter4500
|-- pycrafter4500.py
```


# Usage

```cam_pyspin.py``` includes functions to define several camera's setting. You may modify / add other functions based on the spinnaker documents. 

Reminder : some arguments are in ```constants.py```

## cam_pyspin.py

1. ROI

2. Image format

3. White balancing

4. Gain

5. Gamma

6. Exposure

7. Binning

8. Trigger mode

9. Acquisition mode

## main.py

To synchronize projector and camera, use ```main.py``` and ensure the trigger mode is True.

## camera.py

We also provide single capture camera setting in ```camera.py```. Please ensure the trigger mode is False.
