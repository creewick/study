var links = document.getElementsByClassName("page-link");

links.forEach(element => {
    if (document.URL.indexOf(element.href) > -1)
        element.className += ' selected';
});
