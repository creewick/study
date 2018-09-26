var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementsByClassName("scroll-hide")[0].className = "menu wrapper scroll-hide open";
  } else {
    document.getElementsByClassName("scroll-hide")[0].className = "menu wrapper scroll-hide";
  }
  prevScrollpos = currentScrollPos;
} 