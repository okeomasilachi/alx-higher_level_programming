#!/usr/bin/python3

class Node:

    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise TypeError("data must be an integer")
        elif type(next_node) != Node and next_node != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(next_node) != Node and next_node != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = []

    def sorted_insert(self, value):
        self.__head.append(value)
        self.__head.sort()

    def __str__(self):
        string = ""
        j, k = 0, len(self.__head)
        for i in self.__head:
            j += 1
            if j == k:
                string += f"{i}"
            else:
                string += f"{i}\n"
        return string    
