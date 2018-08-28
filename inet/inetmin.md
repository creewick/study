<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\(','\)']]}});</script><script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>

[home](../) > [inet](./) > inetmin

# inetmin

#### [Протокол OSPF](routing.html#header-n124)

* [Виды зон OSPF (+чем отличаются)](../routing/ospf.html#header-n114)

			 *Backbone, Norma, Stub, Totally Stub, NSSA, Totally NSSA*

* [Виды маршрутизаторов](../routing/ospf.html#header-n148)

			 *Internal, Area border, Backbone, ASBR*

* [Объявления о состоянии канала LSA (+для чего нужны)](../routing/ospf.html#header-n162)

			 *Router LSA, Network LSA, Summary LSA, AS Summary LSA*

#### [Протокол BGP](bgp#header-n3)

* [Определение автономной системы в Интернете (+как менялось со временем)](../as#header-n3)
* [Инструменты управления BGP трафиком](../bgp/traffic)

			 *AS_Path prepend, MED, Weight, Community, Local Preference, BGP multipath, анонс разных префиксов через разных ISP, AS-Path ACL*

#### [Типы записей DNS (+формат значений)](../dns/conf)

​	 *SOA, NS, A, CNAME, MX, PTR, DS, DNSKEY, RRSIG, SPF*

#### Команды протокола SMTP (+синтаксис и что делают)

​	 *HELP, HELO, EHLO, MAIL, RCPT, DATA, RSET, QUIT*

#### Команды протокола POP3 (+синтаксис и что делают)

​	 *USER, PASS, STAT, LIST, UIDL, TOP, RETR, DELE, RSET, QUIT*

#### Команды протокола FTP (+синтаксис и что делают)

​	 *HELP, USER, PASS, SYST, STAT, TYPE, SWD, LIST, PASV, PORT, RETR, STOR, DELE, QUIT*

#### Заголовки писем (+формат значений)

​	 *Return-Path, Received, From, Reply-To, To, CC, BCC, Message-Id, Subject, MIME-Version, Content-Transfer-Encoding, Content-Type, Content-Type: multipart/\*, DKIM*

#### Методы HTTP (+назначение и формат пакетов)

​	 *GET, HEAD, POST, OPTIONS, TRACE*

#### HTTP заголовки общие (+формат значений)

​	 *Cache-Control, Connection, Date, Trailer, Transfer-Encoding, Upgrade, Via*

#### HTTP заголовки клиента (+формат значений)

​	 *Accept, Accept-Charset, Accept-Encoding, Accept-Language, Authorization, Expect, Host, Cookie, If-Match, If-Non-Match, If-Modified-Since, If-Unmodified-Since, If-Range, Max-Range, Proxy-Authorization, Range, Referer, User-Agent*

#### HTTP заголовки сервера (+формат значений)

​	 *Accept-Ranges, Age, Location, Proxy-Authenticate, Public, Refresh, Server, Set-Cookie, Vary, Warning, WWW-Authenticate*

#### HTTP заголовки сущности (+формат значений)

​	 *Allow, Content-Encoding, Content-Language, Content-Length, Content-Location, Content-MD5, Content-Range, Content-Type, ETag, Expires, Last-Modified*

#### Коды ответов HTTP-сервера (+формат пакетов)

​	 *100 Continue*

​	 *101 Switching Protocols*

​	 *200 OK*

​	 *204 No Content*

​	 *206 Partial Content*

​	 *301 Moved Permanently*

​	 *302 Found*

​	 *304 Not Modified*

​	 *400 Bad Request*

​	 *403 Forbidden*

​	 *404 Not Found*

​	 *413 Request Entity Too Large*

​	 *417 Expectation Failed*

​	 *500 Internal Server Error*

​	 *503 Service Unavailable*