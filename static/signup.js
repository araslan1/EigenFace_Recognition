rootURL = "http://127.0.0.1:5000"
window.addEventListener("load", init)

let stream;
let cameraPreview = document.getElementById("cameraPreview")

function init(){
    getVideoCam()
    const shot = document.getElementById('shot')
    shot.addEventListener('click', takeSnapshot)
    const submitButton = document.querySelector('#signUpForm button[type="submit"]');
    submitButton.addEventListener('click', takeSignUp)
}

async function statusCheck(response) {
    if (!response.ok) {
        console.log("status check not ok")
        throw new Error(await response.text())
    }
    console.log("status check ok")
    return response
}

function getVideoCam() {
    console.log("entered video cam")
    navigator.mediaDevices.getUserMedia({ video: true })
    .then((userMediaStream) => {
        stream = userMediaStream;
        cameraPreview.srcObject = userMediaStream;
        createFaceOverlay();
    })
    .catch((error) => {
        console.error("Error accessing camera:", error);
    });
}

function takeSnapshot(){
    if (stream) {
        // Use html2canvas to capture the content of a specific HTML element (e.g., the video element)
        html2canvas(cameraPreview)
            .then((canvas) => {
            // Convert the canvas to a data URL and display it or save it as needed
            const imgData = canvas.toDataURL("image/png");
            const imageElement = new Image();
            imageElement.src = imgData;
            window.alert("Snapshot taken!")
            document.body.appendChild(imageElement);
            console.log(imgData)
            fetch(rootURL + "/shot", {
                method : "POST",
                body : imgData
            }).then().catch(() => alert("Error occurred"))
        });
    }
}

function takeSignUp(event){
    event.preventDefault();

    // Get the form element
    const signUpForm = document.querySelector('#signUpForm');

    // Access individual input fields by name or ID
    const firstName = signUpForm.querySelector('#firstName').value;
    const lastName = signUpForm.querySelector('#lastName').value;


    // Prepare the data to send in the fetch request
    const formData = new FormData();
    formData.append('firstName', firstName);
    formData.append('lastName', lastName);

    // Make a fetch request to save user signup data
    fetch(rootURL + "/saveUserSignup", {
        method: 'POST',
        body: formData
    })
    .then(statusCheck)
    .then(resp => resp.text())
    .then((responseData) => alert(responseData))
    .catch(() => alert("Error occurred"));
}
