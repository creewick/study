---
title: Теорема о полноте
layout: math
toc: true
---

## Вспомогательные определения 

Пусть __p__ - некоторая формула, содержащая в своей записи предметные символы $x_1, x_2, ..., x_n$. Пусть задана некоторая интерпретация предметных символов. Рассмотрим формулы $q_1, q_2, ..., q_n$, определенные следующим правилом:

**$$q_i=\begin{cases}x_i,&\text{если $x_i$ интерпретируется как 1;}\\(\neg x_i),&\text{если $x_i$ интерпретируется как 0;}\end{cases}$$** 

Определим формулу $$p_i=\begin{cases}p,&\text{если при данной интерпретации предметных символов $p$ принимает значение 1;}\\(\neg x_i),&\text{если при данной интерпретации предметных символов $p$ принимает значение 0;}\end{cases}$$

## Лемма 1

При любой  фиксированной интерпретации из $\{q_1, q_2, ..., q_n\}\vdash p'$

Для понимания рассмотрим пример:

| $x_1$ | $x_2 $ | $p: \neg x_1 \rightarrow x_2$ | $q_1$      | $q_2$      | $p'$                             |
| ----- | ------ | ----------------------------- | ---------- | ---------- | -------------------------------- |
| 0     | 0      | 0                             | $\neg x_1$ | $\neg x_2$ | $\neg(\neg x_1 \rightarrow x_2)$ |
| 0     | 1      | 1                             | $\neg x_1$ | $x_2$      | $\neg x_1 \rightarrow x_2$       |
| 1     | 0      | 1                             | $x_1$      | $\neg x_2$ | $x_1 \rightarrow \neg x_2$       |
| 1     | 1      | 1                             | $x_1$      | $x_2$      | $x_1 \rightarrow x_2$            |

### Доказательство

Индукцией по количеству связок в формуле $p$:

Пусть в $p$ имеется $k$ связок

* **База индукции**
   $k = 0$. Тогда $p = x_1$.

   Если $x_1$ интерпретировано как $1, $ то $q = p$. И в этом случае, конечно,$q \rightarrow p$. Ну а отсюда $q \vdash p = p'$

   $x_1 = 0: q = \neg x_1, p' = \neg p = \neg x_1$, значит $q \vdash p'$

 * __Шаг индукции__ 

   Пусть у нас связок $< k$, то такое уже умеем доказывать. Рассмотрим, когда у нас в формуле $p$ ровно $k$ связок. Рассмотрим последнюю связку, с помощью который была получена $p$.

   1. $p = \neg S$. Зафиксируем некую интерпретацию, и тогда по __Переходу индукции__ из $\{q_1, ..., q_n\} \vdash S'$

      * Если значение $S$ равно 1, то тогда $S' = S$, а значение $p = 0$. Тогда $p' = \neg p$

        Я хочу из $S' \vdash p'$, значит из $S$ нужно вывести $\neg p$ ($S \vdash \neg p$)

        $S \vdash \neg p = \neg \neg S$

      * Если зн. $S = 0$, $S' = \neg S,  p' = p, $ тогда $\neg S \vdash \neg S$. ну а $x_1 \rightarrow x_1$ является формальной теоремой, подставляем

   2. $p = S \rightarrow t$. Зафиксируем некую интерпретацию, у $S$ и $t$ связок $< k$, значит из $\{q_1, ..., q_n\} \vdash S', \{q_1, ...., q_n\} \vdash t'$

      * Если зн. $S = 1$ и зн. $t = 1$, то $S' = S, t' = t$, следовательно $p'=p$. Нужно $S',t \vdash p'$. Из $q_1, q_2,...,q_n \vdash t' = t$, тогда $q_1, q_2, ..., q_n, S \vdash t'$, по теореме о дедукции $q_1, q_2, ..., q_n \vdash S' \rightarrow t' = S \rightarrow t =p =p'$;

      * Если зн. $S = 1, t = 0$, то $S' = S, t' = \neg t$, зн. $p = 0, p' = \neg p$

        Нужно показать, что $S' t' \vdash p' = \neg p = \neg(S \rightarrow t)$ , для этого покажем что $S' \rightarrow (t' \rightarrow p' )$, подставив $S, t, p$ , получим $S \rightarrow (\neg t \rightarrow \neg(S \rightarrow t))$ . Рассмотрим 5.3 аксиому, где $x_1 = S \rightarrow t, x_2 =t$ тогда получим $((S \rightarrow t) \rightarrow t) \rightarrow (\neg t \rightarrow \neg (S \rightarrow t))$. Заметим, что правая часть это как раз то, что мы хотим вывывести, а для этого достаточно $S \vdash ((S \rightarrow t) \rightarrow t)$, а для этого достаточно $S, S \rightarrow t \vdash t$, а это очевидно(МР)

      * Если зн. $S = 0, S' = \neg S$, зн. $p = 1$, значит $p' = p$

        Нужно показать, что $S' \vdash p' = p = S \rightarrow t$, по теореме о дедукции достоточно $S', S \vdash t$ т.е $\neg S, S \vdash t$, рассмотрим акс 1.1 $\neg S \rightarrow (\neg t \rightarrow \neg S)$, согласно МР $\neg S, S \vdash \neg t \rightarrow \neg S $ , воспользуемся акс 5.3 и МР, тогда $ \neg S, S \vdash \neg \neg S \rightarrow \neg \neg t $, заметим, что $S \vdash \neg \neg S$, но тогда $\neg S, S \vdash \neg \neg t$(MP), посколько $\neg \neg t \rightarrow t$ формальная теорема, то $\neg S, S \vdash t$

   3. $p = S \land t$. Фиксируем некую интерпретацию.

      * Если S и t имеют зн. 1, p зн. 1, то $s' =s, t' = t, p' = p$

        $S \rightarrow (t \rightarrow s \land t)$

        $(S \rightarrow t) \rightarrow ((S \rightarrow t) \rightarrow (S \rightarrow S \land t ))$ акс 2.3

        По МР получаем $(S \rightarrow t) \rightarrow (S \rightarrow S \land t )$.

        Значит $S \rightarrow t \vdash S \rightarrow S \land t $, а отсюда следует $S, S \rightarrow t \vdash S \land t$.

        Поскольку $S, t \vdash S \rightarrow t$, имеем $S, t \vdash S \land t$, т.е $S', t' \vdash p'$

      * Если $S = 0, S' = \neg S, p' = \neg p$

        $\neg S \vdash \neg p$

        $\neg S \vdash \neg (S \land t)$

        $S \land t \rightarrow S$

        $\neg S \rightarrow \neg (S \land t)$

   4. $p = s \lor t$ проделать самостоятельно 

   5. $p = S \leftrightarrow t$ 

