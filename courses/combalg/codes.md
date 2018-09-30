---
title: Коды алгоритмов
layout: math
toc: true
---

[Старая версия .docx](files/shpora.docx)

## Минимальный остов

Поиск минимального остова во взвешенном графе

### Борувки-Краскала

Сложность: $O(m⋅log(n))$



Опишем процедуру $Merge(v, w, p, q)$, предназначенную для слияния двух деревьев $H_1 = (V_1, E_1)$ и $H_2 = (V_2, E_2)$ по ребру $vw$, внешнему к основному лесу $F$. Предполагается, что $v \in V_1$, $w \in V_2$, $p = name[v]$, $q = name[w]$.

```python
def Merge(v, w, p, q):
    name[w] = p
    u = next[w]
    while name[u] != p:
        name[u] = p
        u = next[u]
    size[p] += size[q]
	next[v], next[w] = next[w], next[v]
```



Алгоритм:

Вход: связный взвешенный граф $G = (V, E, c)$.

Выход: минимальный остов $T$ графа $G$.

```python
Q = Queue(Sorted(E))
for v in V:
    name[v] = next[v] = v
    size[v] = 1
T = []
while len(T) != n - 1:
    vw = Q.dequeue()
    p, q = name[v], name[w]
    if p != q:
        if size[p] > size[q]:
            Merge(w, v, q, p)
        else:
        	Merge(v, w, p, q)
        T.append(vw)
```



### Ярника-Прима-Дейкстры

Сложность: $O(n^2)$



Вход: связный взвешенный граф $G = (V, E, c)$, заданный матрицей весов `A[n][n]`

Выход: минимальный остов $T$ графа $G$.

```python
w = V[0]
W = V.difference(w)
T = []
for v in V:
    near[v] = w
    d[v] = A[v][w]
while len(T) != n - 1:
    v = Min(W)
    u = near[v]
    T.append(vu)
    W = W.difference(v)
    for u in W:
        if d[u] > A[u][v]:
            near[u] = v
            d[u] = A[u][v]
```



## Кратчайший путь

Поиск кратчайшего пути во взвешенном графе

### Форда-беллмана

Сложность: $O(n^3)$



Вход: сеть $G = (V, E, c)$, заданная матрицей весов `A[n][n]`. Вершины `s` и `t`.

Выход: расстояния `D[v]` от `s` до всех вершин $v \in V$, стек $S$, содержащий кратчайший $(s,t)-$путь, или сообщение, что искомого пути в сети не существует.

```python
def Distance:
    D[s] = prev[s] = 0
    for v in V.difference(s):
        D[v] = A[s][v]
        prev[v] = s
    for k in range(n-2):
		for v in V.difference(s):
            for w in V:
                if D[w] + A[w][v] < D[v]:
                    D[v] = D[w] + A[w][v]
                    prev[v] = w
```

```python
Distance()
if D[t] < sys.maxsize:
    S.push(t)
    v = t
    while prev[v] != 0:
        v = prev[v]
        S.push(v)
else:
    print("Not exists")
```



### Дейкстра

Сложность: $O(n^2)$



(нахождение расстояний от фиксированной вершины до всех остальных в сети с неотрицательными весами)

Вход: сеть $G=(V,E,c)$, заданная матрицей весов `A[n][n]`, выделенная вершина `s`.

Выход: расстояния `D[v]` от `s` до всех вершин $v \in V$, `prev[v]` - предпоследняя вершина в катчайшем $(s,v)-$пути.

```python
D[s] = prev[s] = 0
F = V.difference(s)
for v in F:
    D[v] = A[s][w]
    prev[v] = s
for k in range(n-1):
    w = Min(F)
    F = F.difference(w)
    for v in F:
        if D[w] + A[w][v] < D[v]:
            D[v] = D[w] + A[w][v]
            prev[v] = w
```



### Алгоритм топологической сортировки 10.3

Сложность: $O(m)$



Вход: бесконтурный орграф $G = (V, E)$, заданный списками смежностей $\stackrel{\rightarrow}{list}[v]$

Выход: массив $Index$ длины $n$ такой, что для любой дуги $vw \in E$ справедливо неравенство $Index[v]  < Index[w]$

```python
for v in V:
    DegOut[v] = 0
for v in V:
    for w in List[v]:
        DegOut[w] += 1
Q = Queue()
number = n
for v in V:
    if DegOut[v] = 0:
        Q.enqueue(v)
    while Q:
        v = Q.dequeue()
        Index[v] = number
        number -= 1
        for w in List[v]:
            DegOut[w] -= 1
            if DegOut[w] = 0:
                Q.enqueue(v)     
```



