var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementsByClassName("scroll-hide")[0].style.top = "62px";
  } else {
    document.getElementsByClassName("scroll-hide")[0].style.top = "8px";
  }
  prevScrollpos = currentScrollPos;
} 