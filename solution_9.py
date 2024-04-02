class StrandsDNA:
    """
    The `StrandsDNA` class represents a collection of DNA strands.

    Attributes:
    all_strands (list): A list to store all DNA strands added to the class.

    Methods:
    __init__(): Initializes an empty list to store DNA strands.
    add_strands(strands: str): Adds new DNA strands to the collection.
    get_max_strands(): Retrieves the longest DNA strands from the collection.
    __str__(): Returns a string representation of all DNA strands in the collection.
    """

    def __init__(self):
        """
        Initializes an empty list to store DNA strands.
        """
        self.all_strands = []

    def add_strands(self, strands):
        """
        Adds new DNA strands to the collection.

        Parameters:
        strands (str): A string containing DNA strands separated by spaces.
        """
        updating_list = strands.split()
        for elem in updating_list:
            self.all_strands.append(elem)

    def get_max_strands(self):
        """
        Retrieves the longest DNA strands from the collection.

        Returns:
        str: A string containing the longest DNA strands, sorted and separated by spaces.
        """
        longest_strand = max(map(len, self.all_strands))
        longest_list = [elem for elem in self.all_strands if len(elem) == longest_strand]
        return ' '.join(sorted(set(longest_list)))

    def __str__(self):
        """
        Returns a string representation of all DNA strands in the collection.

        Returns:
        str: A string containing all DNA strands in the collection, separated by spaces.
        """
        return ' '.join(elem for elem in self.all_strands)
