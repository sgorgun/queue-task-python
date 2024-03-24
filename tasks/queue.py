"""Templates for programming assignments: queue API."""
from typing import Any, Optional

from tasks.stack import Stack, LinkedListNode

# The following snippet contains the default interface, which can be used to implement the queue data structure. Of course, the interface can be expanded with additional methods if necessary.
class Queue:
    """Default interface for Queue data structure."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def empty(self) -> bool:
        """Returns True if the queue is empty.

        NOTE: O(1) complexity is expected for this operation.
        """
        return self._size == 0

    def size(self) -> int:
        """Returns the number of elements within the queue.

        NOTE: O(1) complexity is expected for this operation.
        """
        return self._size

    def push(self, element: Any):
        """Adds a given element to the queue's tail.

        NOTE: O(1) complexity is expected for this operation.
        """
        new_node = LinkedListNode(element)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_element = new_node
            self.tail = new_node
        self._size += 1

    def pop(self) -> Any:
        """Returns the head element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.empty():
            raise ValueError
        value = self.head.value
        self.head = self.head.next_element
        self._size -= 1
        return value

    def peak(self) -> Any:
        """Returns the head element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.empty():
            raise ValueError
        return self.head.value


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
        return self.first_stack.empty() and self.second_stack.empty()

    def size(self) -> int:
        """Returns the number of elements within the queue.

        NOTE: O(1) complexity is expected for this operation.
        """
        return self.first_stack.size() + self.second_stack.size()

    def push(self, element: Any):
        """Adds a given element to the queue's tail.

        NOTE: O(1) complexity is expected for this operation.
        """
        self.first_stack.push(element)

    def pop(self) -> Any:
        """Returns the head element and removes it.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.empty():
            raise ValueError("Queue is empty")
        if self.second_stack.empty():
            while not self.first_stack.empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.pop()

    def peak(self) -> Any:
        """Returns the head element.

        NOTE: O(1) complexity is expected for this operation.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.empty():
            raise ValueError("Queue is empty")
        if self.second_stack.empty():
            while not self.first_stack.empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.peak()
