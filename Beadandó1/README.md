[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/eNaAwWLc)
# Mesterséges Intelligenciák I. beadandó feladat

|                     |                |
| ------------------- | -------------- |
| Név                 | Sindely Richárd |
| NEPTUN              | P1UV07         |
| Programozási nyelv  | Python           |
| Eltöltött idő (óra) | ~17              |
| Mi volt unalmas?    |   -             |
| Mi volt érdekes?    |   Az órán foglalkoztunk ezekkel az algoritmusokkal és érdekes volt ezeket kódba megírni             |
| Mi volt nehéz?      |    A kiterjesztések megszámolása            |

## Feladat

A feladat egyszerű és optimális keresők programozása
**választott programozási nyelvben**.
A teszteléshez a gráfok a [`graphs.txt`](./graphs.txt) fájlban találhatóak.
A feladatot **egyénileg kell elkészíteni**, a félév végén **mindenkinek be kell mutatnia a megoldását**!

Implementálja és tesztelje az alábbi algoritmusokat:

- DFS
- BFS
- Hegymászó keresés (Hill-climbing)
- Nyalábkeresés (Beam search)
  - $w = 2$
- Elágazás és korlátozás (B&B)
  - Mindhárom verzió
- A\*

A programnak képesnek kell lennie a graphs.txt beolvasására és a gráf automatikus felépítésére!

### Dokumentáció

Az algoritmusok működését és a kapott eredményeket dokumentálja!

- Algoritmusok ismertetése
- Futási eredmények (útvonal, hossz)
- Futási idő
- Kiterjesztett csomópontok száma

A fájl tetején található `yaml` táblázat kitöltése egyéni bevallás alapján kötelező!

[Angol nyelvű segédlet](./tutorial.md).

## Algoritmusok bemutatása

### DFS
DFS elindul a kezdő csúcstól mélységben keres, vagyis a legmélyebb csúcsig megy,majd visszafelé halad,amíg más elágazási lehetőség nem akad.

### BFS
BFS minden szomszédot megvizsgál mielött a következő szintre lépne. BFS a legrövidebb utat találja meg a gráfban.

### HC
Hill Climbing egy heurisztikus kereső algoritmus. Minden lépésben a legjobb szomszédot választja.

### Beam
Beam Search egy heurisztikus keresési algoritmus. BFS-hez hasonlóan szintenként vizsgálja a csúcsokat,de a teljes szint helyett csak a legjobb w csúcsokat tartja meg.

### B&B
Branch and Bound algoritmus az utak halmozott költsége alapján keresi meg a legjobb utat.

#### Lista
Branch and Bound Lista algoritmus egy kiterjesztett listát alkalmaz,amely a már meglátogatott csomópontokat tartalmazza,így ezzel a módszerrel csökkenti a felesleges útvonalakat.

#### Heurisztika
Branch and Bound heurisztika algoritmus úgy működik mint a Branch and Bound csak figyelembe kell venni a a célhoz való becsült heurisztikus költséget is. Ez az algoritmus lehetővé teszi a legalacsonyabb költségű út hatékony keresését.

### A\*
Az A* algoritmus a költség + heurisztika alapján választja ki azokat a csomópontokat, amelyek a legközelebb vezetnek a célhoz, miközben egy kiterjesztett lista segítségével megelőzi a csomópontok ismételt feldolgozását. Ezzel hatékonyan és optimálisan találja meg a legrövidebb utat.

## Futási eredmények

### GRAPH_1

| Algoritmus   | Útvonal | Futási idő (mp) | Kiterjesztések száma |
| :----------- | :------ | :-------------: | :------------------: |
| DFS          |   ['a', 'b', 'c', 'd']      |      0.000189 sec           |           5           |
| BFS          |   ['a', 'b', 'd']      |          0.000239 sec       |       7               |
| HC           |    ['a', 'b', 'c', 'd']     |      0.000173 sec          |            5          |
| Beam         |     ['a', 'b', 'c', 'd']    |        0.000164 sec         |           8           |
| B&B          |    ['a', 'c', 'd']     |     0.000155 sec            |            8          |
| B&B w. List  |  ['a', 'b', 'd']       |     0.000153 sec            |           4           |
| B&B w. Heur. |   ['a', 'c', 'd']      |        0.000206 sec         |          8            |
| A\*          |    ['a', 'b', 'd']     |    0.000177 sec             |          4            |

### GRAPH_2

| Algoritmus   | Útvonal | Futási idő (mp) | Kiterjesztések száma |
| :----------- | :------ | :-------------: | :------------------: |
| DFS          |    ['S', 'A', 'C', 'D', 'E', 'F', 'G']     |      0.000203 sec           |         16             |
| BFS          |     ['S', 'A', 'C', 'E', 'G']    |       0.000566 sec          |          50            |
| HC           |   ['S', 'A', 'D', 'H', 'F', 'G']      |       0.000191 sec          |          10            |
| Beam         |   ['S', 'B', 'Y', 'C', 'E', 'G']      |        0.000165 sec         |         14             |
| B&B          |    ['S', 'B', 'C', 'E', 'G']     |      0.000183 sec           |         31             |
| B&B w. List  |   ['S', 'B', 'C', 'E', 'G']      |      0.000159 sec           |         11             |
| B&B w. Heur. |  ['S', 'B', 'C', 'E', 'G']       |      0.000199 sec           |            13          |
| A\*          |   ['S', 'B', 'C', 'E', 'G']      |     0.000210 sec            |            10          |
