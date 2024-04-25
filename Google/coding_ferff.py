import bisect

class Example:
    def __init__(self):
        self.records = [[('a', 1), ('b', 2), ('c', 3)], [('d', 4), ('e', 5), ('f', 6)]]

    def find_index(self, index, snap_id):
        idx = bisect.bisect_right(self.records[index], snap_id, key=lambda x: x[1])
        return idx

ex = Example()
print(ex.find_index(0, ('b', 2)))  # Output: 2