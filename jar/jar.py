class Jar:
    # checks to see if capacity is not positive integer, raises an exception if that's rthe case
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity should be a non-negative integer")
        
        self.capacity = capacity
        self.size = size
        
        ...

    def __str__(self):
        # returns a string of cookies in the jar
        return "🍪" * self.size       
        ...

    def deposit(self, n):
        # deposit's cookies to jar
        if n + self.size > self.capacity:
            raise ValueError("Number of cookies should not be higher than that of capacity")
        
        self.size += n
        
        ...

    def withdraw(self, n):
        # withdraw cookies from jar
        if n > self.size:
            raise ValueError("Number of cookies to be withdrawn should not be greater than Jar size")   
             
        self.size -= n
        
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...