## Лемма 2

Формула $\neg (x_1 \land \neg x_1)$ является формальной теоремой.

### Доказательство

### что за пример 4в

Рассмотрим $x_1 \rightarrow ((x_2 \rightarrow x_2) \rightarrow x_1)$ - первая аксиома из второй(1 ?) группы, только вместо $x_2$ подставляем $x_2 \rightarrow x_2$. Из этого мы можем получить

$\neg x_1 \rightarrow (x_1 \rightarrow \neg (x_2 \rightarrow x_2))$

**по формуле $\neg S \rightarrow (S \rightarrow t)$ (пример 4в) получаем**

$\neg x_1 \land x_1 \rightarrow \neg (x_2 \rightarrow x_2)$

Применяем 5.3

$\neg \neg (x_2 \rightarrow x_2) \rightarrow \neg (\neg x_1 \land x_1)$

Применяем $x_1 \rightarrow \neg \neg x_1$

$(x_2 \rightarrow x_2) \rightarrow \neg (\neg x_1 \land x_1)$

$(x_2 \rightarrow x_2)$ - формальная теорема, поэтому ее можно отбросить

## Лемма 3

Формула $x_1 \lor \neg x_1$ - формальная теорема

### Доказательство

Здесь потребуется 3-я группа аксиом.

$x_1 \rightarrow x_1 \lor \neg x_1$

$\neg x_1 \rightarrow x_1 \lor \neg x_1$

$\neg(x_1 \lor \neg x_1) \rightarrow \neg x_1$

$\neg(x_1 \lor \neg x_2) \rightarrow \neg\neg x_1$

$\neg(x_1 \lor \neg x_1) \rightarrow \neg x_1 \land x_1$

$\neg(\neg x_1 \land x_1) \rightarrow \neg\neg(x_1 \lor \neg x_2) \rightarrow x_1 \lor \neg x_1$

## Лемма 4

Если $\Gamma,\ p\vdash q$ и $\Gamma, \neg p \vdash q$, то $\Gamma \vdash q$ 

### Доказательство

По теореме дедукции

$\Gamma \vdash p \rightarrow q$ $\Gamma \vdash \neg p \rightarrow q$

По аксиоме 3.3

$\Gamma \vdash (p \or \neg p) \rightarrow q$

Лемма 3, MP

$\Gamma \vdash q$

## Теорема о полноте

Всякая тавтология является формальной теоремой.

### Доказательство

Пусть $p$ - формула, являющаяся тавтологией, $x_1, ..., x_n$ - ее предметные символы, содержащиеся в ее записи.

Выберем интерпретацию с произвольными значениями предметных символов $x_1, x_2, …, x_{n – 1}$ и единичной интерпретацией символа $x_n$. Обозначим через $\Gamma$ множество ${ q_1, q_2, …, q_{n – 1} }$.

Поскольку $p$ – тавтология, по лемме 1: $\Gamma \cup { x_n } \vdash p$. Выберем ту же интерпретацию для $x_1, x_2, …, x_{n – 1}$ и нулевую для символа $x_n$.

Опять-таки по лемме 1: $\Gamma \cup { \neg x_n } \vdash p.$

По лемме 4: $\Gamma \vdash p.$ Поскольку интерпретация была любой, то множество $\Gamma$ можно урезать, удалив $x_{n – 1}$.

И т.д.

В конце концов, получим $\vdash p$, т.е. $p$ является формальной теоремой.

## Теорема о разрешимости

$\exists​$ алгоритм, позволяющий по формуле узнать является ли она теоремой.

$\neg S \vdash S \rightarrow t$

### Доказательство

(по акс 1.1) $\neg S \rightarrow ((\neg t) \rightarrow(\neg S)) $

(MP) $ \neg S \vdash (\neg t) \rightarrow (\neg S) $

(по аксиоме 5.3) $\vdash (\neg \neg S) \rightarrow (\neg \neg t)$

$\neg S \vdash S \rightarrow t$