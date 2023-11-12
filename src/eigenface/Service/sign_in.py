import numpy as np
from src.eigenface.Service.sign_up import process_img
from numpy import linalg as LA
import os

# the threshold is currently set to 11.0
threshold = 11.0
def sign_in():
    # get working path of 5 files, training files, database files, and user input image
    cwd = os.getcwd()
    image_path = cwd + "/src/eigenface/Service/signupImage.png"  # user's input image
    eigen_space_relative_path = cwd + "/src/eigenface/Training/eigen_space.npy"  # training
    user_keys_relative_path = cwd + "/src/db/user_keys.npy"  # database
    name_keys_relative_path = cwd + "/src/db/name_keys.npy"  # database
    average_relative_path = cwd + "/src/eigenface/Training/average_face.npy"  # training

    # MANUAL TESTING
    # image_path = cwd + "/signupImage.png"
    # eigen_space_relative_path = cwd + "/../Training/eigen_space.npy"
    # user_keys_relative_path = cwd + "/../../db/user_keys.npy"
    # name_keys_relative_path = cwd + "/../../db/name_keys.npy"
    # average_relative_path = cwd + "/../Training/average_face.npy"

    # load all files
    U = np.load(eigen_space_relative_path)
    keys = np.load(user_keys_relative_path)
    names = np.load(name_keys_relative_path)
    average = np.load(average_relative_path)
    cropped_face = process_img(image_path, 99)
    cropped_face = cropped_face - average
    Ukey = cropped_face @ U

    # check if there's a key match
    for k in range(0, keys.shape[0]):
        print(LA.norm(Ukey - keys[k, :]))
        if LA.norm(Ukey - keys[k, :]) < threshold:  # if its key matches any other image's key
            print("MATCH FOUND!")
            return names[k]

    return ""
