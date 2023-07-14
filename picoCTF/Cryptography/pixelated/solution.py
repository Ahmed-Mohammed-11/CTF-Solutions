import numpy as np
import sys, os


# we will use keras and tensorflow instead of Pillow/PIL
# Open images
im1 = open("scrambled1.png", "rb")
im2 = open("scrambled2.png", "rb")

# Make into Numpy arrays
im1np = np.array(im1)
im2np = np.array(im2)

# Add images
result = im2np + im1np

# Save result
result = write("result.png", result)
