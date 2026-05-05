#!/usr/bin/python3
"""Class Node of a stingly linked list"""


class Node:
    """Class definition of the Node nice"""

    def __init__(self, data, next_node = None):
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
        if not None or not isinstance(value, object):
            raise TypeError("next_node must be a Node object")

class StinglyLinkedList(Node):
    """The StignlyLinkedList class"""

    def __init__(self):
        self.__data = []
        
    def sorted_insert(self, value):
        self.__data.append(value).sort()
