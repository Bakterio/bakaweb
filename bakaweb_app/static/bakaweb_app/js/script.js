var ShowPasswordCheckbox = document.getElementById("password-input")
var PasswordEye = document.getElementById("PasswordEye")
var SlashPasswordEye = document.getElementById("SlashPasswordEye")
var idk = document.getElementsByClassName("fa-eye")
var idk2 = document.getElementsByClassName("fa-eye-slash")

function ZmenTypInputu() {
    if (ShowPasswordCheckbox.type === "password") {
        ShowPasswordCheckbox.type = "text";
        console.log("1")
            // idk.style.display = "block";
            // idk2.style.display = "none";
        idk.classList.add('displaynone')
        console.log("2")
    } else {
        ShowPasswordCheckbox.type = "password";
        // idk.style.display = "none";
        // idk2.style.display = "block";
    }
}