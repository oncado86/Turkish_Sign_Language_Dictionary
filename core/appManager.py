"""
    Initializes the object by creating instances of 
    the Managers, LabelWidget, ShowMessageBox, and SpeechRecognition classes.
    
    @category: Manager, Business
    @see: LabelWidget, Managers, ShowMessageBox, SpeechRecognition
"""

from business.managers import Managers
from ui.labelWidget import LabelWidget
from core.showMessageBox import ShowMessageBox
from core.speechRecognition import SpeechRecognition


class AppManager:
    """
        Initializes the object by creating instances of 
        the Managers, LabelWidget, ShowMessageBox, and SpeechRecognition classes.
        
        @category: Manager, Business
        @see: LabelWidget, Managers, ShowMessageBox, SpeechRecognition
    """

    def __init__(self) -> None:
        """
        Initializes the object by creating instances of 
        the Managers, LabelWidget, ShowMessageBox, and SpeechRecognition classes.
        
        @category: Manager, Business
        @see: LabelWidget, Managers, ShowMessageBox, SpeechRecognition
        """
        self.__managers: Managers = Managers()
        self.__label_widget: LabelWidget = LabelWidget()
        self.__mb: ShowMessageBox = ShowMessageBox()
        self.__sp = SpeechRecognition()

    @property
    def managers(self) -> Managers:
        """
        Get the `Managers` object.

        Returns:
            Managers: The `Managers` object.
        """
        return self.__managers

    @property
    def label_widget(self) -> LabelWidget:
        """
        Get the label widget.

        Returns:
            LabelWidget: The label widget.
        """
        return self.__label_widget

    @property
    def message_box(self) -> ShowMessageBox:
        """
        Getter method for the `message_box` property.

        Returns:
            ShowMessageBox: The value of the `message_box` property.
        """
        return self.__mb

    @property
    def speech_recognition(self) -> SpeechRecognition:
        """Returns the speech recognition object.

        Returns:
            SpeechRecognition: The speech recognition object.
        """
        return self.__sp
