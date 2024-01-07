"""
This module contains the Managers class.

@category: Business, Manager
@see: WordManager
"""

from business.wordManager import WordManager


class Managers:
    """The Managers class has a default constructor that initializes an instance of the class.     
    It also has a property method word that returns the WordManager object. 
    The WordManager object is assigned to the __word_manager attribute of the Managers class.

    @category: Business, Manager
    @see: WordManager
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the class.

        Parameters:
            None

        Returns:
            None

        @category: Business, Manager
        @see: WordManager
        """
        self.__word_manager: WordManager = WordManager()

    @property
    def word(self) -> WordManager:
        """
        Get the WordManager object.

        Returns:
            WordManager: The WordManager object.
        """
        return self.__word_manager
