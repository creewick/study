---
title: Формат DNS пакета
---

Для DNS запроса и DNS отклика используется одинаковый формат:

`------------Идентификация-(32-бита)------------`

`QR` `Opcode(4)` `AA` `TC` `RD` `RA` `нули(3)` `rcode(4)`

`---------Количество-вопросов-(32-бита)---------`

`----------Количество-ответов-(32-бита)---------`

`-------Количество-прав-доступа-(32-бита)-------`

`--------Количество-доп-записей-(32-бита)-------`

------

`-------------------Вопросы-(?)-----------------`

`-------------------Ответы-(?)------------------`

`----------------Права-доступа-(?)--------------`

`------------------Доп-записи-(?)---------------`

**Идентификация** устанавливается клиентом и возвращается сервером. Позволяет клиенту понять, на какой из его запросов пришел отклик.

**QR** - тип сообщения (1 бит):

0. Запрос
1. Отклик

 **OpCode** - код операции (4 бита):

0. Стандартный запрос
1. Инверсный запрос
2. Запрос статуса сервера

**AA** - авторитетный ответ (1 бит)

**TC** - сообщение обрезано (1 бит). Полный размер отклика превысил 512 байт, были возвращены только первые 512 байт отклика

**RD** - требуется рекурсия. Требует от DNS сервера обработать этот запрос самомму (сервер сам должен определить требуемый IP адрес, а не возвращать адрес другого DNS сервера)

**RA** - рекурсия возможна. Устанавлиавется сервером, если он поддерживает рекурсию (например, корневые сервера не в состоянии обрабатывать рекурсивные запросы в силу своей загруженности)

**RCode** - код возврата (4 бита):

* 0. Нет ошибок
* 3. Ошибка имени

## Формат вопроса

`-------------Имя-запроса-(?)-----------`

`-Тип-запроса-(16)-` `-Класс-запроса(16)-`

### Формат записи имени

Имя выглядит как последовательность меток. Каждая метка начинается с однобайтового счетчика, который содержит количество следующих за ним байт. Имя заканчивается байтом равным 0. Каждый счетчик должен быть в диапазоне от 0 до 63.

Пример: `6` `gemini` `3` `tuc` `4` `noao` `3` `edu` `0`

### Сокращения в записи имени

Если старшие два бита счетчика равны 1, то это не однобитовое число - длина метки, а 16-битный указатель, 14 бит которого являются смещением от начала DNS-сообщения, указывающим на следующую метку.

**Пример**:

*начиная с байта #20*: `1` `f` `3` `i` `s` `i` `4` `a` `r` `p` `a` `0`

*байт #40:* `3` `f` `o` `o` `0x1101_0100`

*байт #64:* `0x1101_1010`

*байт #92*: `0`

**Здесь записаны:** `f.isi.arpa.` , `foo.f.isi.arpa.` , `arpa.` , `.`

  

**Типы запроса**:

| Имя     | Значение | Описание                |
| ------- | -------- | ----------------------- |
| A       | 1        | IPv4                    |
| AAAA    | 28       | IPv6                    |
| AXFR    | 252      | запрос на передачу зоны |
| CNAME   | 5        | каноничное имя          |
| HINFO   | 13       | информация о хосте      |
| MX      | 15       | запись об обмене почтой |
| NS      | 2        | сервер DNS              |
| PTR     | 12       | запись указателя        |
| * (ANY) | 255      | запрос всех записей     |

**Класс запроса** обычно равен 1 (Internet)

## Формат ресурса

Последние три поля в пакете DNS: ответы, полномочия и доп. информация; объединены общим форматом и называются записью ресурса.

`--------------Имя-домена-(?)------------`

`------Тип-(16)-----` `-----Класс-(16)----`

`--------------TTL-(32-бита)-------------`

`-Длина-данных-(16)-` `----Данные-(?)-----` 