"""Templates for programming assignments: queue API."""
from typing import Any, Optional

from tasks.stack import Stack


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
