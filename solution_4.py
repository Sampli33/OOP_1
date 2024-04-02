class User:
    """
    The `User` class represents a user with various personal details.

    Attributes:
    __id (str): The unique identifier for the user.
    __nick_name (str): The nickname of the user.
    __firstname (str): The first name of the user.
    __last_name (str, optional): The last name of the user (default is None).
    __middle_name (str, optional): The middle name of the user (default is None).
    __gender (str, optional): The gender of the user (default is None).

    Methods:
    __init__(id: str, nick_name: str, first_name: str, last_name: str = None,
            middle_name: str = None, gender: str = None): Initializes a new User object.
    update(id: str = None, nick_name: str = None, first_name: str = None,
           last_name: str = None, middle_name: str = None, gender: str = None):
           Updates the user's details.
    __str__(): Returns a string representation of the user's details.
    __repr__(): Returns the unique identifier of the user.
    """

    def __init__(self, id, nick_name, first_name,
                 last_name=None, middle_name=None, gender=None):
        """
        Initializes a new `User` object with the provided details.

        Parameters:
        id (str): The unique identifier for the user.
        nick_name (str): The nickname of the user.
        first_name (str): The first name of the user.
        last_name (str, optional): The last name of the user (default is None).
        middle_name (str, optional): The middle name of the user (default is None).
        gender (str, optional): The gender of the user (default is None).
        """
        self.__id = id
        self.__nick_name = nick_name
        self.__firstname = first_name
        self.__last_name = last_name
        self.__middle_name = middle_name
        self.__gender = gender

    def update(self, id=None, nick_name=None, first_name=None,
               last_name=None, middle_name=None, gender=None):
        """
        Updates the user's details with the provided values.

        Parameters:
        id (str, optional): The new unique identifier for the user.
        nick_name (str, optional): The new nickname of the user.
        first_name (str, optional): The new first name of the user.
        last_name (str, optional): The new last name of the user.
        middle_name (str, optional): The new middle name of the user.
        gender (str, optional): The new gender of the user.
        """
        if id:
            self.__id = id
        if nick_name:
            self.__nick_name = nick_name
        if first_name:
            self.__firstname = first_name
        if last_name:
            self.__last_name = last_name
        if middle_name:
            self.__middle_name = middle_name
        if gender:
            self.__gender = gender

    def __str__(self):
        """
        Returns a string representation of the user's details.
        """
        output = f'ID: {self.__id} Nickname: {self.__nick_name} Name: '
        if self.__last_name:
            output += f'{self.__last_name} '
        output += f'{self.__firstname} '
        if self.__middle_name:
            output += f'{self.__middle_name} '
        if self.__gender:
            output += f'Gender: {self.__gender}'
        return output

    def __repr__(self):
        """
        Returns the unique identifier of the user.
        """
        return self.__id
