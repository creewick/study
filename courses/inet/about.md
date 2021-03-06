---
title: Описание курса
---

Курс длится 1 семестр, в конце семестра экзамен. В неделю 1 лекция, 1 практика.  

### Цель преподавания дисциплины

 Изучение базовых принципов работы сети Интернет, приобретение навыков  практического программирования для сети Интернет. В рамках курса студенты имеют возможность взять курсовые работы, которые  могут стать основой для бакалаврских и магистерских работ.  

### Задачи изучения дисциплины

 Изучение служб и протоколов Интернета. Получение навыков релизации на выбранном языке программирования протоколов взаимодействия клиентов и серверов.  

### Место дисциплины в системе высшего профессионального образования

 В рамках курса используются знания, полученные студентами на курсах "Скрипты", "Языки сценариев (Python)", "Сети".  

### Требования к уровню освоения содержания курса

**Студент должен иметь представление** о принципах ораганизации и управления Инетрнетом; о принципах функционирования служб Интернета.

**Студент должен знать** архитектуру стека протоколов TCP/IP; механизм функционирования слуб DNS, E-mail, FTP, Web и соответствующие протоколы.

**Студент должен уметь** пользоваться утилитами для настройки/диагностики протоколов TCP/IP; реализоваывать на выбранном (студентом) языке программирования протоколы Интернета.

### Содержание курса

 Темы и разделы, их краткое содержание: 

1. Хост, IP-адрес, IP-сеть. Маршрутизация и протоколы маршрутизации  (RIP, OSPF). Технология CIDR, маски переменной длины и их использование  при маршрутизации и для агрегирования адресов сетей.
2. Автономная система. Протокол междоменной маршрутизации BGP-4 и его расширения.
3. Служба сетевого времени (NTP/SNTP).
4. Службы Интернета. Служба доменных имён (DNS), форвардинг,  кэширующие сервера, распределённая система хранения зон, ресурсные  записи, корневые сервера. Утилита nslookup и dig.
5. Служба электронной почты. Протоколы smtp, pop3, imap команды.
6. Служба FTP. Протокол ftp, команды.
7. Протокол HTTP.
8. Служба WWW. Понятие "гипертекст".
9. Криптографические протоколы, обеспечивающие защищенную передачу данных между узлами в сети Интернет.

### Темы лабораторных работ

1. Использование эмулятора Cisco Packet Tracer. Базовая настройка  хостов, коммутаторов и маршрутизаторов; VLAN и NAT. Настройка RIP.
2. Динамическая маршрутизация. Настройка протокола OSPF.
3. Работа с whois серверами региональных интернет регистраторов. Получение статистических данных от RIPE, https://stat.ripe.net/
4. Принцип работы утилит nslookup и dig.
5. Настройка DNS сервера.
6. Настройки учётной записи почтового клиента и связь их с командами POP3.
7. Способы получения почты. Последовательность команд для получения письма через telnet по протоколу POP3.
8. Способы отправки почты. Последовательность команд для оправки письма через telnet по протоколу SMTP.
9. Формат письма (.eml). Минимальный набор заголовков. Формат составного письма с вложением.
10. Последовательность команд ftp для передачи файла в двоичном формате  с одного ftp-сервера на другой напрямую (без скачивания себе). Утилита  ftp: интерактивный и пакетный режимы.
11. Структура HTTP-пакета. Процесс работы с HTTP-сервером через telnet:  Передача запроса на сервер (GET, POST) и ответа с сервера. Утилиты  webproxy, httplook и другие сниферы.
12. Настройки веб-сервера и их связь с HTTP. Ограничения по командам HTTP. Дополнительные заголовки. Типы файлов.

### Обязательные задачи, инетмин и вопросык экзамену

 До экзамена или на экзамене надо сдать [inetmin.txt](inetmin)

 К концу семестра необходимо сдать [три обязательные задачи](tasks). Можно сдать  больше задач и тем самым поднять балл текущей успеваемости.

### Коллоквиум

 В апреле проводится коллоквиум, дата будет согласована с группами.  Баллы, полученные на коллоквиуме, будут учтены на экзамене. Те вопросы,  на которые даны неверные ответы, пойдут плюсом к доп. вопросам, которые  будут заданы на экзамене.  Коллоквиум проводится в письменной форме, в виде теста. Вопросы с  вариантами ответов и без таковых (надо указать свой ответ, иногда  развернутый). 

##### Темы, выносимые на коллоквиум:

1. Маршрутизация
2. Автономные системы Интернета, протокол BGP-4.
3. Служба DNS.

