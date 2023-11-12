from flask import Flask, render_template, request, redirect
import base64
import numpy as np
import cv2 as cv

import src.eigenface.Service.sign_up as signup
import src.eigenface.Service.sign_in as signin


app = Flask(__name__)

signupRoute = "signupImage.png"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/shot", methods=["GET", "POST"])
def shot():
    if request.method == "POST":
        img_data = request.data.decode('utf-8')
        _, base64_data = img_data.split(',', 1)

        # Decode the Base64 data into binary data
        image_data = base64.b64decode(base64_data)
        # Generate a unique filename for the saved image, or you can use a fixed filename
        # Ensure the 'static' folder exists in your Flask app's directory
        filename = 'src/eigenface/Service/' + signupRoute

        with open(filename, 'wb') as f:
            f.write(image_data)

    return "done"


@app.route("/signin")
def sign_in():
    return render_template("signin.html")


@app.route("/takeSignin", methods=["GET"])
def takeSignin():
    signinSuccess = signin.sign_in()
    return signinSuccess


@app.route("/signup")
def sign_up():
    return render_template("signup.html")


@app.route("/saveUserSignup", methods=["POST"])
def saveUserSignup():
    try:
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        signup.sign_up(first_name, last_name)
        return "Sign up success! Next time I'll remember you :)"
    except Exception as err:
        print(err)
        return "Error occurred when you tried to sign up!"


@app.route("/success/<name>")
def success_page(name):
    # This function serves the success HTML page
    return render_template('successPage.html', content=name)


@app.route("/failure")
def failure_page():
    # This function serves the failure HTML page
    return render_template('failurePage.html')


if __name__ == '__main__':
    app.run()
