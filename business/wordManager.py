"""The wordManager module contains the WordManager class, which manages Word objects and interacts with a WordDal object. 
Here's a summary of each class method:

__init__: Initializes the object and sets the __wdal attribute to an instance of WordDal.
get: Retrieves a Word object by its entity ID.
get_id: Retrieves the ID for a given name.
get_all: Retrieves all instances of a specified entity.
is_there: Checks if a specified entity exists in the system.
is_safe: Checks if a given string is safe.
to_clear_spesials: Removes special characters from a string.

@category: Business, Manager
@see: Word, WordDal
"""

import re
from dataAccess.wordDal import WordDal, Word


class WordManager():
    """The WordManager class manages Word objects and interacts with a WordDal object. 
    Here's a summary of each class method:

    __init__: Initializes the object and sets the __wdal attribute to an instance of WordDal.
    get: Retrieves a Word object by its entity ID.
    get_id: Retrieves the ID for a given name.
    get_all: Retrieves all instances of a specified entity.
    is_there: Checks if a specified entity exists in the system.
    is_safe: Checks if a given string is safe.
    to_clear_spesials: Removes special characters from a string.

    @category: Business, Manager
    @see: Word, WordDal
    """

    def __init__(self) -> None:
        """
        Initializes the object.

        Parameters:
            None

        Returns:
            None
            
        @category: Business, Manager
        @see: Word, WordDal
        """
        self.__wdal = WordDal()

    def get(self, _entity_id: int) -> Word:
        """
        Get a Word object by its entity ID.

        Parameters:
            _entity_id (int): The entity ID of the Word object to retrieve.

        Returns:
            Word: The Word object with the given entity ID.
        """
        return self.__wdal.get(_entity_id)

    def get_id(self, _name: str) -> int:
        """
        Get the ID for a given name.

        Args:
            _name (str): The name for which to retrieve the ID.

        Returns:
            int: The ID corresponding to the given name.
        """
        return self.__wdal.get_id(_name)

    def get_all(self, _entity_name: str = "") -> list[Word]:
        """
        Retrieves all instances of the specified entity.

        Args:
            _entity_name (str): The name of the entity to retrieve instances of. 
            Defaults to an empty string.

        Returns:
            list[Word]: A list of Word objects representing the instances of the specified entity.
        """
        return self.__wdal.get_all(_entity_name)

    def is_there(self, entity_name: str = "") -> bool:
        """
        Check if the specified entity exists in the system.

        Parameters:
            entity_name (str): The name of the entity to check. Defaults to an empty string.

        Returns:
            bool: True if the entity exists, False otherwise.
        """
        return self.get_id(entity_name) > 0

    def is_safe(self, _str: str) -> bool:
        """
        Check if a given string is safe.

        Args:
            _str (str): The string to be checked.

        Returns:
            bool: True if the string is safe, False otherwise.
        """
        if re.match(r"^[\w\s]*$", _str):
            return True
        return False

    def to_clear_spesials(self, _str: str) -> str:
        """
        Remove special characters from a string.

        Args:
            _str (str): The input string.

        Returns:
            str: The modified string after removing special characters.
        """
        return re.sub(r"[^\w\s]", "", _str)
