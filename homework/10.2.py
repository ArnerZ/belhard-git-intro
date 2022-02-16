import pickle
class Square:
    def __init__(self, side):         
        self.side= side
    def Area(self):
        return self.side * self.side
s1 = Square(5)

serialized = pickle.dumps(s1)
deserialized = pickle.loads(serialized) 

print(deserialized.Area())