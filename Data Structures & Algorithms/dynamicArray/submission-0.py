class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0]*capacity
        self.capacity = capacity
        self.pos = 0


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.pos >= self.capacity:
            self.resize()
        
        self.arr[self.pos] = n
        self.pos += 1
        



    def popback(self) -> int:
        self.pos -= 1
        val = self.arr[self.pos]
        return val
 

    def resize(self) -> None:
        new_arr = [0 for _ in range(2*self.capacity)]
        for idx, elem in enumerate(self.arr):
            new_arr[idx] = elem
        self.arr = new_arr
        self.capacity *= 2


    def getSize(self) -> int:
        return self.pos
        
    
    def getCapacity(self) -> int:
        return self.capacity