### Алгоритм 10.4

Сложность: $O(m)$



(вычисление расстояний от вершины $v_1$ в бесконтурной сети)

Вход: бесконтурная сеть $G = (V, E, c)$ с топологически отсортированными вершинами, заданная списками $\stackrel{\rightarrow}{list}[v]$

Выход: расстояния $D[v]$ от $v_1$ до всех $v \in V$, $prev[v] - $ предпоследняя вершина в кратчайшем $(v_1, v)-$пути.

```python
D[V[1]] = 0
prev[V[1]] = 0
for k in range(2, n+1):
    D[V[k]] = sys.maxsize
for k in range(2, n+1):
    for w in List[V[k]]:
        if D[w] + c(w, V[k]) < D[V[k]]:
            D[V[k]] = D[w] + c(w, V[k])
            prev[V[k]] = w
```



### Флойда

Сложность: $O(n^3)$



(вычисление расстояий между всеми парами вершин)

Вход: сеть $G = (V, E, c)$, заданная матрицей весов `A[n][n]`

Выход: расстояния `D[i][j]` для всех пар $v_i, v_j \in V$, матрица `prev`, в которой `prev[i][j]` равно номеру предпоследней вершины в кратчайшем $(v_i, v_j)-$пути.

```python
for i in range(n):
    for j in range(n):
		D[i][j] = A[i][j]
        prev[i][j] = i
    for k in range(n):
		for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    prev[i][j] = prev[k][j]
```



## Сроки выполнения работ

### Алгоритм 10.5

(расчет наиблее ранних возможных сроков начала и выполнения работ)



Вход: сетевой график $G$ работ $V$, заданный списками $prev(v), v \in V$

Выход: наиболее ранние возможный сроки начала и выполнения работ $ebeg[v], efin[v], v \in V$

```python
for k in range(n+2):
    ebeg[k] = efin[k] = 0
for k in range(1, n+2):
    for i in prev(k):
        ebeg[k] = max(efin[i], ebeg[k])
    efin[k] = ebeg[k] + time[k]
```

В этом алгоритме вершины сетевого графика `s` и `t` обозначены соответсвтенно через `0` и `n+1`.



### Алгоритм 10.6

(расчет наиболее поздних сроков начала и окончания работ)



Вход: сетевой график $G$ работ $V$, заданный списками $prev[v], v \in V$, плановый срок окончания проекта - $T$.

Выход: наиболее поздние допустимые сроки выполнения и начала работ $lfin[v]$ и $lbeg[v]$.

```python
for v in V:
    lfin[v] = T
for k in reversed(range(1, n+2)):
    lbeg[k] = lfin[k] - time[k]
    for i in prev[v]:
        lfin[i] = min(lfin[i], lbeg[k])
```



## Максимальный поток

### Алгоритм Форда-Фалкерсона

Сложность: $O(n^5)$



Опишем вначале процедуру помечивания вершин в сети $G$. Эта процедура является модифицированной версией процедуры поиска в ширину. В ней через $Q$ обозначена очередь, в окторую заносятся помеченные вершины.

```python
def Labeling(f):
    for v in V:
        h[v] = sys.maxsize
    Q = Queue()
    Q.enqueue(s)
    prev[s] = None
    while h[t] == sys.maxsize and Q:
        w = Q.dequeue()
        for v in V:
            if h[v] != sys.maxsize and A[w][v] - F[w][v] > 0:
                h[v] = min(h[w], A[w][v] - F[w][v])
             	prev[v] = w
                Q.enqueue(v)
                choice[v] = 1
            for v in V.difference(s):
                if h[v] == sys.maxsize and F[w][v] > 0:
                    h[v] = min(h[w], F[w][v])
                    Q.enqueue(v)
                    father[v] = w
                    choise[v] = -1 
```

Алгоритм:

Вход: сеть $G = (V, E, c)$, заданная матрицей пропускный способностей `A[n][n]`, источник `s`, сток `t`.

Выход: максимальный поток `f`, заданный матрицей $F$ порядка $n$, для которой $F[v, w] = f(v, w), \|f\| -$величина максимального потока.

```python
for v in V:
    for w in V:
        F[v][w] = 0
|f| = 0
while True:
    Labeling(f)
    if h[t] < sys.maxsize:
        |f| += h[t]
        v = t
        while v != s:
            w = prev[v]
            if choise[v] = 1:
                F[w][v] += h[t]
            else:
                F[v][w] -= h[t]
            v = w
    if h[t] = sys.maxsize:
        break
```