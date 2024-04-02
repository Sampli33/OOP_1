class TrafficLight:
    """
    The `TrafficLight` class represents a traffic light with three possible signals: 'зеленый', 'желтый', and 'красный'.

    Attributes:
    current_signal (str): The current signal of the traffic light, initialized to 'зеленый'.
    counter (int): A counter to keep track of the number of times `next_signal` has been called.

    Methods:
    __init__(): Initializes a new `TrafficLight` object with the current signal set to 'зеленый' and counter set to 0.
    next_signal(): Updates the current signal based on the counter and returns the new signal.
    __str__(): Returns a string representation of the current signal.
    __repr__(): Returns a string representation of the current signal, calling the __str__ method.
    """

    permissible_values = ['зеленый', 'желтый', 'красный']

    def __init__(self):
        """
        Initializes a new `TrafficLight` object with the current signal set to 'зеленый' and counter set to 0.
        """
        self.current_signal = 'зеленый'
        self.counter = 0

    def next_signal(self):
        """
        Updates the current signal based on the counter and returns the new signal.

        Returns:
        str: The new current signal after updating.
        """
        self.counter += 1
        if self.counter == 3:
            self.current_signal = 'желтый'
            self.counter = -1
        else:
            self.current_signal = TrafficLight.permissible_values[self.counter]

    def __str__(self):
        """
        Returns a string representation of the current signal.

        Returns:
        str: The string representation of the current signal.
        """
        return self.current_signal

    def __repr__(self):
        """
        Returns a string representation of the current signal, calling the __str__ method.

        Returns:
        str: The string representation of the current signal.
        """
        return self.__str__()
