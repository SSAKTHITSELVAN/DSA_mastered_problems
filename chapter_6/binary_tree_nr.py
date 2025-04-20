"""Creating the binary tree by the node and reference approach"""

class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None
    
    def insert_left_child(self, new_left_child):
        new_child = BinaryTree(new_left_child)
        if self.left_child is None:
            self.left_child = new_child
        else:
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right_child(self, new_right_child):
        new_child = BinaryTree(new_right_child)
        if self.right_child is None:
            self.right_child = new_child
        else:
            new_child.right_child = self.right_child
            self.right_child = new_child
    
    def set_root_val(self, new_value):
        self.root = new_value
    
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child


tree = BinaryTree('A')
tree.insert_left_child('B')
tree.insert_right_child('C')
tree.left_child.insert_left_child('D')
tree.right_child.insert_right_child('E')
