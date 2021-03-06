---
title: Автономные системы
toc: true
---

## Мотивировка

Интернет состоит не из хостов или сетей, а из автономных систем.

Протокол BGP выполняет междоменную маршрутизацию.

В ПО маршрутизаторов предусмотрена передача информация от RIP процессу OSPF:

 `R1` —RIP→ `R2` —OSPF→ `R3`

Можно ли использовать RIP или OSPF для маршрутизации в масштабах Интернета?

1. OSPF - это протокол состояния связей. Маршрутизатор знает топологию всей сети. Из соображений безопасности, не стоит показывать детали своей сети.
2. В Интернете более 500 тыс. маршрутов. Внутренние протоколы не предназначены для обработки такого объема информации.

## Автономная система

__Автономная система__ - группа из одного или нескольких префиксов IP, работающих у одного или нескольких сетевых операторов, которые имеют __единую__ и __четко определенную__ политику маршрутизации.

![2](img\Автономная система.png)

## Классификация AS

*согласно RFC 1772*

* __Тупиковая (stub)__ - имеет соединение только с одной АS.
* __Многодомная (multihomed)__ - соединена с несколькими AS, но не принимает транзитный трафик.
* __Транзитная__ - соединена с множеством AS и предназначена (с некоторыми ограничениями) для поддержки локального и транзитного трафиков.
