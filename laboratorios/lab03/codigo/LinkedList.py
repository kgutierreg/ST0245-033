#!/usr/bin/python

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    """docstring for LinkedList."""
    def __init__(self, arg):
        super(LinkedList, self).__init__()
        self.arg = arg
