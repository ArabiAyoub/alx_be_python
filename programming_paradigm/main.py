# main.py

import sys
from simple_calculator import SimpleCalculator

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <num1> <num2>")
        return

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    calc = SimpleCalculator()

    try:
        result = calc.divide(num1, num2)
        if result is None:
            raise ValueError("Cannot divide by zero.")
        print("Result: {}".format(result))
    except ValueError as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    main()