from business.managers import Managers
from ui.labelWidget import LabelWidget
from core.showMessageBox import ShowMessageBox
from core.speechRecognition import SpeechRecognition # type: ignore


class AppManager:
    """
        Initializes the object by creating instances of the Managers, LabelWidget, ShowMessageBox, and SpeechRecognition classes.
    """
    def __init__(self) -> None:
        """
        Initializes the object by creating instances of the Managers, LabelWidget, ShowMessageBox, and SpeechRecognition classes.
        """
        self.__managers: Managers = Managers()
        self.__label_widget: LabelWidget = LabelWidget()
        self.__mb: ShowMessageBox = ShowMessageBox()
        self.__sp = SpeechRecognition()
    # end default constructor

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
        Returns the label widget property.

        :return: The LabelWidget object.
        :rtype: LabelWidget
        """
        return self.__label_widget

    @property
    def message_box(self) -> ShowMessageBox:
        """
        Retrieves the `ShowMessageBox` instance associated with the `message_box` property.

        :return: The `ShowMessageBox` instance.
        :rtype: ShowMessageBox
        """
        return self.__mb

    @property
    def speech_recognition(self) -> SpeechRecognition:
        """
        Returns the SpeechRecognition object associated with this instance.

        :return: The SpeechRecognition object.
        :rtype: SpeechRecognition
        """
        return self.__sp
