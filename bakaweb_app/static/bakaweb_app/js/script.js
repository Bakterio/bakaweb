const ShowPasswordCheckbox = document.getElementById("password-input");

function ZmenTypInputu() {
    if (ShowPasswordCheckbox.type === "password") {
        ShowPasswordCheckbox.type = "text";
    } else {
        ShowPasswordCheckbox.type = "password";
    }
}