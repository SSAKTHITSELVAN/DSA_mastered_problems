from .binary_search_tree import BinarySearchTree, TreeNode

class AVLBalanceTree(BinarySearchTree):
    
    def _put(self, key, value, current):
        
        if key < current.key:
            if current.left_child:
                self._put(key, value, current.left_child)
            else:
                current.left_child = TreeNode(key, value, 0, parent=current.left_child)
        else:
            if current.right_child:
                self._put(key, value, current.right_child)
            else:
                current.right_child = TreeNode(key, value, 0, parent=current.right_child)
            