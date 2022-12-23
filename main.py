import argparse
import math

from pizza import Pizza


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("diameter", type=float, help="The diameter of the pizza by default in inches")
    parser.add_argument("--crust-width", type=float, default=1, help="The width of the crust by default in inches.")
    parser.add_argument("--units", type=str, default='inches', help="If we want to override the units from being in inches.")
    parser.add_argument("--cost", type=float, default=0, help="The cost of the pizza. If not zero then we will return the area per dollar.")
    args = parser.parse_args()
    pizza = Pizza(diameter=args.diameter, crust_width=args.crust_width)
    
    print(f"For a pizza with a diameter of {args.diameter} {args.units}")
    print(f"Area of whole pizza: {round(pizza.area(), 2)} square {args.units}")
    print(f"Estimated area of crust: {round(pizza.crust_area(), 2)} square {args.units}")
    print(f"Estimated area of middle: {round(pizza.middle_area(), 2)} square {args.units}")
    if args.cost != 0:
        print(f"Whole pizza:{round(pizza.area()/args.cost, 2)} square {args.units} per $ ")
        print(f"Estimated crust: {round(pizza.crust_area()/args.cost, 2)} square {args.units} per $")
        print(f"Estimated middle: {round(pizza.middle_area()/args.cost, 2)} square {args.units} per $")
if __name__ == "__main__":
    main()
