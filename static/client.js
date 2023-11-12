rootURL = "http://127.0.0.1:5000"
window.addEventListener("load", init)
let stream
let cameraPreview = document.getElementById("cameraPreview")
let signUpForm = document.getElementById('signUpForm');

function init() {
    const signIn = document.getElementById('signIn')
    signIn.addEventListener('click', toSignIn)

    const signUp = document.getElementById("signUp")
    signUp.addEventListener('click', toSignUp)
    // Now you can use the submitButton variable to manipulate the button, add event listeners, etc.

}

async function statusCheck(response) {
    if (!response.ok) {
        console.log("status check not ok")
        throw new Error(await response.text())
    }
    console.log("status check ok")
    return response
}


function toSignIn() {
    window.location.href = rootURL + "/signin";
     fetch(rootURL + "/signin")
        .then(statusCheck)
        .then(() => {
            window.location.href = rootURL + "/signin";
        })
        .catch(() => alert("Error occurred"))
}

function toSignUp() {
    fetch(rootURL + "/signup")
        .then(statusCheck)
        .then(() => {
            window.location.href = rootURL + "/signup";
        })
        .catch(() => alert("Error occurred"))
}


