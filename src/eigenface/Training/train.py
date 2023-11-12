import os
from numpy import linalg as LA
import numpy as np
import matplotlib.pyplot as plt
from src.eigenface.Service.sign_up import process_img

# Get the current working directory
cwd = os.getcwd()

# Specify the path to the "pictures" folder
pictures_folder = os.path.join(cwd, "pictures")

# List all files in the "pictures" folder
image_files = [f for f in os.listdir(pictures_folder) if os.path.isfile(os.path.join(pictures_folder, f))]


width = 135
height = 165
pixels = 20000
average = np.zeros(pixels)
imageCount = 0


Data = []
for image in image_files:
    image_relative_path = "Pictures/" + str(image)
    image_path = os.path.join(cwd, image_relative_path)
    croppedFace = process_img(image_path, imageCount)
    average = average + croppedFace
    Data.append(croppedFace)
    imageCount += 1


average = average/imageCount

Data = np.array(Data)

# normalize each image
for i in range(imageCount):
    Data[i, :] = Data[i, :] - average

Data = np.transpose(Data)

U, S, V = LA.svd(Data, full_matrices=False)  # false to only contain the most important eigenvectors
U = U[:, 0:100]
# 'U' are the left singular vectors (eigenvectors of the covariance matrix, ordered by their importance)

np.save('eigen_space.npy', U)
np.save('average_face.npy', average)


# MANUAL TESTING


# Keys = np.transpose(Data) @ U
# Multiply image data with our eigenvectors
# perform matrix multiplication, Keys is a matrix where each row corresponds to a training image
# ... and each column represents a coefficient indicating how much of each dominant eigenface is present in that image
# image_relative_path = str("signupImage.png")
# image_path = os.path.join(cwd, image_relative_path)
# croppedFace = process_img(image_path, imageCount)
# croppedFace = croppedFace - average
# TestKeys = croppedFace @ U
# output = []
# for k in range(0, imageCount):
#     output.append(LA.norm(TestKeys-Keys[k, :]))
#
# x = np.arange(imageCount)
#
# # Plot the results and label the x-axis with image labels
# plt.scatter(x, output)
# plt.xticks(x, image_files, rotation='vertical')  # Set x-axis labels to image labels
# plt.xlabel("Images")
# plt.ylabel("Recognition Score")
# plt.show()

