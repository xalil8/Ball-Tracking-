import pyrealsense2 as rs
import numpy as np
import cv2
import time
import datetime
import csv
import threading


"""
Mobirob Stohi
This script was written to log ASIC and projector temperatures of
Intel Realsense D435i and D430.

ref:
github.com/IntelRealSense/librealsense/issues/866#issue-278008036
github.com/IntelRealSense/librealsense/issues/1735#issuecomment-390840337
"""

# Configure depth and color streams...
# ...from Camera 1
pipeline = rs.pipeline()
config = rs.config()
config.enable_device('935322073125')
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)




colorizer = rs.colorizer()
decimation = rs.decimation_filter()
spatial = rs.spatial_filter()
temporal = rs.temporal_filter()
hole_filling = rs.hole_filling_filter()


# Start streaming from both cameras
cfg=pipeline.start(config)


dev = cfg.get_device()


depth_sensor = dev.first_depth_sensor()


try:

	while True:

		# Wait for a coherent pair of frames: depth and color
		frames = pipeline.wait_for_frames()
		depth_frame = frames.get_depth_frame()
		depth_to_disparity = rs.disparity_transform(True)
		disparity_to_depth = rs.disparity_transform(False)
		# Convert images to numpy arrays
		without_filter = np.asanyarray(depth_frame.get_data())
		# filtered = decimation.process(depth_frame)
		filtered = depth_to_disparity.process(depth_frame)
		#filtered = spatial.process(filtered)
		filtered = temporal.process(filtered)
		filtered = disparity_to_depth.process(filtered)
		filtered = hole_filling.process(filtered)
		colorized = np.asanyarray(colorizer.colorize(filtered).get_data())
		# Apply colormap on depth image (image must be converted to 8-bit per
		# pixel first)
		wo_filter_img = cv2.applyColorMap(cv2.convertScaleAbs(without_filter, None,0.5, 0), cv2.COLORMAP_BONE)
		decimated_colorized = cv2.applyColorMap(cv2.convertScaleAbs(colorized, None,0.5, 0), cv2.COLORMAP_BONE)
		# Stack both images horizontally
		# Get device temperature
		# Show images
		# cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
		cv2.imshow('Without Filter', wo_filter_img)
		cv2.imshow('Decimated and Colorized', decimated_colorized)
		cv2.waitKey(1)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break



finally:
	# Stop streaming
	pipeline.stop()
	cv2.destroyAllWindows()