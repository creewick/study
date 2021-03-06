---
title: Вопросы к экзамену
---

1. [Маршрутизация. Определение, виды (внешняя и внутренняя, протоколы состояния связей и дистанционно векторные), примеры протоколов маршрутизации. ](../routing)

2. [Протокол RIP-v2. Общая характеристика, схема работы. Проблемы сходимости и способы улучшения сходимости.](../routing/rip) 

   [Протокол OSPF. Общая характеристика, схема работы. Понятия зон (Area), виды зон, для чего нужны. Виды маршрутизаторов в OSPF. Объявления о состоянии канала (LSA).](../routing/ospf)

3. [Автономные системы (АС) в Интернете, определения согласно RFC (и как менялось представление об АС в течение времени), виды.](../as) 

   [Протокол BGP-v4. Общая характеристика, схема работы. Распространение маршрутной информации между АС и внутри АС. ](../routing/bgp)

4. [Служба DNS. Исторический обзор и принципы DNS. Понятие домена и зоны, делегирование полномочий. Полностью определенные имена и суффиксы DNS. Процедура разрешение имен, рекурсивные и не рекурсивные запросы и процедуры разрешения, авторитетные и не авторитетные ответы. Типы серверов, мастер, слэйв, кэширующий, скрытый. Передача зоны, полное (AXFR) и инкрементальное копирование (IXFR). Динамический DNS (Dynamic Updates in the Domain Name System).](../dns)

5. [Ресурсные записи DNS. Описание зоны.](../dns/conf)

   [Формат пакета DNS.](../dns/format)

6. [Расширение DNSSEC. Ресурсные записи DS, DNSKEY, RRSIG: формат, назначение. Цепочка доверия.](../dns/dnssec) 

7. [Служба электронной почты. Исторический обзор и принципы функционирования.](email) [Формат письма и заголовки письма.](../email/smtp) Стандарт MIME. Передача писем с вложениями, заголовок Content-Type, тип multipart и его подтипы.

   Протоколы SMTP, POP3, IMAP, общая характеристика, схема работы. Принцип работы почтового сервера. Методы борьбы со спамом: черные и белые списки, использование ресурсных записей DNS (PTR, SPF и т. д.), DomainKeys Identified Mail. 

8. Протокол FTP: общая характеристика, схема работы. Пассивный и активный режимы, прямая передача между серверами. Протокол Bittorrent: общая характеристика, схема работы. 

9. Протокол TCP. Методы повышения производительности и решения проблем снижений пропускной способности: алгоритм медленного старта, борьба с «синдромом мелкого окна», управление тайм-аутами повторной передачи. 

10. Протокол HTTP: общая характеристика, версии, схема работы. URI. Типы сообщений и их формат. Методы протокола. Заголовки, их значения. Коды ответов. Соединения, буферизация и прокси-сервера. Идентификация доступа (базовая и дайджест). Согласование содержимого под управление клиента и сервера. Кэширование, механизмы управления кэшированием в HTTP. Валидаторы (сильные и слабые), условные запросы. Частичная загрузка и байтовые диапазоны. Загрузка динамически формируемого контента, чанки. 

11. Основные понятия ассиметричной криптографии. [Открытый и закрытый ключ, односторонние функции. Алгоритм Диффи-Хэллмана. Алгоритм RSA.](../dns/crypto) Атака «человек посредине».]9 Цифровые сертификаты: понятия, виды, назначение. 

12. Протоколы SSL: общая характеристика, схема работы. Общее представление о TLS, HTTPS. 