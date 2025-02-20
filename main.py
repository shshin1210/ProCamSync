import pycrafter4500

import cv2
import os
import cam_pyspin
import constants
import datetime
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import usb.util

import numpy as np

import PySpin

# Total images
total_imgs = 100

# output directory
output_dir = 'your directory to save captured images'

# Initialize camera system
system = PySpin.System.GetInstance()
cam_list = system.GetCameras()
num_cameras = cam_list.GetSize()

# Power on projector
pycrafter4500.power_up()

for i in range(num_cameras):
    camera = cam_list[i]
    camera.Init()
    print(f"Camera {i}: {camera.DeviceModelName()}")

    # Configure camera with trigger enabled
    cam_pyspin.configure_cam(camera, constants.PIXEL_FORMAT, constants.SHUTTER_TIME*1e3, constants.BINNING_RADIUS, roi=None, Trigger=True)
    camera.BeginAcquisition()

# Start pattern projection
pycrafter4500.pattern_sequence_final(
    input_mode='pattern',
    input_source='flash',
    num_pats=8,
    trigger_type='pattern_trigger_mode1',
    exposure_period=100000,
    frame_period=100000,
    bit_depth=[1,1,1,1,1,1,1,1],
    led_color=0b111,
    trig_type=0
)

print('pattern projecting ...')

image_count = 0
image_list_cam1 = []

print('start capturing...')
start_time = time.time()
while True:
    im_cam1 = cam_pyspin.capture_im(cam_list[0], constants.PIXEL_FORMAT, Trigger=True)
    # debug
    image_list_cam1.append(im_cam1)
    
    image_count += 1
    
    # Stop condition
    if image_count >= total_imgs:
        break
    
print('total time for %03d images: %f (s)'%(image_count, time.time() - start_time))
print('fps : %d'%(total_imgs/( time.time() - start_time)))
print('%02d number of images captured'%image_count)

for k in range(image_count):
    cv_image_cam1 = (image_list_cam1[k] * 65535).astype(np.uint16)

    # Save captured image
    filename_cam1 = f"{output_dir}/capture_{k:04d}.png"
    cv2.imwrite(filename_cam1, cv2.cvtColor(cv_image_cam1, cv2.COLOR_RGB2BGR))

print('%02d number of images saved'%image_count)

# Power down projector
pycrafter4500.power_down()

# Release cameras
for camera in cam_list:
    camera.EndAcquisition()
    camera.DeInit()

# Release system
cam_list.Clear()
# system.ReleaseInstance()