---
title: Логическое следование
layout: math
toc: true
---

Формула $G$ называется **логическим следованием** формул $F_1, F_2, .., F_k$, если для любой интерпретации $\phi$, если $\phi(F_1) = 1, \phi(F_2) = 1, .., \phi(F_k) = 1$, то и $\phi(G) = 1$.

$\{F_1, F_2, .., F_k\} \vDash G​$

## Свойства

- **Рефлексивность:** $\{F_1, F_2, .., F_k\} \vDash F_i , i \in \{1..k\}$
- **Транзитивность:** Eсли $\forall i \in \{1..p\} : \{F_1, F_2, .., F_k\} \vDash G_i$ и $\{G_1, G_2, .., G_p\} \vDash H$, то $\{F_1, F_2, .., F_k\} \vDash H$
- **Монотонность:** Если $\{F_1, F_2, .., F_k\} \vDash G$, то $\forall H : \{F_1, F_2, .., F_k, H\} \vDash G$

## Теорема (критерии)

$\forall F_1, F_2, .., F_k, G$

- $\{F_1, F_2, .., F_k\} \vDash G \Leftrightarrow F_1 \and F_2 \and .. \and F_k \to G$ - тавтология
- $\{F_1, F_2, .., F_k\} \vDash G \Leftrightarrow F_1 \and F_2 \and .. \and F_k \and ¬G$ - противоречие

### Док-во

- - Пусть $F_1, .., F_k \vDash G$ и $\phi$ - произольная интерпретация формулы $F_1 \and .. \and F_k \to G$.

    Тогда если 	 $\exists i \in \{1..k\}: \phi (F_i) = 0$, то $\phi(F_1 \and .. \and F_k) = 0$.

    Следовательно, $\phi(F_1 \and .. \and F_k \to G) = 1$.

    Если $\forall i \in \{1..k\} : \phi(F_i) = 1$, то $\{F_1, F_2, .., F_k\} \vDash G \Rightarrow \phi(G) = 1$

    И потому  $\phi(F_1 \and .. \and F_k \to G) = 1$.

    Так как интерпретация выбрана произвольно, формула является тавтологией.

  - Пусть $F_1 \and F_2 \and .. \and F_k \to G$ - тавтология и $\forall i \in \{1..k\} : \phi(F_i) = 1$.

    Тогда $\phi(F_1 \and..\and F_k) = 1$ и $\phi(F_1 \and..\and F_k \to G) = 1$, откуда $\phi(G) = 1$.

    Ввиду произвольности $\phi$, значит, $\{F_1, F_2, .., F_k\} \vDash G $

- - $¬(F_1 \and..\and F_k \to G) \equiv ¬(¬(F_1 \and..\and F_k) \or G) \equiv ¬¬(F_1 \and..\and F_k) \and ¬G \equiv F_1 \and..\and F_k \and ¬G$

    Поэтому, формула $F_1 \and F_2 \and .. \and F_k \to G$ будет тавтологией тогда и только тогда, когда формула $F_1 \and F_2 \and .. \and F_k \and ¬G$ будет противоречием. 

    Отсюда и из доказанного ранее следует, что $\{F_1, F_2, .., F_k\} \vDash G$ тогда и только тогда, если $ F_1 \and F_2 \and .. \and F_k \and ¬G$ - противоречие