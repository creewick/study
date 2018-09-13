var links = document.getElementsByClassName("page-link");

for (var i = 0; i < links.length; i++) {
    if (links[i] != 'study/courses/' && document.URL.indexOf(links[i].href) > -1)
        links[i].className += ' selected';
    if (links[i] == 'study/courses/' && document.URL.endsWith(links[i].href))
        links[i].className += ' selected';
};
