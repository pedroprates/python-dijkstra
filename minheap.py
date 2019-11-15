class MinHeap:
    """ Creating a Minimum Heap to hold values

        The time complexity for insertion and deletion are O(log N), which can hold an
        easy and fast way to hold a sorted array.
        
        As we are creating a Minimum Heap, the parent node will always be greater or equal to its child.
    """

    def __init__(self):
        self.heap = []
        
    def __len__(self):
        return len(self.heap)

    def __parent(self, i):
        return (i-1) // 2

    def __left(self, i):
        return (i * 2) + 1

    def __right(self, i):
        return (i * 2) + 2

    def __sort_heap(self):
        i = len(self.heap) - 1

        while (i != 0) and (self.heap[self.__parent(i)] > self.heap[i]):
            self.heap[self.__parent(i)], self.heap[i] = self.heap[i], self.heap[self.__parent(i)]

    def __heapify(self, i):
        l = self.__left(i)
        r = self.__right(i)
        smallest = i

        if (l < len(self.heap)) and (self.heap[l] < self.heap[i]):
            smallest = l
        if (r < len(self.heap)) and (self.heap[r] < self.heap[smallest]):
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.__heapify(smallest)

    def show(self):
        for n in self.heap:
            print(n)

    def insert(self, x):
        self.heap.append(x)
        self.__sort_heap()

    def remove(self):
        item = self.heap[0]
        self.__heapify(0)

        return item