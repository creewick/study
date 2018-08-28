<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\(','\)']]}});</script><script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>

[home](../../) > [logic](../) > [0](./) > equiv

# Отношение равносильности

[TOC]

Две формулы **равносильны** ($F \equiv G$), если $BInt(F) = BInt(G)$.

> Отношение равносильности на множестве всех формул рефлексивно, симметрично и тразитивно, то есть это *отношение эквивалентности*, разбивающее это множество на классы равносильных формул.
>
> Например, класс тавтологий и класс противоречий.

##Законы логики высказываний

**1. Законы коммутативности**

- $F \and G \equiv G \and F$ 
- $F \or G \equiv G \or F$
- $F \leftrightarrow G \equiv G \leftrightarrow F$

**2. Законы ассоциативности**

- $F \and (G \and H) \equiv (F \and G) \and H$
- $F \or (G \or H) \equiv (F \or G) \or H$

**3. Законы дистрибутивности**

- $F \and (G \or H) \equiv (F \and G) \or (F \and H)$
- $F \or (G \and H) \equiv (F \or G) \and (F \or H)$

**4. Законы идемпотентности**

- $F \and F \equiv F$
- $F \or F \equiv F$

**5. Законы поглощения**

- $F \and (F \or G) \equiv F$
- $F \or (F \and G) \equiv F$
  $F \or 1 \equiv 1$	 $F \and 1 \equiv F$	 $F \or 0 \equiv F$	 $F \and 0 \equiv 0$

**6. Закон двойного отрицания**

- $¬¬F \equiv F$

**7. Закон импликации**

- $F \to G \equiv ¬F \or G$

**8. Закон контрапозиции**

- $F \to G \equiv ¬G \to ¬F$

**9. Законы де Моргана**

- $¬(F \and G) \equiv ¬F \or ¬G$
- $¬(F \or G) \equiv ¬F \and ¬G$

**10. Закон исключенного третьего**

- $F \or ¬F \equiv 1$

**11. Закон противоречия**

- $F \and ¬F \equiv 0$

**12. Закон эквиваленции**

- $F \leftrightarrow G \equiv (F \to G) \and (G \to F)$

Проверка законов осуществляется с помощью сравнения таблиц истинности.

Знание основных законов логики высказываний позволяет упрощать формулы, т.е. находить равносильную данной наиболее простого вида. А также помогает доказывать равносильность формул.

> Пример: $¬A \and ¬(¬A \and ¬B) \to B \equiv^7 ¬(¬A \and ¬(¬A \and ¬B)) \or B \equiv^9$
>
> $\equiv^9 (¬¬A \or ¬¬(¬A \and ¬B)) \or B \equiv^6 (A \or (¬A \and ¬B)) \or B \equiv^3$
>
> $\equiv^3 (A \or ¬A) \and (A \or ¬B) \or B \equiv^{10} 1 \and (A \or ¬B) \or B \equiv^5$
>
> $\equiv^5 (A \or ¬B) \or B \equiv^2 A \or (¬B \or B) \equiv^{10} A \or 1 \equiv^5 1$