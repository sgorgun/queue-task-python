# Queue (python)

Set of programming assignments that are designed to test knowledge of queue data structure.

### Default interface for Queue data structure

The following snippet contains the default interface that could be used for implementation of Queue data structure. Of course the interface could be expanded with additional methods if needed.

```python
class Queue:
    """Default interface for Queue data structure."""

    def __init__(self):
        pass

    def empty(self) -> bool:
        """Returns True if the queue is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def size(self) -> int:
        """Returns the number of elements within the queue.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def push(self, element: Any):
        """Adds a given element to the queue's tail.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def pop(self) -> Any:
        """Returns the head element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        pass

    def peak(self) -> Any:
        """Returns the head element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        pass
```

You may find the interface above here: `tasks/queue.py:Queue`.

## Problem 1: Implement queue using the default interface

Your first programming assignment is to implement the provided default interface for Queue above.
Tests will check your implementation in different scenarios, for simplicity you may assume that only numeric elements will be used for testing.


Please use a template for the implementation (`tasks/queue.py:Queue`).


## Problem 2: Implement queue using two stacks

Your task is to implement queue data structure using only two stacks. For this programming assignment you should re-use your solution for the first problem from the Stack problem set (`Problem 1: Implement stack using the default interface`).


Please use a template for the implementation (`tasks/queue.py:QueueViaStacks`).


## Problem 3: Calculate the number of islands in a given grid

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

Input:
```
000000000
001111100
001101000
001100000
000000000
```

Expected result: 1.

Explanation: there is the only one island in the middle.

**Example 2:**

Input:
```
000000000
001110000
001100000
001100011
000000011
```

Expected result: 2.

Explanation: there is one island in the middle, and the second one is in the bottom-right corner.

Please use a template for the implementation (`tasks/islands.py:get_islands_count`).


## Problem 4: Minimum knight moves (with obstacles)

For a given `chessboard` (`8 x 8` cells) you need to determine the minimal number of moves for the knight (`K` character) to reach the destination cell (`D` character). It is guaranteed the answer exists.

There are four types of cells available:

* `K` - the knight. It is guaranteed it exists on the board.
* `D` - the destination cell. It is guaranteed it exists on the board.
* `O` - obstacles. The knight cannot go to cells with obstacles.
* `.` - empty cells, the knight can go to such cells.

**Eligible knight moves**
![alt text](imgs/knight_moves.png "Eligible knight moves")

**Example 1:**

Input:
```
K.......
........
........
........
........
........
........
.....D..
```

Expected result: 4.

Explanation:
```
K.......
........
.1......
........
..2.....
........
...3....
.....D..
```

**Example 2:**

Input:
```
K...O...
.....O..
.O..OO..
.O......
...O.O..
O.OOO...
O.......
O....D..
```

Expected result: 6.

Explanation:
```
K...O...
..1..O..
2O..OO..
.O3.....
...O4O..
O.OOO.5.
O.......
O....D..
```

Please use a template for the implementation (`tasks/knight.py:get_minimum_knight_moves`).
