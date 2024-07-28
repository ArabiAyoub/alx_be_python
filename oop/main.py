from polymorphism_demo import Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        # Using .format() for string formatting compatible with older Python versions
        print("The area of the {} is: {}".format(shape.__class__.__name__, shape.area()))

if __name__ == "__main__":
    main()