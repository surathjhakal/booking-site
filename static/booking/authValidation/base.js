let data = document.getElementsByClassName("page")[0];
let dim = document.getElementsByClassName("dim")[0];
const navbar_profile = document.getElementsByClassName("navbar_profile")[0];
const navbar = document.getElementsByClassName("navbar")[0];
let show = false;
const path = window.location.pathname;
const body = document.getElementsByTagName("body")[0];

function showProfile() {
  if (path === "/") {
    if (show === true) {
      data.style.display = "none";
      dim.style.display = "none";
      navbar.style.background = "none";
      body.style.overflow = "visible";
      show = false;
    } else {
      dim.style.display = "flex";
      data.style.display = "flex";
      navbar.style.background = "rgba(31, 29, 29, 0.6)";
      show = true;
      body.style.overflow = "hidden";
    }
  } else {
    if (show === true) {
      data.style.display = "none";
      dim.style.display = "none";
      navbar.style.background = "#582c2c";
      show = false;
      body.style.overflow = "visible";
    } else {
      dim.style.display = "flex";
      data.style.display = "flex";
      navbar.style.background = "#582c2c";
      show = true;
      body.style.overflow = "hidden";
    }
  }
}
// console.log(window.location.pathname);
navbar_profile.addEventListener("click", showProfile);

function openPopup(data) {
  $("#movieHeading").text($(data).attr("movieName"));
  $("#movieRatingView").text($(data).attr("movieRating"));
  $("#openModal").trigger("click");
}

$("#paymentBtn").click(function () {
  $(".formData").val("");
});
