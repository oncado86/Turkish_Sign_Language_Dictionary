"""The speechRecognition module provides a class for speech recognition using the Google Speech Recognition API.


@category: Utilities

# pip install SpeechRecognition
# pip install requests
"""
import speech_recognition as sr  # type: ignore
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

    def recognize_speech(self) -> tuple[bool, str]:
        """
        Recognizes speech using the Google Speech Recognition API.

        Returns:
            A tuple containing a boolean value indicating success or failure of speech recognition,
            and a string representing the recognized speech.

        Raises:
            UnknownValueError: If the speech cannot be understood.
            RequestError: If there is an error with the speech recognition request.


        @category: Utilities
        """
        r = sr.Recognizer()

        if not self.__is_connect_internet():
            return False, "Lütfen internet bağlantınızı kontrol ediniz"

        with sr.Microphone() as source:
            print("Dinliyorum...")
            audio = r.listen(source)  # type: ignore

        try:
            text: str = r.recognize_google(
                audio, language="tr-TR")  # type: ignore
            print("Metin:", text)  # type: ignore
            return True, text
        except sr.UnknownValueError:
            print("Ses anlaşılamadı")
            return False, "Ses anlaşılmadı"
        except sr.RequestError as e:
            print("Hata:", e)
            return False, f"Hata: {e}"

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
