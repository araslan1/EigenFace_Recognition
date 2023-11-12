import cv2
import numpy as np
import os


def process_img(file_name, i):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    grayIMG = cv2.imread(file_name, 0)
    croppedFace = []
    faces = face_cascade.detectMultiScale(grayIMG, 1.25, 5, minSize=(200, 200))
    for (x, y, w, h) in faces:
        cv2.rectangle(grayIMG, (x, y), (x + w, y + h), (255, 0, 0), 5)
        croppedFace = grayIMG[y + 6: y + h - 6, int(x + w / 6): int(x + w - (w / 6))]

    if len(croppedFace) == 0:
        print("error couldn't find a face")
        print(file_name)
    else:
        croppedFace = cv2.resize(croppedFace, (135, 165))
        pixel = 0
        for row in range(125, 165):
            value = int(pixel)
            croppedFace[row, :value] = 0
            croppedFace[row, 135 - value:] = 0  # Set the last 'pixel' columns to 0
            pixel += 0.75
        # Make test picture
        # cv2.imwrite("croppedFace" + str(i) + ".png", croppedFace)

        croppedFace = np.array(croppedFace).flatten()
        # Create a boolean mask for non-zero values
        non_zero_mask = croppedFace != 0
        # Use boolean indexing to keep only non-zero values
        croppedFace = croppedFace[non_zero_mask]

        newCroppedFace = croppedFace[0:20000]

        return newCroppedFace / 255

    return []


def sign_up(firstName, lastName):
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

    # process image user signed up with
    cropped_face = process_img(image_path, 99)
    if len(cropped_face) == 0:
        print("ERROR IMAGE COULDN'T be FOUND!")
        return
    # test print statement for success
    print("cropped face success!")

    # load all files with paths previously declared
    U = np.load(eigen_space_relative_path)
    keys = np.load(user_keys_relative_path)
    names = np.load(name_keys_relative_path)
    average = np.load(average_relative_path)
    cropped_face = cropped_face - average
    Ukey = cropped_face @ U

    # add new user to the database, add their user key
    new_keys = []
    for k in range(0, keys.shape[0]):
        new_keys.append(keys[k, :])
    new_keys.append(Ukey)
    new_keys = np.array(new_keys)
    # save user to database
    np.save(user_keys_relative_path, new_keys)
    # add user's name to names database and save
    new_names = []
    for k in range(0, names.shape[0]):
        new_names.append(names[k])
    new_names.append(firstName + " " + lastName)
    new_names = np.array(new_names)
    np.save(name_keys_relative_path, new_names)

# MANUAL TESTING
# sign_up("Adam", "Raslan")
# cwd = os.getcwd()
# image_relative_path = str("blake.png")
# image_path = os.path.join(cwd, image_relative_path)
# process_img(image_path, 99)
