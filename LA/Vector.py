class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    def __add__(self, other):
        assert len(self) == len(other), \
            "Error in adding. Length of vectors must be same"
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        assert len(self) == len(other), \
            "Error in adding. Length of vectors must be same"
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        return self * k

    def __pos__(self):
        return 1*self

    def __neg__(self):
        return -1*self

    def __iter__(self):
        return self._values.__iter__()

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "Vector({})".format(self._values)