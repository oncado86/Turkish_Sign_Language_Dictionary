from business.wordManager import WordManager


class Managers:
    def __init__(self) -> None:
        """
        Initializes a new instance of the class.

        Parameters:
            None

        Returns:
            None
        """
        self.__word_manager: WordManager = WordManager()
    # end default constructor

    @property
    def word(self) -> WordManager:
        """
        Returns the WordManager object associated with this instance of the class.

        :return: The WordManager object.
        :rtype: WordManager
        """
        return self.__word_manager
