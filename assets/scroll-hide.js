var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementsByClassName("scroll-hide")[0].style.top = "62px";
    document.getElementsByClassName("scroll-hide")[0].style.backgroundColor = "rgba(255, 255, 255, 0.8)";
    document.getElementsByClassName("site-header")[0].style.backgroundColor = "rgba(255, 255, 255, 0.8)";

  } else {
    document.getElementsByClassName("scroll-hide")[0].style.top = "8px";
    document.getElementsByClassName("scroll-hide")[0].style.backgroundColor = "white";
    document.getElementsByClassName("site-header")[0].style.backgroundColor = "white";
  }
  prevScrollpos = currentScrollPos;
} 