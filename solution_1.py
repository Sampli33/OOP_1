class Dog:
    """
    The `Dog` class represents a basic representation of a dog.

    Attributes:
    name (str): The name of the dog.

    Methods:
    __init__(name: str): Initializes the `Dog` object.
    say(): Prints the sound made by the dog.
    __repr__(): Returns the name of the dog as a string.
    """

    def __init__(self, name):
        """
        Initializes a new `Dog` object.

        Parameters:
        name (str): The name of the dog.
        """
        self.name = name

    def say(self):
        """
        Prints the sound made by the dog.
        """
        print('Woof!')

    def __repr__(self):
        """
        Returns the name of the dog as a string.
        """
        return self.name
