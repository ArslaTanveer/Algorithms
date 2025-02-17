Insert Sort
-----------

> [!Note]
>The code available [here](https://github.com/ArslaTanveer/Algorithms/blob/main/implementations/sorting/sorting.py) assumes demonstration of Bubble Sorting already known

Assume the following that you got cards:
```
+----+
| 12 |-------> Border Position
+----+
| 47 |-------> Reading Position
+----+
| 85 |
+----+
| 23 |
+----+
| 59 |
+----+
```
From the Reading position, we know that we start from 1 position (assuming the first item is zero), and we move to the final position, which is a total number of items so:
```python
for i in range(1, len(array)):
```
We take two key things here that change every time the loop changes, the Border Position and Reading Position which increments every time, so for the next loop:
```
+----+
| 12 |
+----+
| 47 |-------> Border Position
+----+
| 85 |-------> Reading Position
+----+
| 23 |
+----+
| 59 |
+----+
```
For this, we write:
```python
    MoveItem = array[i]
    BorderItemPosition = i - 1
```
Obviously now `MoveItem` is what we are reading, and Border Position is positioned above it, continue by writing:

```python
    while (MoveItem < array[BorderItemPosition]) and (BorderItemPosition > -1) :
```

Now, we continue looping until we reach the top, `BorderItemPosition > -1`, and if `MoveItem` is less than data at `BorderItemPosition`, it moves up.

For the final part:
```python
        array[BorderItemPosition+1] = array[BorderItemPosition]
        BorderItemPosition -= 1
        array[BorderItemPosition+1] = MoveItem
```
If the data has to jump up:
```
1. Move the border item position to up
2. We decrement the border item position. This is because our reading position item which was `MoveItem` goes below
3. Put in that place the new item
```
