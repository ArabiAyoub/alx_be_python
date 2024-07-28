class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not require access to class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Accesses and prints a class attribute before performing the multiplication.
        """
        print("Calculation type: {}".format(cls.calculation_type))
        return a * b