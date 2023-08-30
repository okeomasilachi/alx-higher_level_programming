#!/usr/bin/python3

"""
This program defines a singly linked list and a node class.
"""


class Node:
    """
    A node class for a singly linked list.

    Args:
        data: The data stored in the node.
        next_node: The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize the node.

        Raises:
            TypeError: If `data` is not an integer.
            TypeError: If `next_node` is not a Node object.
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        elif type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Raises:
            TypeError: If `value` is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Get the next node in the list.

        Returns:
            The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the list.

        Raises:
            TypeError: If `value` is not a Node object.
        """
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """"
    A singly linked list class.
    """

    def __init__(self):
        """
        Initialize the linked list.
        """
        self.__head = []

    def sorted_insert(self, value):
        """
        Insert a node with the given value into the linked list in sorted order.

        Args:
            value: The value to insert.
        """
        self.__head.append(value)
        self.__head.sort()

    def __str__(self):
        """
        Get a string representation of the linked list.

        Returns:
            A string representation of the linked list.
        """
        string = ""
        j, k = 0, len(self.__head)
        for i in self.__head:
            j += 1
            if j == k:
                string += f"{i}"
            else:
                string += f"{i}\n"
        return string
