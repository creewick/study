Routing Information Protocol - протокол динамической маршрутизации, относящийся к дистанционно-векторным протоколам. 

[TOC]

## История

Алгоритм маршрутизации RIP (алгоритм Форда — Беллмана) был впервые разработан в 1969 году, как основной для сети ARPANET.

Версия RIP, которая поддерживает протокол интернета была включена в пакет BSD операционной системы Unix под названием routed (route daemon), а также многими производителями, реализовавшими свою версию этого протокола. В итоге протокол был унифицирован в документе RFC 1058.

В период с 1993 по 1998 годы разрабатывался протокол RIP-2 (RFC 2453), который является расширением протокола RIP, обеспечивающим передачу дополнительной маршрутной информации в сообщениях RIP и повышающим уровень безопасности.

Для работы в среде IPv6 была разработана версия RIPng.

## Алгоритм Форда - Беллмана

### Постановка задачи

Найти кратчайшие пути от вершины $s$ до всех остальных вершин графа.

Гарантируется, что в графе нет контуров отрицательной длины.

### Описание алгоритма

* Основная идея алгоритма - поэтапное вычисление кратчайших расстояний

* Пусть $d_k(v)$ - длина кратчайшего среди всех $(s, v)$ - путей, содержащих не более $k$ дуг.

* Легко понять, что $d_1(v) \geq d_2(v) \geq ... \geq d_{n-1}(v)$

* Поскольку в графе нет контуров отрицательной длины, кратчайший $(s, v)$-путь не может содержать более, чем n-1 дугу.

  Поэтому $d_{n-1}(v)$ дает искомое расстояние

* Значения $d_1(v)$ вычисляются просто:

  $d_1(v) = c(s, v),  \forall v \in V$

* $d_{k+1}(v) = min(d_k(v), d_k(w) + c(w,v) |w \in V)$

## Заголовок пакета

`Команда` `Версия ` `0000000000000000`

**Команды:**

1. request
2. response

## RIP v1

Очень простой. Применяется в небольших сетях. В качестве метрики использует число переходов.

Максимальное число хопов: 15

Работает на сетевом уровне, 520/UDP

### Формат записи

`-Тип-Адреса-(2)-` `0000000000000000`

`--------IP-Адрес-(4-байта)--------`

`0000000000000000000000000000000000`

`0000000000000000000000000000000000`

`---------Метрика-(4-байта)--------`

**Тип адреса** - обычно IP = 2

### Принцип работы

1. **Создание минимальной таблицы**

   На каждом маршрутизаторе создается минимальная таблица маршрутизации, в которой учитываются непосредственно подсоединенные сети

   | Номер сети  | Адрес след. маршрутизатора | Порт | Расстояние |
   | ----------- | -------------------------- | ---- | ---------- |
   | 201.36.14.0 | 201.36.14.3                | 1    | 1          |
   | 132.11.0.0  | 132.11.0.7                 | 2    | 1          |
   | 194.27.18.0 | 194.27.18.1                | 3    | 1          |

2. **Рассылка минимальной таблицы соседям**

3. **Получение сообщений от соседей и обработка полученной информации**

   Маршрутизатор, после получения сообщений от соседей, увеличивает каждое поле метрики на 1, и запоминает через какой порт и от какого маршрутизатора получена информация, складывая ее себе в таблицу

4. **Рассылка новой таблицы соседям**

   Обновив таблицу маршрутизатор снова отправляет ее всем своим соседям. 

   ...

### Преимущества

* Простота изучения и конфигурирования
* Обычно не становится причиной возникновения петлей
* Почти полностью гарантируется поддержка маршрутизаторами любых типов
* Обеспечивает распределение нагрузки

### Проблемы

* Ограничение на 15 хопов не дает применять этот протокол в больших сетях

* Не позволяет учитывать в метрике пропускную способность, задержку или надежность

* Метрика по количеству переходов неэффективна 

  RIP не учитывает реальную производительность каналов связи, что может оказаться неэффективным в сятех, объединяющих каналы связи различного устройства, производительности, в которых используются разные сетевые технологии

* Проблема медленной конвергенции

  Маршрутизаторы, использующие протокол RIP, рассылают маршрутную информацию каждые 30 секунд, причем их работа не синхронизирована. В ситуации, когда некоторый маршрутизатор обнаружит, что какая-либо сеть стала недоступной, то в худшем случае, он сообщит об этом соседям через 30 секунд. Информация о недоступности может распространяться маршрутизаторам достаточно долго, при этом сеть будет находиться в нестабильном состоянии.

* Широковещательная рассылка таблиц маршрутизации

  Отправленный пакет RIP вынуждены получить и проанализировать  все компьютеры сети, в которую он направлен, вызывая затраты процессорного времени хостов

* Не поддерживает бесклассовую адресацию

* Не поддерживает аутентификацию обновлений

  Существует возможность намеренно нарушить процесс маршрутизации путем несанкционированного применения маршрутизатора

## RIP v2

Протокол RIP версии 2 (RFC 2453) позволяет устранить некоторые ограничения версии 1, но без внесения в сам протокол каких-либо кардинальных изменений.

### Изменения

* **Поддержка бесклассовой адресации** 

  Вместе с обновлениями RIPv2 передаются маски подсети 

* **Многоадресные обновления**

  Обновления передаются с помощью многоадресной, а не широковещательной рассылки

* **Поддержка аутентификации**

  В маршрутизаторах, совместимых с требованиями RFC 2453, поддерживаются аутентификация на основе открытого текста (В маршрутизаторах Cisco также - с шифрованием MD5)