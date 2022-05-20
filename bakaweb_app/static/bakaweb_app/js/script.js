const ShowPasswordCheckbox = document.getElementById("password-input");

function ZmenTypInputu() {
    if (ShowPasswordCheckbox.type === "password") {
        ShowPasswordCheckbox.type = "text";
    } else {
        ShowPasswordCheckbox.type = "password";
    }
}

function logout() {
    s = NewSession();
    s.Item('user') = null;
    s.Item('url') = null;
    s.Item('pw') = null;
}
