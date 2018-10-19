---
title: Протоколы Интернет
toc: true
---

Солодушкин Святослав Игоревич

---

[Описание курса](about)

[inetmin](inetmin)

[Билеты](exam)

[Задачи](tasks)



## Материалы по курсу

### Лекция № 1. Маршрутизация, протокол RIP

* [Презентация](lectures/1.pdf)
* [Вопросы к пятиминутке](lectures/1q)

#### Практика № 1. Маршрутизация (статическая и RIP)

* [Базовая настройка, VLAN и NAT. Настройка RIP](practice/1.pdf)
* [Протоколы маршрутизации, список команд с объяснениями, CISCO](practice/1commands.pdf)
* [Конфигурирование маршрутизаторов, гл. 4, раздел "Конфигурирование IP-маршрутизации", CISCO](practice/1config.pdf)

### Лекция № 2. Маршрутизация, протокол OSPF

* [Презентация](lectures/2.pdf)
* [Вопросы к пятиминутке](lectures/2q)
* [Протокол OSPF, RFC-2328](lectures/rfc2328.pdf)
* [Руководство по проектированию OSPF, CISCO](lectures/2ospfManual.pdf)
* [Типы областей OSPF и соответстующие LSA](http://habrahabr.ru/post/162163/)

#### Практика № 2. Маршрутизация, OSPF

* [Настройка протокола OSPF на устройствах CISCO](practice/2.pdf)
* [Сборка сети, одна область](practice/2sborka1.pkt)
* [Сборка сети, несколько областей, часть 1](practice/2sborka2.pkt)

### Лекция № 3. Автономные системы Интернета, протокол BGP-4

* [Презентация](lectures/3.pdf)
* [Вопросы к пятиминутке](lectures/3q)

* [Опорный конспект](lectures/3notes.pdf)
* [Руководство по созданию, выбору и регистрации автономных систем, RFC-1930](lectures/3rfc1930.pdf)
* [Протокол BGP-4, RFC-4271](lectures/3rfc4271.pdf)

#### Практика № 3. Маршрутизация, протокол BGP-4

* [Настройка протокола BGP на устройствах CISCO](practice/3.pdf)
* [Сборка сети](practice/3sborka.pkt)

### Лекция № 4. Служба DNS, принципы работы

* [Презентация](lectures/4.pdf)
* [Книга про DNS и BIND](lectures/4dnsbook.pdf)
* [DOMAIN NAMES - CONCEPTS AND FACILITIES, RFC-1034](lectures/4rfc1034.pdf)
* [Доменные имена - реализация и спецификация, RFC-1035](lectures/4rfc1035.pdf)

#### Практика № 4. Работа с BGP

Работа с BGP: базы RIS'ов, утилита BGPlay, Looking glass, сервис whois и т. д.

* [Работа с BGP, написание своей whois утилиты](practice/4.pdf)
* [Search RIPEstat](https://stat.ripe.net/)
* [Джентельменский набор для работы с BGP](http://nt.ua/aboutcenter/articles/Pages/samoilenko_bgp_2013.aspx)

### Лекция № 5. Служба DNS, описание зоны, настройка BIND

* [Презентация](lectures/5.pdf)

#### Практика № 5. Работа с утилитами nslookup и dig

* [План практики](practice/5.pdf)
* [Самостоятельная работа по nslookup](practice/5nslookup.pdf)

### Лекция № 6. Служба DNS, основы асимметричной криптографии и расширения DNSSEC

* [Презентация](lectures/6.pdf)
* [Вопросы к пятиминутке](lectures/6q)

#### Практика № 6. Настройка BIND, создание своего "Интернета"

* [План практики](practice/6.pdf)
* [BIND 9 Manual](practice/6bind.pdf)
* [Архив с настройками](practice/6.zip)

### Лекция № 7. Служба e-mail, протокол SMTP, борьба со спамом

* [Презентация](lectures/7.pdf)
* [Простой протокол передачи электронной почти (SMTP), RFC-5321](lectures/7rfc5321.pdf)
* [Формат сообщений Internet, RFC-5322](lectures/7rfc5322.pdf)
* [Почтовый сервер для начинающих](http://interface31.ru/tech_it/2010/10/pochtovyj-server-dlya-nachinayushhix-nastraivaem-dns-zonu.html), три статьи про найстроку почтового сервера без привязки к конкретной программе

### Лекция № 8. Служба e-mail, протокол POP и IMAP

* [Презентация](lectures/8.pdf)
* [Протокол POP3, лекция на INUIT](http://www.intuit.ru/studies/courses/116/116/lecture/3365)
* [Протокол IMAP, лекция на INUIT](http://www.intuit.ru/studies/courses/116/116/lecture/3367)

### Лекция № 9. Служба передачи файлов, протокол FTP и BitTorrent 

* [Презентация FTP](lectures/9ftp.pdf)
* [Презентация BitTorrent](lectures/9bit.pdf)
* [Опорный конспект по BitTorrent](lectures/9bit2.pdf)

### Лекция № 10. Протокол TCP: повышение производительности 

* [Презентация](lectures/10.pdf)
* [Transmission Control Protocol, RFC-793](lectures/10rfc793.pdf)

### Лекция № 11. Протокол HTTP 

* [Конспект лекции](lectures/11.pdf)
* [Перевод документации, RFC-2616](lectures/11rfc2616.html)



## Конспекты

[Маршрутизация](notes/routing)

* [Протокол RIP](notes/routing/rip)
* [Протокол OSPF](notes/routing/ospf)
* [Автономные системы](notes/as)
* [Протокол BGP](notes/routing/bgp)
  * [Управление трафиком BGP](notes/routing/bgp/traffic)

[Служба DNS](notes/dns)

* [Конфигурация DNS сервера, ресурсные записи](notes/dns/config)
* [Формат DNS пакета](notes/dns/format)
* [Расширение DNSSEC](notes/dns/dnssec)
* [Криптосистемы с открытым ключом](notes/dns/crypto)

[Электронная почта](notes/email)

* [Протокол SMTP](notes/email/smtp)

------

[Quizlet по inetmin](https://quizlet.com/join/yVSXV8DXb)

