class NotSleeping:
    """
    The `NotSleeping` class represents an entity that is not sleeping.

    Attributes:
    name (str): The name of the not sleeping entity.
    value (int): The value associated with the not sleeping entity (default is 0).

    Methods:
    __init__(name: str, value: int = 0): Initializes a new `NotSleeping` object.
    add_sheep(): Increases the value associated with the not sleeping entity by 1.
    get_value(): Returns the current value associated with the not sleeping entity.
    __repr__(): Returns the name of the not sleeping entity as a string.
    """

    def __init__(self, name, value=0):
        """
        Initializes a new `NotSleeping` object.

        Parameters:
        name (str): The name of the not sleeping entity.
        value (int, optional): The value associated with the not sleeping entity (default is 0).
        """
        self.name = name
        self.__value = int(value)

    def add_sheep(self):
        """
        Increases the value associated with the not sleeping entity by 1.
        """
        self.__value += 1

    @property
    def get_value(self):
        """
        Returns the current value associated with the not sleeping entity.
        """
        return self.__value

    def __repr__(self):
        """
        Returns the name of the not sleeping entity as a string.
        """
        return self.name
