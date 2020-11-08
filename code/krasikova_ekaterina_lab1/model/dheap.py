class DHeap:
    def __init__(self, d=2, data=None):
        self.d = d
        if data is None:
            self.heap = []
        else:
            if not isinstance(data, list):
                raise TypeError("Must be list")
            for elem in data:
                if not (isinstance(elem, int) or isinstance(elem, float)):
                    raise TypeError("Elements must have numeric type")
            self.heap = data
            for i in range(len(self.heap)-1, -1, -1):
                self._diving(i)

    def _parent(self, i):
        if i > 0 and i < len(self.heap):
            return (i - 1) // self.d
        else:
            return -1

    def _left_child(self, i):
        if i >= 0 and self.d * i + 1 < len(self.heap):
            return self.d * i + 1
        else:
            return -1

    def _min_child(self, i):
        lc = self._left_child(i)
        if lc == -1:
            return -1
        mc = lc
        for j in range(lc+1, min(lc + self.d, len(self.heap))):
            if self.heap[j] < self.heap[mc]:
                mc = j
        return mc
    
    def _emersion(self, i):
        j1 = i
        j2 = self._parent(j1)
        while j2 != -1 and self.heap[j2] > self.heap[j1]:
            self.heap[j1], self.heap[j2] = self.heap[j2], self.heap[j1]
            j1 = j2
            j2 = self._parent(j1)

    def _diving(self, i):
        j1 = i
        j2 = self._min_child(j1)
        while j2 != -1 and self.heap[j1] > self.heap[j2]:
            self.heap[j1], self.heap[j2] = self.heap[j2], self.heap[j1]
            j1 = j2
            j2 = self._min_child(j1)

    def insert(self, w):
        if not (isinstance(w, int) or isinstance(w, float)):
            raise TypeError("Elements must have numeric type")
        self.heap.append(w)
        self._emersion(len(self.heap) - 1)
        
    def min(self):
        return self.heap[0]

    def delete_min(self):
        if len(self.heap) == 0:
            raise RuntimeError("Can't delete minimum from empty heap")
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._diving(0)

    def decrease_weight(self, i, delta):
        if delta < 0:
            raise ValueError("Can't increase weight")
        if i < 0 or i >= len(self.heap):
            raise ValueError("Index is out of range")
        self.heap[i] -= delta
        self._emersion(i)

    def delete(self, i):
        self.decrease_weight(i, float('Inf'))
        self.delete_min()

