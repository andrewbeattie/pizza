import math
import pytest

from pizza import Pizza

class TestPizza:
    def test_area(self):
        """
        Calculate area of a pizza for 12 and 16 inches
        """
        pizza = Pizza(diameter=12)
        assert math.isclose(pizza.area(), 113.09733552923254, rel_tol=1e-9)

        pizza = Pizza(diameter=16)
        assert math.isclose(pizza.area(), 201.06192982974676, rel_tol=1e-9)

    def test_crust_area(self):
        """
        Estimating the crust area of a pizza for 12 and 16 inches 
        with a 1 and 1.5 inch crust width repsectively
        """
        pizza = Pizza(diameter=12, crust_width=1)
        assert math.isclose(pizza.crust_area(), 34.55751918948772, rel_tol=1e-9)

        pizza = Pizza(diameter=16, crust_width=1.5)
        assert math.isclose(pizza.crust_area(), 68.329640215578, rel_tol=1e-9)

    def test_middle_area(self):
        """
        Estiate the middle area of a pizza for 12 and 16 inches 
        with a 1 and 1.5 inch crust width respectively
        """
        # Test a pizza with a 12-inch diameter and a 1-inch crust width
        pizza = Pizza(diameter=12, crust_width=1)
        assert math.isclose(pizza.middle_area(), 78.53981633974483, rel_tol=1e-9)

        # Test a pizza with a 16-inch diameter and a 1.5-inch crust width
        pizza = Pizza(diameter=16, crust_width=1.5)
        assert math.isclose(pizza.middle_area(), 132.73228961416876, rel_tol=1e-9)
