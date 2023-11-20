# EigenFace_Recognition

Inspiration: 
I first read about eigenfaces being used for facial recognition from an article on twitter, and found it to be a very amazing way of applying linear algebra. So this was my attempt at finding eigenfaces for facial recognition.

# What it does: 
My project allows you to create an account merely by typing in your name and taking a snapshot of your face. For future logins, you merely take a picture of your face again and my program (ideally) will identify who you are and relay back on the screen the name you created your account with.

# Project Structure:

### src
- **python backend**
    - `db`: Database storing users' face information and their name in .npy files. Also contains files to view and clear the database.
    - `eigenface`: Main algorithm for eigenface implementation.
        - `Service`: Backend logic for "sign in" and "sign up" functions. `sign up` contains the logic for processing images.
        - `Training`: Contains `train.py` for training models, output files of the training process, and the `Pictures` directory for storing training images.

### static
- JavaScript and CSS files for each page. (Three pages: `/`, `/signup`, `/signin`)

### templates
- HTML templates for rendering the pages.

### main.py
- Server script for the project.

# How I built it:
I built the frontend of the application with javascript, CSS, HTML and the backend with flask. My model was trained in src/eigenface/Training/train.py. It was trained on pictures I got my friends to take on my computer in the Training/Pictures directory. I removed these pictures from the directory for safety purposes. For each image, it was processed using a pre-trained cascade classifier to detect frontal faces. The alternative was to merely draw a face cutout onto the web camera preview so that users could manually align their faces into the cutout. This cutout would be cropped and serve as my “face” that I would use for training. However, it seemed like a good option to use the classifier for user experience and easier testing of my program’s core functionality (recognition with eigenfaces). 

This method of face recognition builds upon linear algebra and the unique properties of matrices. To train the model, for each image in my training directory, I took the first n pixels (n = 20000) which are BGR values ranging from 0 to 255, converted to grayscale, and added these pixels to a new row in a matrix (call it M). M was thus an m x n matrix with m images and each image (row) has n pixels. I calculated the covariance matrix by taking the dot product of M and M transpose, and then I calculated the corresponding eigenvectors of the covariance matrix. These vectors capture the most significant patterns present in my set of faces. They might represent features like the angle of the jaw, the spacing of the eyes, or other facial characteristics. The bigger the value of the eigenvector, the more significant the facial feature is.

A single face can be broken down into a linear combination of these eigenvectors. The coefficient of each eigenvector depends on how prominent the facial feature is in the face.  
Projecting a face onto the subspace spanned by these eigenvectors gives us the best way to represent that face using these eigenvectors. The coefficients are used as a key to represent that face and will give us the ability to to recognize that face again in the future using these keys. Each face having a unique "key" or representation through these coefficients means that you can store or recognize faces based on these coefficients rather than the entire image. This key represents the most distinguishing facial characteristics from the dataset, enabling facial recognition.

# Problems and Future Improvements

There are many limitations to my project and the accuracy of using eigenfaces for facial recognition. For example, lighting, brightness levels, and other external factors can vary greatly among picture to picture. If a well lit picture is taken to signup, but you try to login in a darker room, the accuracy of the program dropped drastically. Even alternating between glasses and contacts made a huge difference in my program successfully recognizing my face. One possible future addition to make this a more robust program is to have multiple image signups. When you signup as a user, you take many images under many different conditions to help with future logins. 
