function requestDemo() {
    let formContents = document.getElementById("requestDemoForm").elements;
    let overlay = document.getElementById("requestDemoOverlay");

    console.log(formContents.nameField.value, formContents.emailField.value);

    // Show the "Thanks!" overlay
    overlay.style.display = "block";
}

export default requestDemo;