var links = document.getElementsByClassName("page-link");

for (var i = 0; i < links.length; i++) {
    if (links[i].href != "https://creewick.github.io/study/courses/" 
        && document.URL.indexOf(links[i].href) > -1)
        links[i].className += ' selected';
    if (links[i].href == "https://creewick.github.io/study/courses/" 
        && document.URL.endsWith(links[i].href))
        links[i].className += ' selected';
};

if (document.URL == 'https://creewick.github.io/study/')
    document.getElementsByClassName('site-title')[0].className += ' selected';
