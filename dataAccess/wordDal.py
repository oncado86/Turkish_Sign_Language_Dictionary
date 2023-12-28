from dataAccess.sqliteDbHelper import SqliteDbHelper as db_helper
from entity.word import Word
from typing import Any


class WordDal(db_helper):
    def __init__(self) -> None:
        """
        Purpose: Construct
        Entity fields::
        id, ad, anlam, img, yapilis
        """
    # end default constructor

    def get(self, _entity_id: int) -> Word:
        """
        Retrieves a word from the database based on the provided entity ID.

        Parameters:
            _entity_id (int): The ID of the word to retrieve.

        Returns:
            Word: The word object containing the retrieved information.
        """
        query: str = "SELECT id, ad, anlam, img FROM kelime WHERE id = ?"
        word: Word = Word()

        with self.connect as cn:
            cr = cn.cursor()
            datas: tuple[int] = (_entity_id,)
            cr.execute(query, datas)
            values: Any = cr.fetchone()
            if values:
                (
                    word.id,
                    word.name,
                    word.info,
                    word.img,
                ) = values
            return word

    def get_id(self, _name: str) -> int:
        """
        Retrieves the id associated with a given name.

        Parameters:
            _name (str): The name to retrieve the id for.

        Returns:
            int: The id associated with the name. Returns 0 if no id is found.
        """
        _name = _name.lower()
        query: str = "SELECT id FROM kelime WHERE ad=?"
        datas: tuple[str] = (_name,)
        with self.connect as cn:
            im = cn.cursor()
            im.execute(query, datas)
            result = im.fetchone()
        return result[0] if result is not None else 0

    def get_all(self, _entity_name: str = "") -> list[Word]:
        """
        Retrieves a list of Word objects from the database.

        Args:
            _entity_name (str): The name of the Word to search for. Defaults to an empty string.

        Returns:
            list[Word]: A list of Word objects matching the search criteria.
        """
        _entity_name = _entity_name.lower()
        query: str = "SELECT * FROM kelime WHERE ad LIKE ? ORDER BY ad"
        datas: tuple[str] = ('%' + _entity_name + '%',)
        word_list: list[Word] = []
        with self.connect as cn:
            cr = cn.cursor()
            cr.execute(query, datas)
            values: list[Any] = cr.fetchall()

            for value in values:
                wrd: Word = Word()
                (wrd.id, wrd.name, wrd.info, wrd.img) = value
                word_list.append(wrd)

        return word_list
