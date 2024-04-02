class Game:
    """
    The `Game` class represents a simple game between two commands, keeping track of their scores.

    Attributes:
    __command1_name (str): The name of the first command.
    __command2_name (str): The name of the second command.
    __score1 (int): The score of the first command.
    __score2 (int): The score of the second command.

    Methods:
    __init__(kwarg: dict): Initializes a new `Game` object with the provided commands and initial scores.
    ball_thrown(command: int, point: int): Updates the score of the specified command by the given points.
    get_score(): Returns the current scores of both commands.
    get_winner(): Determines and returns the winner of the game based on the scores.
    __str__(): Returns a string representation of the game with commands and scores.
    __repr__(): Returns a tuple containing the scores of both commands.
    """

    def __init__(self, kwarg):
        """
        Initializes a new `Game` object with the provided commands and initial scores.

        Parameters:
        kwarg (dict): A dictionary containing 'command1' and 'command2' keys with command names.
        """
        self.__command1_name = kwarg['command1']
        self.__command2_name = kwarg['command2']
        self.__score1 = 0
        self.__score2 = 0

    def ball_thrown(self, command, point):
        """
        Updates the score of the specified command by the given points.

        Parameters:
        command (int): The command (1 or 2) whose score needs to be updated.
        point (int): The points to be added to the command's score.
        """
        if command == 1:
            self.__score1 += point
        if command == 2:
            self.__score2 += point

    def get_score(self):
        """
        Returns the current scores of both commands.

        Returns:
        tuple: A tuple containing the scores of both commands.
        """
        return self.__score1, self.__score2

    def get_winner(self):
        """
        Determines and returns the winner of the game based on the scores.

        Returns:
        str: The name of the winning command or 'Ничья' if it's a tie.
        """
        if self.__score1 > self.__score2:
            return self.__command1_name
        elif self.__score1 < self.__score2:
            return self.__command2_name
        else:
            return 'Ничья'

    def __str__(self):
        """
        Returns a string representation of the game with commands and scores.

        Returns:
        str: A string containing the names of the commands and their scores.
        """
        return (f'{self.__command1_name}: {self.__score1},'
                f' {self.__command2_name}: {self.__score2}')

    def __repr__(self):
        """
        Returns a tuple containing the scores of both commands.

        Returns:
        tuple: A tuple containing the scores of both commands.
        """
        return self.__score1, self.__score2
