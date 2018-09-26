var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    
    document.getElementsByClassName("scroll-hide")[0].style.top = "62px";
    
    var links = document
      .getElementsByClassName("scroll-hide")[0]
      .getElementsByClassName("page-link");
    
      for (let i = 0; i < links.length; i++) {
        links[i].style.color = "black";
      }
  } else {
    document.getElementsByClassName("scroll-hide")[0].style.top = "8px";
   
    var links = document
      .getElementsByClassName("scroll-hide")[0]
      .getElementsByClassName("page-link");
  
    for (let i = 0; i < links.length; i++) {
      links[i].style.color = "white";
    }
  }
  prevScrollpos = currentScrollPos;
} 