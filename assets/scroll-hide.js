var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementsByClassName("scroll-hide")[0].style.top = "62px";
    document.getElementsByClassName("scroll-hide")[0].style.color = "white";

  } else {
    document.getElementsByClassName("scroll-hide")[0].style.top = "8px";
    document.getElementsByClassName("scroll-hide")[0].style.color = "black";
  }
  prevScrollpos = currentScrollPos;
} 