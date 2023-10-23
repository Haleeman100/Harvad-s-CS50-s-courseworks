class Jar:
    # checks to see if capacity is not positive integer, raises an exception if that's rthe case
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity should be a non-negative integer")
        
        self.capacity = capacity
        
        ...

    def __str__(self):
        
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...