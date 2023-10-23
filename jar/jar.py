class Jar:
    # checks to see if capacity is not positive integer, raises an exception if that's rthe case
    def __init__(self, capacity = 12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity should be a non-negative integer")     
        self._capacity = capacity
        self._size = 0      
        

    def __str__(self):
        # returns a string of cookies in the jar
        return "🍪" * self._size       
        ...

    def deposit(self, n):
        # deposit's cookies to jar
        if  self.size + n > self.capacity:
            raise ValueError("Number of cookies should not be higher than that of capacity")
        
        self._size += n
        
        ...

    def withdraw(self, n):
        # withdraw cookies from jar
        if n > self.size:
            raise ValueError("Number of cookies to be withdrawn should not be greater than Jar size")   
             
        self._size -= n
        
        ...

    @property
    def capacity(self):
        return self._capacity
        

    @property
    def size(self):
        return self._size
        
        
def main():
    jar = Jar(5)
    jar.deposit(3)
    print(jar.size)
    print(jar.capacity)
    print(jar)
    
        
if __name__ == "__main__":
    main()