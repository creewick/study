<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$']]}});</script><script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>
[home](../../../) > [inet](../../) > [email](../) > smtp

# SMTP

[TOC]

## Формат письма

- **Заголовок SMTP**
  - Имя отправляющего узла (EHLO, IP)
  - MAIL FROM
  - RCPT TO
- **Письмо**
  - Заголовки письма (DATE, FROM, TO, MESSAGE-ID, SUBJECT)
  - *Пустая строка*
  - Тело письма

## Заголовки письма

- **Date -** Дата и время создания сообщения

- **From -** Адреса авторов сообщения, разделенные запятой. 

  Если адресов несколько, должно быть поле **Sender**.

- **Sender** - Адрес отправителя. 

  Если **From** содержит один адрес, то **Sender** может отсутствовать. Если значения **Sender** и **From** совпадают, то **Sender** должно отсутствовать.

- **Reply-to** - Адрес, на который автор сообщения желал бы получить ответ.

- **To** - Адреса адресатов, разделенные запятой.

- **Cc** - Копии. Адреса других адресатов, разделенные запятой.

- **Bcc** - Слепые копии. Адреса адресатов, которые будут не видны другими адресатами, получающим это сообщение. Разделяются запятыми.

- **Message-id** - Уникальный идентификатор сообщения. Идентификатор уникален для всего мира.

- **In-Reply-To** - Идентификатор сообщения, на которое делается ответ.

- **References** - Идентификатор сообщения, на которое делается ответ.

- **Subject** - Тема сообщения.

- **Comments** - Дополнительные комментарии к сообщению.

- **Keywords** - Ключевые слова, которые могут быть полезны адресату.

- **Resent-Date**, **Resent-From**, **Resent-Sender**, **Resent-To**, **Resent-Cc**, **Resent-Bcc**, **Resent-Message-Id** - Используются при пересылке сообщения. Эти поля содержат информацию, измененную тем, кто производил пересылку.

- **Return-Path** - Почтовый адрес, проставляемый SMTP-сервером на стадии финальной отсылки. Используется для доставки отчета об ошибке.

- **Received** - Используется для идентификации SMTP-серверов, которые принимали участие в отправке сообщения от отправителя к получателю. Каждый SMTP-сервер добавляет свое поле.

- **Encrypted** - Указывает на то, что сообщение было подвергнуто шифрованию.

- **MIME-Version** - Содержит версию MIME.

- **Content-Type** - Наиболее полная информация о содержимом сообщения, которая позволяет почтовому клиенту выбрать соответствующий механизм обработки.

- **Content-Transfer-Encoding** - Указывается способ помещения двоичных данных в тело сообщения.

- **Поля начинающиеся с X-** - Дополнительное незарегистрированное поле. Разные почтовые клиенты могут использовать разные незарегистрированные поля для собственных нужд.

## Команды

В конце каждой команды ставится перевод строки: `/r/n`

* **HELO `domain`** 

  Идентификация отправителя на принимающем сервере. В случае успешного выполнения этой команды получатель и отправитель готовы к дальнейшей работе.

* **MAIN FROM `email`** 

  Отправить почту по одному или более адресатам.

* **RCPT TO `email`**

  Определение одного получателя почты. Множество получателей определяются множеством этих команд.

* **DATA**

  Получатель получает данные о дате отправке почты. После этой команды клиент передает сообщение.

* **SEND FROM: `email`**

  Используется вместо MAIL FROM для передачи на терминал получателя.

* **SOML FROM: `email`**

  Используется для передачи на терминал получателя или в почтовый ящик, если пользователь не активен или запретил прием сообщений с терминала.

* **SAML FROM: `email`**

  Используется для передачи и на терминал, и в почтовый ящик.

* **RSET**

  Аннулирует все переданные до нее на сервер данные. Процесс передачи сообщения нужно начать заново.

* **VRFY `email`**

  Проверка наличия указаного адреса. Сервер посылает информацию о владельце ящика или говорит, что ящик не существует.

* **EXPN `email`**

  Получение адресов, внесенных в список рассылки

* **HELP `[command]`** 

  Описание команды \ список доступных команд

* **NOOP**

  Сервер отправляет ОК

* **QUIT**

  Сервер отправляет ОК и закрывает канал связи

* **TURN **

  1. Получатель отправляет ОК и берет на себя роль SMTP-передатчика
  2. Отвечает отказом и остается в роли SMTP-приёмника.

## MIME

__Multipurpose Internet Mail Extension__ – стандарт, описывающий передачу различных типов данных по электронной почте. 

Спецификация для кодирования информации и форматирования сообщений для передачи разного рода информации внутри текстовых данных. 

Определяет набор e-mail-заголовков для определения дополнительных атрибутов сообщения. 

Определяет множество кодировок, которые могут быть использованы для представления 8-битных бинарных данных с помощью символов из 7-битного ASCII.

### Примеры заголовков

