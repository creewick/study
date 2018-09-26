var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementsByClassName("scroll-hide")[0].className = "scroll-hide open";
  } else {
    document.getElementsByClassName("scroll-hide")[0].className = "scroll-hide";
  }
  prevScrollpos = currentScrollPos;
} 