class Polygon:
    def __init__(self, sides):
        self.sides = sides
    def abc(self):
        print(self.sides+1)

class Triangle(Polygon):
    # imp
    def __init__(self, sides):
        super().__init__(self)
        self.sides = sides    
    

class Square(Polygon):
    # imp
    def __init__(self, sides):
        super().__init__(self)
        self.sides = sides

class PolygonFactory:
    @staticmethod
    def get_polygon(sides):
        if(sides == 3):
            return Triangle(sides)
        if(sides == 4):
            return Square(sides)
        raise ValueError("no shit")

t = PolygonFactory.get_polygon(3)
t = PolygonFactory.get_polygon(4)
