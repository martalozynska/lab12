"""
File: node.py

Node classes for one-way linked structures and two-way
linked structures.
"""

class Node(object):

    def __init__(self, data, next1 = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next1 = next1

class TwoWayNode(Node):

    def __init__(self, data, previous = None, next1 = None):
        Node.__init__(self, data, next1)
        self.previous = previous

# Just an empty link
node1 = None

# A node containing data and an empty link
node2 = Node("A", None)

# A node containing data and a link to node2
node3 = Node("B", node2)
