#!/usr/bin/python3
"""Module that defines a Node and SinglyLinkedList classes."""


class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node = None):
        """Initialize a new Node instance.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class StinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList instance."""
        self.__head = None

    def __Str__(self):
        """Print the entire list in stdout."""
        result =""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip
 
    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = current.next_node
            current.next_node = new_node


