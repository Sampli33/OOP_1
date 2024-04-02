class Point:
    """
    The `Point` class represents a point in a 2D coordinate system.

    Attributes:
    x (int): The x-coordinate of the point.
    y (int): The y-coordinate of the point.

    Methods:
    __init__(coordinate: tuple): Initializes a new `Point` object with the provided coordinates.
    get_x(): Returns the x-coordinate of the point.
    get_y(): Returns the y-coordinate of the point.
    distance(other: Point): Calculates and returns the distance between this point and another point.
    sum(other: Point): Calculates and returns a new point representing the sum of this point and another point.
    __str__(): Returns a string representation of the point in the format "(x; y)".
    """

    def __init__(self, coordinate=None):
        """
        Initializes a new `Point` object with the provided coordinates.

        Parameters:
        coordinate (tuple, optional): A tuple containing the x and y coordinates of the point (default is None).
        """
        if coordinate:
            self.x = int(coordinate[0])
            self.y = int(coordinate[1])
        else:
            self.x = 0
            self.y = 0

    def get_x(self):
        """
        Returns the x-coordinate of the point.

        Returns:
        int: The x-coordinate of the point.
        """
        return self.x

    def get_y(self):
        """
        Returns the y-coordinate of the point.

        Returns:
        int: The y-coordinate of the point.
        """
        return self.y

    def distance(self, other):
        """
        Calculates and returns the distance between this point and another point.

        Parameters:
        other (Point): Another point to calculate the distance to.

        Returns:
        float: The distance between the two points.
        """
        dist = ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5
        return dist

    def sum(self, other):
        """
        Calculates and returns a new point representing the sum of this point and another point.

        Parameters:
        other (Point): Another point to sum with.

        Returns:
        Point: A new point representing the sum of the two points.
        """
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point((new_x, new_y))

    def __str__(self):
        """
        Returns a string representation of the point in the format "(x; y)".

        Returns:
        str: A string representation of the point.
        """
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return self.__str__()
