import cv2
import numpy as np
import os
import cam_pyspin
import constants
import datetime
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import PySpin


# initialize camera
# singleton reference to system obj
system = PySpin.System.GetInstance()
# list of cam from sys
cam_list = system.GetCameras()
# number of cam
num_cameras = cam_list.GetSize()

for i in range(len(cam_list)):
    camera = cam_list[i]
    camera.Init()

    print(camera.DeviceModelName())

    # setup camera                                  # 150
    cam_pyspin.configure_cam(camera, constants.PIXEL_FORMAT, constants.SHUTTER_TIME*1e3, constants.BINNING_RADIUS, roi = None, Trigger = False)

    # Begin acquiring images/ capturing images
    camera.BeginAcquisition()

    im = cam_pyspin.capture_im(camera, constants.PIXEL_FORMAT)
    
    cv_image = (im*65535).astype(np.uint16)
    
    output_dir = '%s/%s%s/' % (constants.SCENE_PATH, constants.SCENE_NAME, datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M')) # experiments/test/
    
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    # =================================================== NAME OF FILE ====================================================
    cv2.imwrite("%s/capture_%04d.png" % (output_dir, i), cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR))