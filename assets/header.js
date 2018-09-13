var links = document.getElementsByClassName("page-link");

for (var i = 0; i < links.length; i++) {
    if (document.URL.indexOf(links[i].href) > -1)
        links[i].className += ' selected';
};
