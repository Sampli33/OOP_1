class NotSleeping:
    """
    The `NotSleeping` class represents an entity that is not sleeping and keeps track of sheep count.

    Attributes:
    name (str): The name of the not sleeping entity.
    __value (int): Private attribute to store the count of sheeps.

    Methods:
    __init__(name: str, value: int = 0): Initializes a new `NotSleeping` object.
    add_sheep(): Increases the count of sheeps by 1.
    get_count_sheeps(): Returns the current count of sheeps.
    lost(): Resets the count of sheeps to 0.
    __repr__(): Returns the name of the not sleeping entity as a string.
    """

    def __init__(self, name, value=0):
        """
        Initializes a new `NotSleeping` object.

        Parameters:
        name (str): The name of the not sleeping entity.
        value (int, optional): The initial count of sheeps (default is 0).
        """
        self.name = name
        self.__value = int(value)

    def add_sheep(self):
        """
        Increases the count of sheeps by 1.
        """
        self.__value += 1

    def get_count_sheeps(self):
        """
        Returns the current count of sheeps.
        """
        return self.__value

    def lost(self):
        """
        Resets the count of sheeps to 0.
        """
        self.__value = 0

    def __repr__(self):
        """
        Returns the name of the not sleeping entity as a string.
        """
        return self.name
