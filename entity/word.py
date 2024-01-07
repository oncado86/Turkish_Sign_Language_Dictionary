"""This module contains the Word class.

@category: Entities
"""


class Word:
    """Initializes the object with default values for the following attributes:

            - __id: int - The unique identifier of the object (default: 0).
            - __name: str - The name of the object (default: "").
            - __img_path: str - The path to the image associated with the object (default: "").
            - __howdo: str - A description of how to use the object (default: "").
            - __info: str - Additional information about the object (default: "").

        @category: Entities
    """

    def __init__(self) -> None:
        """
            Initializes the object with default values for the following attributes:

            - __id: int - The unique identifier of the object (default: 0).
            - __name: str - The name of the object (default: "").
            - __img_path: str - The path to the image associated with the object (default: "").
            - __howdo: str - A description of how to use the object (default: "").
            - __info: str - Additional information about the object (default: "").

        @category: Entities
        """
        self.__id: int = 0
        self.__name: str = ""
        self.__img_path: str = ""
        self.__info: str = ""

    @property
    def id(self) -> int:
        """Returns the value of the `id` property.

        Returns:
            int: An integer representing the id.
        """
        return self.__id

    @id.setter
    def id(self, _id: int) -> None:
        """
        Setter method for the `id` attribute.

        Parameters:
            _id (int): The new value for the `id` attribute.

        Returns:
            None
        """
        self.__id = _id

    @property
    def name(self) -> str:
        """
        Get the name property.

        Returns:
            str: The name property as a string.
        """
        return self.__name

    @name.setter
    def name(self, _name: str) -> None:
        """
        Setter method for the 'name' attribute.

        Parameters:
            _name (str): The new value for the 'name' attribute.

        Returns:
            None
        """
        self.__name = _name

    @property
    def img(self) -> str:
        """
        Returns the image path.

        Returns:
        str: A string representing the image path.
        """
        return self.__img_path

    @img.setter
    def img(self, _path: str) -> None:
        """
        Setter for the `img` attribute.

        Parameters:
            _path (str): The path to the image.

        Returns:
            None
        """
        self.__img_path = _path

    @property
    def info(self) -> str:
        """
        Returns the `info` property of the class.

        Returns:
        str: The value of the `info` property as a string.
        """
        return self.__info

    @info.setter
    def info(self, _info: str) -> None:
        """
        Set the value of the `info` attribute.

        Parameters:
            _info (str): The new value for the `info` attribute.

        Returns:
            None
        """
        self.__info = _info
