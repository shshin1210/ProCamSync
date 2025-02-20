import datetime
import numpy as npp
from os.path import join

# camera
PATTERN_PATH = './patterns/graycode_pattern/'
EMIT_TIME = 0 # ms 
TRIGGER_TIME = 0 # msa
SHUTTER_TIME = 15 #3 # ms / 100ms는 0.1초 # 0.25 / 15 # CRF 90 ms / 3ms
PIXEL_FORMAT = "BayerGB16"

WAIT_TIME = 74 # ms

GAIN = 0  # this is log scale. /20 for conversion. 7.75db * 20, 0db - previous capture, for material capture
GAMMA = 1
BINNING_RADIUS = 2
NUM_BUFFERS = NUM_TRIGGERS = 71

# scene parameters
SCENE_PATH = './experiments'
SCENE_NAME = 'test'
LOG_FN = SCENE_PATH + '/logs/' + datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M') + '.txt'

# screen index
CAMERA_NUM = 0  # camera num
SCREEN_NUM = 1  # for projector

# debug
VERBOSE = True
SAVE_INTERM = False