class LinkedList:
    """
    This is my Own Linked List
    """

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                previous = node
                node = node.next
                node.previous = previous

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append({'Previous Node': node.previous, 'Actual Node Data': node.data, 'Next Node': node.next})
            node = node.next
        # nodes.append("\n")
        return str(nodes)


class Node:
    """
    This Class will server as a node for the Linked List
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    # Return Data with repr()
    def __repr__(self):
        return self.data
