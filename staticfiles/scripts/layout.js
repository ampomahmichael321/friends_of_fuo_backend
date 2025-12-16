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
