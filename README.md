# Queue

## Purpose

The coding exercises are designed to test knowledge of the following concepts:

* The default Queue interface
* Queue via two Stacks
* Usage of Queue data structure in practice

## Overview

The coding exercises cover the following practical problems:
* Implementing the default Queue interface
* Implementing Queue via two Stacks
* Calculating the number of islands in a grid
* Knight traversal


## Coding exercises

### Exercise 1: Implement the default Queue interface

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

Your task is to implement the provided default interface for Queue above.

Please use a template for the implementation (`tasks/queue.py:Queue`).

## Exercise 2: Implement queue using two stacks

Your task is to implement Queue data structure using only two Stacks. For this exercise you should re-use your solution for the first problem from the Stack problem set (`Exercise 1: Implement the default Stack interface`).
Replace a template `tasks/stack.py:Stack` with your solution.

The proposed template for you to use:
```python
class QueueViaStacks:
    """Default Queue interface implemented with two stacks only.

    NOTE: Stack interface is defined within `tasks/stack.py:Stack`, you may re-use
    the existing implementation (you should have created it at this point).

    NOTE: all methods of Queue interface should be implemented.
    """

    def __init__(self):
        # NOTE: __init__ shouldn't be changed.
        self.first_stack = Stack()
        self.second_stack = Stack()

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

Please use a template for the implementation (`tasks/queue.py:QueueViaStacks`).


## Exercise 3: Calculate the number of islands in a grid

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Your task is implement the following function that solves the problem above:

```python
def get_islands_count(grid: List[List[str]]) -> int:
    """Returns the number of islands in a given grid.

    Hint: you need to go over the grid and 'explore' islands
    one by one, some sort of BFS (using queue) will do.
    """
    pass
```

**Example 1:**

`grid`:
```
000000000
001111100
001101000
001100000
000000000
```

Expected output: 1.

Explanation: there is the only one island in the middle.

**Example 2:**

`grid`:
```
000000000
001110000
001100000
001100011
000000011
```

Expected output: 2.

Explanation: there is one island in the middle, and the second one is in the bottom-right corner.

Please use a template for the implementation (`tasks/islands.py:get_islands_count`).


## Exercise 4: Knight traversal

For a given `chessboard` (`8 x 8` cells) you need to determine the minimal number of moves for the knight (`K` character) to reach the destination cell (`D` character). It is guaranteed the answer exists.

There are four types of cells available:

* `K` - the knight. It is guaranteed it exists on the board.
* `D` - the destination cell. It is guaranteed it exists on the board.
* `O` - obstacles. The knight cannot go to cells with obstacles.
* `.` - empty cells, the knight can go to such cells.

**Eligible knight moves**
![alt text](imgs/knight_moves.png "Eligible knight moves")

Your task is implement the following function that solves the problem above:

```python
def get_minimum_knight_moves(chessboard: List[List[str]]) -> int:
    """Returns the minimum knight moves to reach the destination point."""
    pass
```

**Example 1:**

`chessboard`:
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

Expected output: 4.

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

`chessboard`:
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

Expected output: 6.

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
