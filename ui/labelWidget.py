# pip install PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel as label
from PIL import Image
from typing import Any

import os


current_movie_index: int = 0


class LabelWidget:

    def __init__(self) -> None:
        """
        Purpose: 
        """

    # end default constructor

    def set_gif(self, _label: label, _img_path: str) -> None:
        """
        Set a GIF on a label.

        Parameters:
            _label (label): The label on which to set the GIF.
            _img_path (str): The path to the GIF image.

        Returns:
            None
        """
        movie = QMovie(_img_path)
        _label.setMovie(movie)
        movie.start()
        _label.setAlignment(Qt.AlignCenter)  # type: ignore

    def merge_gifs(self, _img_paths: list[str]) -> str:
        """
        Merge multiple GIFs into a single GIF file.

        Args:
            _img_paths (list[str]): A list of file paths of the GIFs to be merged.

        Returns:
            str: The file path of the merged GIF.

        """
        merged_gif: str = os.path.join(".", "tmp", "merged_gif.gif")
        frames: list[Any] = [Image.open(gif) for gif in _img_paths]
        frames[0].save(merged_gif, save_all=True,
                       append_images=frames[1:], loop=0)
        return merged_gif
