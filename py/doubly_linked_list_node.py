import linked_list_node

class DoublyNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.prev = None