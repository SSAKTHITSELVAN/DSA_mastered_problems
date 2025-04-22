
class BinaryHeap:
    
    def __init__(self):
        self.heap = []
    
    def _percolate_up(self, index):
        while index >= 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            else:
                break
            index = parent_index
    
    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)
    
    def _percolate_down(self, index):
        """Main the heap structure after the deletion"""
        
        while index*2 + 1 >= len(self.heap):
            min_index = self._get_min_index(index)
            if self.heap[index] > self.heap[min_index]:
                self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            else:
                break
            index = min_index
    
    
    def __get_min_index(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        
        if right >= len(self.heap):
            return left
        else:
            if self.heap(right) < self.heap[left]:
                return right
            else:
                return left
    
    def delete(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        element = self.heap.pop()
        self._percolate_down(0)
        return element
    
    def heapify(self, not_a_heap):
        self.heap = not_a_heap[:]  # Copy the input list into the heap
        i = len(self.heap) // 2 - 1  # Start from the last non-leaf node
        while i >= 0:
            self.perc_down(i)       # Fix the heap property at each node
            i = i - 1
