
class TreeNode:
    def __init__(self, root_value):
        self.root = root_value
        self.left_chid = None
        self.right_chid = None

class Binary_search_tree:
    """Implements the BST"""
    
    def __init__(self, root):
        self.bst = TreeNode(root)
    
    def insert(self, element):
        
        new_node = TreeNode(element)
        current_root = self.bst
        while(current_root.root is not None):
            if current_root.root > element :
                current_root = current_root.left_chid
            else:
                current_root = current_root.right_chid
        current_root = new_node
