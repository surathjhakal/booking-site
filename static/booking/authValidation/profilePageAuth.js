function validate() {
  const firstName = document.getElementById("user_firstName").value;
  const lastName = document.getElementById("user_lastName").value;
  const gender = document.getElementById("user_gender").value.toLowerCase();
  //   const location = document.getElementById("user_location").value;
  const postal_code = document.getElementById("user_postal_code").value;

  if (firstName === "" || lastName === "") {
    alert("You can't keep name fields empty");
    return false;
  } else if (postal_code != "" && postal_code.toString().length != 6) {
    alert("Enter correct postal code, the size should be 6");
    return false;
  } else if (
    gender != "male" ||
    gender != "female" ||
    gender != "transgender"
  ) {
    alert("You have entered something incorrect in the gender place");
    return false;
  } else {
    return true;
  }
}
