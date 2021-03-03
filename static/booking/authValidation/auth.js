function validate() {
  const name = document.getElementById("user_name").value;
  const email = document.getElementById("user_email").value;
  const number = document.getElementById("user_number").value;
  const password = document.getElementById("user_password").value;
  const passwordAgain = document.getElementById("user_password_again").value;
  if (
    name === "" ||
    email === "" ||
    number === "" ||
    password === "" ||
    passwordAgain === ""
  ) {
    alert("You can't keep any empty fields");
    return false;
  } else if (email.indexOf("@") == -1 || email.indexOf(".") == -1) {
    alert("Invalid Email");
    return false;
  } else if (number.toString().length != 10) {
    alert("Enter correct number");
    return false;
  } else if (password.length < 8 || passwordAgain.length < 8) {
    alert("Your password length should be minmum 8");
    return false;
  } else if (password != passwordAgain) {
    alert("Your both the passwords are not same");
    return false;
  } else {
    return true;
  }
}

function validateSignin() {
  const email = document.getElementById("user_email").value;
  const password = document.getElementById("user_password").value;
  if (email === "" || password === "") {
    alert("You can't keep any empty fields");
    return false;
  } else {
    return true;
  }
}
