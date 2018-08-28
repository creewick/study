<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\(','\)']]}});</script><script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>

[home](../../../) > [inet](../../) > [email](../) > pop3

# POP3

**POP3** *Post Office Protocol Version 3* - стандартный интернет-протокол прикладного уровня, используемый клиентами электронной почты для получения почты с удаленного сервера по TCP-соединению.

[TOC]

POP поддерживает простые требования «загрузи-и-удали» для доступа к удалённым почтовым ящикам. Использующие POP клиенты обычно соединяются, извлекают все письма, сохраняют их локально как новые сообщения, удаляют их с сервера, после чего разъединяются.

POP3-сервер прослушивает порт 110. Шифрование связи для POP3 запрашивается после запуска протокола, с помощью либо команды STLS (если она поддерживается), либо POP3S, которая соединяется с сервером используя протокол TLS или SSL по TCP-порту 995.

Доступные сообщения клиента фиксируются при открытии почтового ящика POP-сессией и определяются количеством сообщений для сессии, или, по желанию, с помощью уникального идентификатора, присваиваемого сообщению POP-сервером. Этот уникальный идентификатор является постоянным и уникальным для почтового ящика и позволяет клиенту получить доступ к одному и тому же сообщению в разных POP-сессиях. Почта извлекается и помечается для удаления с помощью номера сообщения. При выходе клиента из сессии помеченные сообщения удаляются из почтового ящика.

## История

