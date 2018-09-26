var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  var menu = document.getElementsByClassName("scroll-hide")[0];

  if (prevScrollpos > currentScrollPos) {
    menu.className = "menu wrapper scroll-hide open";
  } else {
    menu.className = "menu wrapper scroll-hide";
  }

  if (pageYOffset > 0) {
    menu.style.boxShadow = "0 5px 20px -15px";
  } else {
    menu.style.boxShadow = "none";
  }
  
  prevScrollpos = currentScrollPos;
} 