> __Mime-Version – версия MIME.__
>
> ​	Mime-Version: 1.0
>
> ​	MIME-Version: 1.0 (Generated by GBD 3.7)
>
> __Content-Type – тип сообщения.__
>
> ​	Content-Type: text/plain; charset=KOI-8
>
> ​	application: octet-stream
>
> __Content-Transfer-Encoding – тип транспортного кодирования__
>
> ​	Content-Transfer-Encoding: base64 

## Extended SMTP

Механизм расширений протокола SMTP 

> S: 220 smtp.example.com ESMTP Postfix
>
> C: EHLO bob.example.org
>
> S: 250 smtp.example.com Hello bob.example.org [192.0.2.201]
>
> S: 250 8BITMIME
>
> S: 250 SIZE 14680064
>
> S: 250 AUTH LOGIN PLAIN CRAM-MD5 DIGEST-MD5
>
> S: 250 STARTTLS
>
> S: 250 PIPELINING S: 250 HELP
>
> S: 250 ETRN
>
> S: 250 CHECKPOINT

 ## AUTH – аутентификация и шифрование 

> S: 220 smtp.server.com Simple Mail Transfer Service Ready
>
> C: EHLO client.example.com
>
> S: 250-smtp.server.com Hello client.example.com
>
> S: 250 AUTH LOGIN PLAIN CRAM-MD5
>
> C: AUTH LOGIN
>
> S: 334 VXNlcm5hbWU6 Base64(Username:)
>
> C: dm92YQ== Base64(vova)
>
> S: 334 UGFzc3dvcmQ6 Base64(Password:)
>
> C: c2VjcmV0X3Bzd2Q= Base64(secret_pswd)
>
> S: 235 2.7.0 Authentication successful

## STARTTLS (Start Transport Layer Security) 

> C: EHLO client.example.com 
>
> S: 250-smtp.server.com Hello client.example.com 
>
> S: 250-AUTH LOGIN PLAIN CRAM-MD5 
>
> S: 250-STARTTLS 
>
> C: STARTTLS 
> 
> S: 220 TLS go ahead 
>
> C: <starts TLS negotiation>
>
> C:  C & S: <negotiate a TLS session and check result of negotiation>
>
> C: EHLO client.example.com *
>
> S: 250-smtp.server.com Hello client.example.com
>
> S: 250-AUTH LOGIN PLAIN CRAM-MD5
>
> C: AUTH LOGIN S: 334 VXNlcm5hbWU6
>
> C: dm92YQ== S: 334 UGFzc3dvcmQ6
>
> C: c2VjcmV0X3Bzd2Q=
>
> S: 235 2.7.0 Authentication successful 

## Заголовок multipart 

Содержимое письма состоит из некоторого множества частей, содержащих данные различных взаимонезависимых типов.

__mixed __ основной подтип;

__alternative__ представление одних и тех же данных в разных форматах;

__parallel__ одновременный просмотр разных частей документа; 

__digest__ объединение в одном письме частей, каждая из которых имеет тип message. 

### Пример multipart/alternative

Content-Type: multipart/alternative; boundary=boundary42

--boundary42 

Content-Type: text/plain; charset=us-ascii



... Здесь содержится версия простым текстом ....

--boundary42

Content-Type: text/richtext



.... Здесь содержится версия с разметкой RFC 1341...

--boundary42

Content-Type: text/x-whatever



.... Здесь содержится версия в гипотетическом формате..

 --boundary42-- 



## BASE64

Схема преобразования произвольной последовательности байт в последовательность печатных ASCII символов.

символы (A—Z, a—z),

цифры (0—9), символы «+» и «/»,

символ «=» в качестве специального кода суффикса.

> Hello, World -> SGVsbG8sIFdvcmxk 

## Настройка зоны DNS: PTR запись 

![1529606596216](img\Настройка зоны DNS - PTR запись.png)

> 44.33.22.11.in-addr.arpa. IN PTR mail.example.com. 

В случае Mail сервера для двух доменов PTR-запись должна указывать на имя почтового хоста (которое он передает в рамках SMTP-сессии), даже если он расположен в другом домене.

## Настройка зоны DNS: SPF



![1529606695111](img\Настройка зоны DNS - SPF.png)

![1529606720959](img\Настройка зоны DNS - SPF - 2.png)

## DomainKeys Identified Mail

DKIM-Signature: __v__=1; __a__=rsa-sha256; __d__=example.net;

__s__=brisbane; __c__=relaxed/simple; __q__=dns/txt; __l__=1234; 

__t__=1117574938; __x__=1118006938;

__h__=`from:to:subject:date:keywords:keywords;` __bh__=`MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI=;` __b__=`dzdVyOfAKCdLXdJOc9G2q8LoXSlEniSbav+yuU4zGeeruD00lszZVoG4 ZHRNiYzR `

![1529606759348](img\DomainKeys Identified Mail.png)

