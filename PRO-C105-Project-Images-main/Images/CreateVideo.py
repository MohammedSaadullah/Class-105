import os
import cv2

# Set a path for the Images folder
path = "Images/"

# Create a list variable named Images = [ ]
Images = [ ]

# Using for loop to check each file in the folder using os.listdir(path)
for file in os.listdir(path):
    # For each file name, use os.splitext(file) to separate the name and extension from a file name.
    name, extension = os.path.splitext(file)
    
    # Create an if condition to check if the extension of the file matches with the image extension.
    if extension == '.jpg' or extension == '.png':
        # Create a variable file_name by concatenating the path “/” and file name(Includes both name and extension).
        file_name = path + name + extension
        
        # Use print(file_name) to make sure filenames are formed correctly.
        print(file_name)
        
        # Add each file in the images list using .append()
        Images.append(file_name)

# Create a variable count to store len(images)
count = len(Images)

# Create a variable named frame to read the first image from the images list.
frame = cv2.imread(Images[0])

# Use frame.shape to capture width, height & Channels
width, height, channels = frame.shape

# Create a tuple variable size using width, height.
size = (width, height)

# Use print(size) to check the result.
print(size)

# Create a variable out.
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Create a for loop to add images to a videowriter.
for i in range(0, count-1):
    # Use cv2.imread() to reach each image
    img = cv2.imread(Images[i])
    
    # Add the image in Video using out.write()
    out.write(img)

# Print a message to know the video is complete as print(“Done”)
print("Done")

# Release the VideoWriter
out.release()

# Close all windows
cv2.destroyAllWindows()