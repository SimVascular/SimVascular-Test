'''This scripts tests reading in legacy segmentation files.
'''
import os
from pathlib import Path
import sv
import sys
import vtk

## Set some directory paths. 
script_path = Path(os.path.realpath(__file__)).parent
parent_path = Path(os.path.realpath(__file__)).parent.parent
data_path = parent_path / 'data'

try:
    sys.path.insert(1, str(parent_path / 'graphics'))
    import graphics as gr
except:
    print("Can't find the new-api-tests/graphics package.")

file_name = str(data_path / 'segmentation' / '0110_0001_groups-cm' / 'aorta')
# Bad file name to test error handling.
#file_name = str(data_path / 'segmentation' / '0110_0001_groups-cm' / 'aorta1')
print("Read SV legacy files: {0:s}".format(file_name))

# Read an SV segmentation group file from the contructor. 
if False:
    seg_series = sv.segmentation.Series(file_name, legacy=True)

# Read an SV segmentation group file using the 'read()' method.
else:
    seg_series = sv.segmentation.Series()
    seg_series.read(file_name, legacy=True)

num_times = seg_series.get_num_times()
print("Number of time points: {0:d}".format(num_times))

# Write the segmentation series to a file.
seg_series.write(str(script_path / "test-aorta-legacy.ctgr"))

## Create renderer and graphics window.
win_width = 500
win_height = 500
renderer, renderer_window = gr.init_graphics(win_width, win_height)

## Show contours.
for time in range(num_times):
    num_segs = seg_series.get_num_segmentations(time)
    print('Number of segmentations: {0:d} '.format(num_segs))
    for sid in range(num_segs):
        seg = seg_series.get_segmentation(sid, time)
        ctype = seg.get_type()
        #print('Segmentation type: {0:s}'.format(ctype))
        try:
            control_points = seg.get_control_points()
        except:
            control_points = []
        gr.create_segmentation_geometry(renderer, seg)

# Display window.
gr.display(renderer_window)
