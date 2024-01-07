
"""This module provides the LabelWidget class for merging multiple GIF images into a single GIF file.


# pip install PyQt5
# pip install Pillow

@category: UI, Utilities
"""


import os
from typing import Any
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel as label
from PIL import Image


current_movie_index: int = 0


class LabelWidget:
    """This class, LabelWidget, provides two methods:

    - set_gif: Sets a GIF image on a label by creating a QMovie object and starting it. 
    The GIF is aligned in the center of the label.

    - merge_gifs: Merges multiple GIF images into a single GIF file by opening each image using PIL library, saving them as frames, and then saving the frames as a single GIF file. The file path of the merged GIF is returned.
    @category: UI, Utilities
    """

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
