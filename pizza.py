import math

class Pizza:
    def __init__(self, diameter: float, crust_width: float = 1):
        self.diameter = diameter
        self.crust_width = crust_width

    def area(self) -> float:
        """Calculate the area of the whole pizza"""
        radius = self.diameter / 2
        return math.pi * radius ** 2

    def crust_area(self) -> float:
        """Calculate the estimated area of the crust for a pizza"""
        radius = self.diameter / 2
        whole_pizza_area = math.pi * radius ** 2
        middle_area = math.pi * (radius - self.crust_width) ** 2
        return whole_pizza_area - middle_area

    def middle_area(self) -> float:
        """Calculate the estimated middle area of a pizza"""
        radius = self.diameter / 2
        return math.pi * (radius - self.crust_width) ** 2
