
class TreeNode:
    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
    
    def is_left_child(self):
        return self.parent and self.parent.left_child is self
    
    def is_right_child(self):
        return self.parent and self.parent.right_child is self
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not (self.left_child or self.right_child)
    
    def has_any_child(self):
        return self.left_child or self.right_child
    
    def has_child(self):
        return self.left_child and self.right_child
    
    def replace(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self


class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value, self.root)
        self.size += 1
    
    def _put(self, key, value, current):
        if key < current.key:
            if current.left_child:
                self._put(key, value, current.left_child)
            else:
                current.left_child = TreeNode(key, value, parent=current)
        else:
            if current.right_child:
                self._put(key, value, current.right_child)
            else:
                current.right_child = TreeNode(key, value, parent=current)
    
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
        return None
    
    def _get(self, key, current):
        if current is None:
            return None
        elif key == current.key:
            return current
        elif key > current.key:
            return self._get(key, current.right_child)
        else:
            return self._get(key, current.left_chid)
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        return bool(self._get(key, self.root))