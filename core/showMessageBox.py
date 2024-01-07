"""This module provides a class named ShowMessageBox for interacting with the user through message box dialogs.
Here's what each class method does:

- show_message(_title: str, _message: str) -> None: Displays a critical message box with a specified title and message.

- show_question(_title: str, _message: str) -> int: Shows a question dialog with the given title and message and returns the user's response as an integer. 
The value 16384 represents "Yes" and 65536 represents "No".

@category: Utilities

# pip install PyQt5
"""

from PyQt5.QtWidgets import (
    QMessageBox as message_box,
)


class ShowMessageBox:
    """
    This class ShowMessageBox is used for interacting with the user through message box dialogs. 
    Here's what each class method does:

    - show_message(_title: str, _message: str) -> None: Displays a critical message box with a specified title and message.

    - show_question(_title: str, _message: str) -> int: Shows a question dialog with the given title and message and returns the user's response as an integer. 
    The value 16384 represents "Yes" and 65536 represents "No".

    @category: Utilities
    """

    def show_message(self, _title: str, _message: str) -> None:
        """
        Displays a critical message box with a specified title and message.

        Args:
            _title (str): The title of the message box.
            _message (str): The message to be displayed.

        Returns:
            None: This function does not return anything.

        @category: Utilities
        """
        mb = message_box()
        mb.setIcon(mb.Critical)  # type: ignore
        mb.setWindowTitle(_title)
        font = mb.font()
        font.setBold(True)
        font.setPointSize(13)
        mb.setFont(font)
        mb.setText(_message)
        mb.exec()

    def show_question(self, _title: str, _message: str):
        """
        Show a question dialog with the given title and message.

        Args:
            _title (str): The title of the question dialog.
            _message (str): The message of the question dialog.

        Returns:
            int: The integer value representing the user's response. 
                 16384 for Yes, 65536 for No.
        """
        question = message_box.question(
            None,  # type: ignore
            _title,
            _message,
            message_box.Yes | message_box.No,  # type: ignore
            message_box.No,  # type: ignore
        )

        return question
