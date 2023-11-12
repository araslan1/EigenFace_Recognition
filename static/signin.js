rootURL = "http://127.0.0.1:5000"
window.addEventListener("load", init)

let stream
let cameraPreview = document.getElementById("cameraPreview")


function init(){
    getVideoCam()
    const shot = document.getElementById('shot')
    shot.addEventListener('click', takeSnapshot)
    const submitButton = document.querySelector('#signUpForm button[type="submit"]');
    submitButton.addEventListener('click', takeSignin)
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
//        createFaceOverlay();
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
//            document.body.appendChild(imageElement);
//            console.log(imgData)
            fetch(rootURL + "/shot", {
                method : "POST",
                body : imgData
            }).then().catch(() => alert("Error occurred"))
        });
    }
}

function takeSignin(event) {
    event.preventDefault();
    fetch(rootURL + "/takeSignin")
        .then(statusCheck)
        .then(resp => resp.text())
        .then(data => {
//            print("hello!")
//            print(data)
            if (data.length === 0) {
                // Redirect to failure page
                window.location.href = rootURL + "/failure";
            } else{
                // Redirect to success page
                window.location.href = rootURL + "/success/" + data;
            }
        })
        .catch(() => alert("Error occurred"));
}


