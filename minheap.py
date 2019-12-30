class MinHeap:
    """MinHeap implementation.

    Supported operations:
        is_empty():         Check whether the heap is empty or not.
        peek():             Return the current smallest heap element.
        insert(value):      Insert element into heap.
        pop():              Return smallest heap element and re-heapify heap.
        update_min(v, l):   Update comparison value of an element in heap.

    Usage:
        >>> h = MinHeap([10, 5, 2, 8, -1, 9])
        >>> h.insert(3)
        2
        >>> h
        [-1, 2, 3, 10, 8, 9, 5]
        >>> ordered = []
        >>> while not h.is_empty():
        ...     ordered.append(h.pop())
        >>> ordered
        [-1, 2, 3, 5, 8, 9, 10]

        >>> h = MinHeap([(10, 'J'), (5, 'E'), (2, 'B'), (8, 'H'), (9, 'I')])
        >>> h.insert((1, 'A'))
        0
        >>> h
        [(1, 'A'), (8, 'H'), (2, 'B'), (10, 'J'), (9, 'I'), (5, 'E')]
        >>> h.update_min(7, 'I')
        (7, 'I')
        >>> h
        [(1, 'A'), (7, 'I'), (2, 'B'), (10, 'J'), (8, 'H'), (5, 'E')]
        >>> ordered = []
        >>> while not h.is_empty():
        ...     ordered.append(h.pop())
        >>> ordered
        [(1, 'A'), (2, 'B'), (5, 'E'), (7, 'I'), (8, 'H'), (10, 'J')]

    Note:
        Elements can be tuples (value, label) which can be useful for tracking
        comparison values of records such as node names i.e. (3, 'A').

    Tests:
        python -m doctest minheap.py
        python test_minheap.py

    """

    def __init__(self, values=None):
        self.h = []
        # Track current index of labels.
        self.index = {}
        if values is not None:
            self._heapify(values)

    def __contains__(self, value):
        return value in self.h

    def __len__(self):
        return len(self.h)

    def __repr__(self):
        return repr(self.h)

    def _label(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            return value[1]
        return value

    def _val(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            return value[0]
        return value

    def _parent_index(self, index):
        return (index - 1) // 2

    def _left_child_index(self, index):
        return (index * 2) + 1

    def _right_child_index(self, index):
        return (index * 2) + 2

    def _heapify(self, values):
        self.h = []
        for v in values:
            self.insert(v)

    def _sift_up(self, i=None):
        if i is None:
            i = len(self.h) - 1

        p = self._parent_index(i)

        while p >= 0 and self._val(self.h[p]) > self._val(self.h[i]):
            self.h[i], self.h[p] = self.h[p], self.h[i]
            # Update label indices.
            self.index[self._label(self.h[i])], self.index[self._label(self.h[p])] = (
                self.index[self._label(self.h[p])],
                self.index[self._label(self.h[i])],
            )
            i = p
            p = self._parent_index(i)
        return i

    def _sift_down(self, i=None):
        if i is None:
            i = 0

        while True:
            l = self._left_child_index(i)
            r = self._right_child_index(i)

            smallest = i

            if l < len(self.h) and self._val(self.h[i]) > self._val(self.h[l]):
                smallest = l
            if r < len(self.h) and self._val(self.h[smallest]) > self._val(self.h[r]):
                smallest = r

            if smallest != i:
                self.h[i], self.h[smallest] = self.h[smallest], self.h[i]
                # Update label indices.
                self.index[self._label(self.h[i])], self.index[
                    self._label(self.h[smallest])
                ] = (
                    self.index[self._label(self.h[smallest])],
                    self.index[self._label(self.h[i])],
                )
                smallest = i
            else:
                return i

    def is_empty(self):
        return len(self.h) == 0

    def peek(self):
        return self.h[0] if len(self.h) > 0 else None

    def insert(self, value):
        label = self._label(value)

        if label in self.index:
            raise ValueError(f"Element with label '{label}' already exists.")

        self.h.append(value)

        # Add index.
        self.index[label] = len(self.h) - 1

        return self._sift_up()

    def update_min(self, value, label):
        if label not in self.index:
            raise ValueError(f"Invalid label '{label}'")
        i = self.index[label]
        current_val = self._val(self.h[i])
        if value < current_val:
            if isinstance(self.h[i], tuple) and len(self.h[i]) == 2:
                self.h[i] = (value, label)
            else:
                self.h[i] = value
        return self.h[self._sift_up(i)]

    def pop(self):
        if len(self.h) == 0:
            return None
        elif len(self.h) == 1:
            self.index = {}
            return self.h.pop()

        top_label = self._label(self.h[0])
        bottom_label = self._label(self.h[-1])

        del self.index[top_label]
        self.index[bottom_label] = 0

        value = self.h[0]
        self.h[0] = self.h.pop()
        self._sift_down()

        return value
