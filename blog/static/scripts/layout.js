const menuButton = document.querySelector(".menu-button");
const hiddenMenu = document.querySelector(".hidden-menu");
const closeButton = document.querySelector(".close-button");
const navLinks = document.querySelectorAll(".nav-link");

menuButton.addEventListener("click", () => {
  hiddenMenu.style.transform = "translateX(0)";
});

closeButton.addEventListener("click", () => {
  hiddenMenu.style.transform = "translateX(200em)";
});
navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    hiddenMenu.style.transform = "translateX(200em)";
  });
});

const contactLink = document.querySelector(".contact-link");
const contactPopUp = document.querySelector(".contact-pop-up");
contactLink.addEventListener("click", () => {
  if (contactPopUp.style.opacity !== "1") {
    contactPopUp.style.opacity = "1";
  }
});
const body = document.querySelector("body");
body.addEventListener("click", (e) => {
  if (contactPopUp.style.opacity === "1" && e.target !== contactLink) {
    contactPopUp.style.opacity = "0";
  }
});
