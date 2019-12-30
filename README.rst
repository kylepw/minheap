=======
minheap
=======
Min-heap implementation in Python. Min-heap is a complete binary tree data
structure that allows constant time retrieval of the minimum element in
the tree. Insertions/deletions operate in O(log n).

Operations
----------
* **is_empty()**:         Check whether the heap is empty or not.
* **peek()**:             Return the current smallest heap element.
* **insert(element)**:      Insert element into heap.
* **pop()**:              Return smallest heap element and re-heapify heap.
* **update_min(value, label)**:     Update comparison value of an element in heap.

Usage
-----
::

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

Tests
-----
::

    $ python -m doctest minheap.py && python test_minheap.py

License
-------
`MIT License <https://github.com/kylepw/minheap/blob/master/LICENSE>`_
