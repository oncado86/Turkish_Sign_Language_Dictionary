"""The speechRecognition module provides a class for speech recognition using the Google Speech Recognition API.


@category: Utilities

# pip install SpeechRecognition
# pip install requests
"""
import threading
import speech_recognition as sr
import requests


class SpeechRecognition:
    """
    The SpeechRecognition class provides a method for speech recognition using the Google Speech Recognition API. 
    Here is a summary of each class method:

    - recognize_speech: Recognizes speech using the Google Speech Recognition API. 
    It returns a tuple with a boolean value indicating success or failure of speech recognition, and a string representing the recognized speech. 
    It can raise UnknownValueError if the speech cannot be understood, or RequestError if there is an error with the speech recognition request.

    - __is_connect_internet: Checks if the device is connected to the internet. 
    It returns a boolean value indicating whether the device is connected to the internet or not.

    @category: Utilities
    """

    def __init__(self) -> None:
        self.r = sr.Recognizer()
        self.text = None

    def recognize_speech(self) -> tuple[bool, str]:
        """
        Recognizes speech and returns a tuple indicating whether the speech was successfully recognized and the recognized speech text.

        Returns:
            tuple[bool, str]: A tuple containing a boolean value indicating whether the speech was successfully recognized and a string representing the recognized speech text.
        """

        if not self.__is_connect_internet():
            return False, "Lütfen internet bağlantınızı kontrol ediniz"

        self.text = None
        thread = threading.Thread(target=self.__listen)
        thread.start()
        thread.join(timeout=3.5)

        if thread.is_alive():
            thread.join(timeout=3)

        if self.text:
            return True, str(self.text)
        else:
            return False, "Ses anlaşılamadı veya zaman aşımı"

    def __listen(self) -> None:
        """
        Listens for audio input using the microphone and converts it to text.

        This method is used to listen for audio input from the microphone using the `sr.Microphone` class from the `speech_recognition` library. 
        It then uses the `recognize_google` method of the `sr.Recognizer` class to convert the audio to text.

        Parameters:
            None

        Return:
            None

        Raises:
            - sr.UnknownValueError: If the audio cannot be recognized as speech.
            - sr.RequestError: If there is an error making the speech recognition request.
        """

        try:
            with sr.Microphone() as source:
                audio = self.r.listen(source)

            self.text = self.r.recognize_google(
                audio, language="tr-TR")

        except (sr.UnknownValueError, sr.RequestError):
            self.text = None

    def __is_connect_internet(self) -> bool:
        """
        Check if the device is connected to the internet.

        Returns:
            bool: True if the device is connected to the internet, False otherwise.
        """
        try:
            response = requests.head("https://www.google.com", timeout=1)
            return response.ok
        except requests.exceptions.RequestException:
            return False
