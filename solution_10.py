class Segment:
    """
    The Segment class represents a line segment in a plane between two points.

    Attributes:
    a (Point): The starting point of the segment.
    b (Point): The ending point of the segment.
    one_intersection (bool): Indicates if the segment intersects with one of the coordinate axes.

    Methods:
    check_intersection(): Checks if the segment intersects with a coordinate axis.
    __str__(): Returns a string representation of the segment.
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.one_intersection = self.check_intersection()

    def check_intersection(self):
        """
        Checks if the segment intersects with a coordinate axis.

        Returns:
        bool: True if the segment intersects with one of the coordinate axes, otherwise False.
        """
        x_cor1 = self.a.x
        x_cor2 = self.b.x
        y_cor1 = self.a.y
        y_cor2 = self.b.y
        return ((x_cor1 * x_cor2 < 0 <= y_cor1 * y_cor2)
                or (x_cor1 * x_cor2 >= 0 > y_cor1 * y_cor2))

    def __str__(self):
        """
        Returns a string representation of the segment.

        Returns:
        str: A string representation of the segment in the format "(a; b)".
        """
        return f"({self.a}, {self.b})"


class CoordinateSystem:
    """
    The CoordinateSystem class represents a coordinate system on a plane.

    Attributes:
    segments (list): List of segments in the coordinate system.

    Methods:
    add_segment(segment): Adds a segment to the coordinate system.
    axis_intersection(): Determines the number of segments that intersect only one coordinate axis.
    __str__(): Returns a string representation of the coordinate system.
    """
    segments =[]

    def add_segment(segment):
        """
        Adds a segment to the coordinate system.

        Parameters:
        segment (Segment): The segment to be added.
        """
       CoordinateSystem.segments.append(segment)

    def axis_intersection():
        """
        Determines the number of segments that intersect only one coordinate axis.

        Returns:
        int: The number of segments that intersect only one coordinate axis.
        """
        counter = 0
        for elem in CoordinateSystem.segments:
            if elem.one_intersection:
                counter += 1
        return counter

    def __str__():
        """
        Returns a string representation of the coordinate system.

        Returns:
        str: A string representation of the coordinate system as a list of segments.
        """
        return ' '.join(str(elem) for elem in CoordinateSystem.segments)
