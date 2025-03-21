class Node:
    """Represents the node"""
    
    def __init__(self, node_data):
        """Initialization of nodes"""
        self._data = node_data
        self._next = None  # Default next reference to None
    
    @property
    def data(self):
        """Data getter"""
        return self._data
    
    @data.setter
    def data(self, node_data):
        """Data setter"""
        self._data = node_data
    
    @property
    def next(self):
        """Next reference getter"""
        return self._next
    
    @next.setter
    def next(self, next_node):
        """Next reference setter"""
        self._next = next_node