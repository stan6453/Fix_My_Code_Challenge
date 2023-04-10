#!/usr/bin/python3
"""
Square module. contains square objects and methods.
"""


class square():
    """
    square class (blueprint for square objects).
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        initialize the square.
        """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.width = args[0]
            self.height = args[1]

    def area_of_my_square(self):
        """
        Area of the square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        perimeter = 2L+2W where L=length and W=Width.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        string representation of the square.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