POP (POP1) определён в [RFC 918](https://tools.ietf.org/html/rfc918) (1984), POP2 в [RFC 937](https://tools.ietf.org/html/rfc937) (1985). Первоначальная спецификация POP3 была представлена в [RFC 1081](https://tools.ietf.org/html/rfc1081) (1988). Нынешняя же описана в [RFC 1939](https://tools.ietf.org/html/rfc1939), обновлена механизмом расширения ([RFC 2449](https://tools.ietf.org/html/rfc2449)) и механизмом аутентификации ([RFC 1734](https://tools.ietf.org/html/rfc1734)).

Версии POP2 был назначен порт 109.

Изначальная спецификация POP3 поддерживала только незашифрованный механизм входа в систему USER/[PASS](https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D0%BE%D0%BB%D1%8C) или управление доступом [.rhosts](https://ru.wikipedia.org/wiki/Rlogin). На данный момент, POP3 поддерживает различные методы [аутентификации](https://ru.wikipedia.org/wiki/%D0%90%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F) для предоставления разных уровней защиты от незаконного доступа к пользовательской почте. Большинство из них предоставлены механизмами расширения POP3. Клиенты POP3 поддерживают методы [SASL](https://ru.wikipedia.org/wiki/Simple_Authentication_and_Security_Layer) через расширение AUTH. В рамках проекта [Массачусетского технологического института](https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%81%D1%81%D0%B0%D1%87%D1%83%D1%81%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%B8%D0%BD%D1%81%D1%82%D0%B8%D1%82%D1%83%D1%82) «Афина» также был введён метод на основе [Кербероса](https://ru.wikipedia.org/wiki/Kerberos). [RFC 1460](https://tools.ietf.org/html/rfc1460) ввёл APOP в основной протокол. APOP — протокол вида [«запрос/ответ»](https://ru.wikipedia.org/wiki/%D0%92%D1%8B%D0%B7%D0%BE%D0%B2-%D0%BE%D1%82%D0%B2%D0%B5%D1%82_(%D0%B0%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F)), использующий [функцию хэширования](https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%85%D0%B5%D1%88-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F) [MD5](https://ru.wikipedia.org/wiki/MD5). Среди клиентов, реализующих APOP, можно выделить [Mozilla Thunderbird](https://ru.wikipedia.org/wiki/Mozilla_Thunderbird), [Opera Mail](https://ru.wikipedia.org/wiki/Opera_Mail), [Eudora](https://ru.wikipedia.org/wiki/Eudora_Mail), Windows Live Mail, PowerMail, [Apple Mail](https://ru.wikipedia.org/wiki/Apple_Mail), и т. д.

Было высказано неофициальное предложение для спецификации «POP4», с рабочей реализацией сервера. Это предложение добавило основные функции управления папками, поддержку составных сообщений, а также управление флагами сообщений. Однако, никакого прогресса «POP4» не наблюдается с 2003 г.

## Расширения

Механизм расширений был предложен в [RFC 2449](https://tools.ietf.org/html/rfc2449) для размещения новых расширений, а также организованного объявления о поддержке опциональных команд, таких как TOP и UIDL. RFC не намеревались поощрять расширения и подтвердили, что роль POP3 заключается в предоставлении простой поддержки в основном для требования «загрузи-и-удали».

Расширения выводятся списком командой CAPA. За исключением APOP, все опциональные команды были включены в изначальный набор возможностей. Как и в стандарте ESMTP ([RFC 5321](https://tools.ietf.org/html/rfc5321)), возможности, начинающиеся с "X", являются локальными.

### STARTTLS

Расширение [STARTTLS](https://ru.wikipedia.org/wiki/STARTTLS) позволяет использовать [TLS](https://ru.wikipedia.org/wiki/TLS) (Transport Layer Security) или [SSL](https://ru.wikipedia.org/wiki/SSL) (Secure Sockets Layer) для связи с помощью команды STLS, по стандартному POP3-порту. Некоторые клиенты и сервера используют метод альтернативного порта, работающий с TCP-портом 995 (POP3S).

### SDPS

Британский провайдер Demon Internet ввёл расширение POP3, позволяющее иметь несколько учётных записей для каждого домена и ставшее известным как SDPS (Standard Dial-up POP3 Service). Для доступа к каждой учётной записи имя пользователя включает в себя имя хоста, например, john@hostname или john+hostname.

Google Apps используют тот же метод[[1\]](https://ru.wikipedia.org/wiki/POP3#cite_note-1).

## Состояние сеанса

В протоколе POP3 предусмотрено 3 состояния сеанса:

- [Авторизация](https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)

  Клиент проходит процедуру [Аутентификации](https://ru.wikipedia.org/wiki/%D0%90%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F).

- [Транзакция](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D0%B7%D0%B0%D0%BA%D1%86%D0%B8%D1%8F_(%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0))

  Клиент получает информацию о состоянии почтового ящика, принимает и удаляет почту.

- Обновление

  Сервер удаляет выбранные письма и закрывает соединение.

## Команды протокола

| Имя  | Аргументы                     | Ограничения                                            | Возможные ответы                                             |
| ---- | ----------------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| APOP | [имя] [digest]                | Её поддержка не является обязательной                  | * +OK maildrop has n message* -ERR password supplied for [имя] is incorrect |
| USER | [имя]                         | —                                                      | * +OK name is a valid mailbox* -ERR never heard of mailbox name |
| PASS | [пароль]                      | Работает после успешной передачи имени почтового ящика | * +OK maildrop locked and ready* -ERR invalid password* -ERR unable to lock maildrop |
| DELE | [сообщение]                   | Доступна после успешной аутентификации                 | * +OK message deleted* -ERR no such message                  |
| LIST | [сообщение]                   | Доступна после успешной аутентификации                 | * +OK scan listing follows* -ERR no such message             |
| NOOP | —                             | Доступна после успешной аутентификации                 | +OK                                                          |
| RETR | [сообщение]                   | Доступна после успешной аутентификации                 | * +OK message follows* -ERR no such message                  |
| RSET | —                             | Доступна после успешной аутентификации                 | +OK                                                          |
| STAT | —                             | Доступна после успешной аутентификации                 | +OK a b                                                      |
| TOP  | [сообщение][количество строк] | Доступна после успешной аутентификации                 | * +OK n octets* -ERR no such message                         |
| QUIT | —                             | —                                                      | +OK                                                          |

### APOP[[править](https://ru.wikipedia.org/w/index.php?title=POP3&veaction=edit&section=9) | [править код](https://ru.wikipedia.org/w/index.php?title=POP3&action=edit&section=9)]

Команда служит для передачи серверу имени пользователя и зашифрованного пароля (digest).
**[имя]** — строка, указывающая имя почтового ящика.
**[digest]** — [хеш-сумма](https://ru.wikipedia.org/wiki/%D0%A5%D0%B5%D1%88-%D1%81%D1%83%D0%BC%D0%BC%D0%B0) временной метки, конкатенированной с паролем пользователя, вычисленная по алгоритму [MD5](https://ru.wikipedia.org/wiki/MD5). В случае поддержки этой команды временная метка получается при соединении с сервером.

### USER[[править](https://ru.wikipedia.org/w/index.php?title=POP3&veaction=edit&section=10) | [править код](https://ru.wikipedia.org/w/index.php?title=POP3&action=edit&section=10)]

Передаёт серверу имя пользователя.
**[имя]** — строка, указывающая имя почтового ящика.

### PASS[[править](https://ru.wikipedia.org/w/index.php?title=POP3&veaction=edit&section=11) | [править код](https://ru.wikipedia.org/w/index.php?title=POP3&action=edit&section=11)]

Передаёт серверу пароль почтового ящика.
**[пароль]** — пароль для почтового ящика.

### DELE[[править](https://ru.wikipedia.org/w/index.php?title=POP3&veaction=edit&section=12) | [править код](https://ru.wikipedia.org/w/index.php?title=POP3&action=edit&section=12)]

Сервер помечает указанное сообщение для удаления. Сообщения, помеченные на удаление, реально удаляются только после закрытия транзакции (закрытие транзакций происходит обычно после посыла команды QUIT, кроме этого, например, на серверах закрытие транзакций может происходить по истечении определённого времени, установленного сервером).
**[сообщение]** — номер сообщения.

### LIST[[править](https://ru.wikipedia.org/w/index.php?title=POP3&veaction=edit&section=13) | [править код](https://ru.wikipedia.org/w/index.php?title=POP3&action=edit&section=13)]

Если был передан аргумент, то сервер выдаёт информацию об указанном сообщении. Если аргумент не был передан, то сервер выдаёт информацию обо всех сообщениях, находящихся в почтовом ящике. Сообщения, помеченные для удаления, не перечисляются.
**[сообщение]** — номер сообщения (необязательный аргумент).

### NOOP[[править](https://ru.wikipedia.org/w/index.php?title=POP3&veaction=edit&section=14) | [править код](https://ru.wikipedia.org/w/index.php?title=POP3&action=edit&section=14)]

Сервер ничего не делает, всегда отвечает положительно.

### RETR сообщение[[править](https://ru.wikipedia.org/w/index.php?title=POP3&veaction=edit&section=15) | [править код](https://ru.wikipedia.org/w/index.php?title=POP3&action=edit&section=15)]

Сервер передаёт сообщение с указанным номером.
**[сообщение]** — номер сообщения.

### RSET[[править](https://ru.wikipedia.org/w/index.php?title=POP3&veaction=edit&section=16) | [править код](https://ru.wikipedia.org/w/index.php?title=POP3&action=edit&section=16)]

Этой командой производится откат транзакций внутри сессии. Например, если пользователь случайно пометил на удаление какие-либо сообщения, он может убрать эти пометки, отправив эту команду.

### STAT[[править](https://ru.wikipedia.org/w/index.php?title=POP3&veaction=edit&section=17) | [править код](https://ru.wikipedia.org/w/index.php?title=POP3&action=edit&section=17)]

Сервер возвращает количество сообщений в почтовом ящике и размер почтового ящика в октетах. Сообщения, помеченные как удалённые, при этом не учитываются.

### TOP[[править](https://ru.wikipedia.org/w/index.php?title=POP3&veaction=edit&section=18) | [править код](https://ru.wikipedia.org/w/index.php?title=POP3&action=edit&section=18)]

Сервер возвращает заголовки указанного сообщения, пустую строку и указанное количество первых строк тела сообщения.
**[сообщение]** — номер сообщения.
**[количество строк]** — сколько строк нужно вывести.

