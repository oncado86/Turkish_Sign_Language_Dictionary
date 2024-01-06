""" In order for the application to run without errors, the following libraries must be installed.
    - PyQt5
    - SpeechRecognition
    - requests
    - Pillow
        
    pip install PyQt5
    pip install SpeechRecognition
    pip install requests
"""
import os
from PyQt5.QtWidgets import (
    QMainWindow as main_window,
    QApplication as application,
)


from core.appManager import AppManager
from entity.word import Word
from ui.tids_ui import Ui_MainWindow as ui_main_window


class TIDSApp(ui_main_window, main_window):
    """Türkçe İşaret Dili Sözlüğü

    Args:
        ui_main_window (ui_main_window): UI
        main_window (main_window): QT framework
    """
    ##################################################################
    # * --------------------------------------------------------------
    # * * * * * * * * * * * *  CONSTRUCTOR  * * * * * * * * * * * * *
    # * --------------------------------------------------------------

    def __init__(self) -> None:
        """
        Purpose: Constructor
        """
        super().__init__()
        self.apman: AppManager = AppManager()
        self.init_ui()

        self.lbl_clear_img()
    # end default constructor

    def init_ui(self) -> None:
        """
        Initializes the user interface by creating an instance of 
        the `ui_main_window` class and setting up the UI. 

        Parameters:
            self (object): The current instance of the class.

        Returns:
            None
        """
        self.ui: ui_main_window = ui_main_window()
        self.ui.setupUi(self)  # type:ignore

        self.fill_words()
        self.line_edit_funcs()
        self.list_widget_funs()
        self.button_funcs()

        self.show()

    ##################################################################
    # * --------------------------------------------------------------
    # * * * * * * * * * * * * *  UI FONC  * * * * * * * * * * * * * *
    # * --------------------------------------------------------------

    ##################################################################
    # * --------------------------------------------------------------
    # * BUTTON FUNCTIONS
    # * --------------------------------------------------------------
    def button_funcs(self) -> None:
        """
        Connect the appropriate functions to the buttons in the user interface.
        This function does not take any parameters and does not return anything.
        """
        self.ui.btn_cevirici_cevir.clicked.connect(
            self.translate_sentence
        )

        self.ui.btn_cevirici_konus.clicked.connect(
            self.translate_to_voice
        )

    def translate_to_voice(self) -> None:
        """
        Translates the text in the `txt_cevirici_cumle` field to voice.

        Returns:
            None
        """
        self.ui.statusbar.showMessage("Dinliyorum...")
        txt_sentence = self.ui.txt_cevirici_cumle

        state, text = self.apman.speech_recognition.recognize_speech()
        if state:
            self.ui.statusbar.clearMessage()
            txt_sentence.clear()
            txt_sentence.setPlainText(text)
            self.translate_sentence()
        else:
            self.ui.statusbar.showMessage(text, 3000)

    def sentece_spliter(self, sentence: str) -> list[str]:
        """
        Split a sentence into individual words, including idioms, and return a list of word names.

        Args:
            sentence (str): The sentence to be split.

        Returns:
            list[str]: A list of word names.

        """
        sentence = sentence.lower()
        word_names: list[str] = []
        words_in_sentence: list[str] = self.apman.managers.word.to_clear_spesials(
            sentence).split()

        idiom_words: list[Word] = [
            word
            for word in self.apman.managers.word.get_all()
            if " " in word.name]

        sentece_fix: str = " ".join(words_in_sentence)
        index: int = 0
        while index < len(words_in_sentence):
            word: str = words_in_sentence[index]
            idiom_added = False
            for idiom in idiom_words:
                if idiom.name in sentece_fix:
                    idiom_name_split: list[str] = idiom.name.split()
                    idiom_name_letter_count: int = len(idiom_name_split)
                    if words_in_sentence[index:index+idiom_name_letter_count] == idiom_name_split:
                        word_names.append(idiom.name)
                        idiom_added = True
                        index += idiom_name_letter_count
                        break
            if not idiom_added:
                word_names.append(word)
                index += 1
        return word_names

    def translate_sentence(self) -> None:
        """
        Translates a given sentence into images.

        Parameters:
            None.

        Return:
            None.
        """
        txt_sentence = self.ui.txt_cevirici_cumle
        lbl_img = self.ui.lbl_cevirici_cumle_img

        words: list[str] = self.sentece_spliter(txt_sentence.toPlainText())
        words_list: list[str] = []
        undefined = False

        for word in words:
            if not self.apman.managers.word.is_there(word):
                undefined = True
                words_list.extend(word)
            else:
                words_list.append(word)

        if undefined:
            self.apman.message_box.show_message(
                "Tanımlı Olmayan Kelime(ler) Algılandı",
                "Tanımlanmamış kelime(ler) kullanıldı, bu kelime(ler) harf harf gösterilecektir."
            )

        path_list: list[str] = [
            self.apman.managers.word.get(
                self.apman.managers.word.get_id(word)).img
            for word in words_list
            if self.apman.managers.word.is_safe(word)
        ]

        if words_list:
            gif_path: str = self.apman.label_widget.merge_gifs(path_list)
            self.apman.label_widget.set_gif(lbl_img, gif_path)
        else:
            self.lbl_clear_img()

    ##################################################################
    # * --------------------------------------------------------------
    # * LIST WIDGET FUNCTIONS
    # * --------------------------------------------------------------
    def list_widget_funs(self) -> None:
        """
        List all the available widget functions.
        This function does not take any parameters.
        It does not return anything.
        """
        self.changed_current_list_item()

    def changed_current_list_item(self) -> None:
        """
        Connects the currentRowChanged signal of the lw_ogretici_kelime_listesi QListWidget 
        to the lw_tutarial_page_word_list_item_changed slot of the class. This ensures that 
        the slot is called whenever the current row of the QListWidget is changed.

        Parameters:
            self (ClassName): An instance of the class.

        Returns:
            None
        """
        self.ui.lw_ogretici_kelime_listesi.currentRowChanged.connect(
            self.lw_tutarial_page_word_list_item_changed
        )

    def lw_tutarial_page_word_list_item_changed(self) -> None:
        """
        Handle the event when an item is changed in the lw_tutarial_page_word_list.

        This function is called when an item in the lw_tutarial_page_word_list is changed.
        It retrieves the selected item and its corresponding information from the UI elements. 
        If a valid item is selected, it retrieves the Word object associated with the selected item from the word manager. 
        It then updates the UI elements with the retrieved information. 
        If no valid item is selected, it clears the UI elements.

        Parameters:
            self (MainWindow): The instance of the MainWindow class.

        Returns:
            None
        """
        lbl_img = self.ui.lbl_ogretici_secili_kelime_img
        txt_info = self.ui.txt_ogretici_secili_kelime_anlam
        lw_words = self.ui.lw_ogretici_kelime_listesi
        current_selected_row: int = lw_words.currentRow()
        selected_item = lw_words.currentItem()

        if current_selected_row >= 0 and selected_item is not None:
            current_name: str = selected_item.text()
            word: Word = self.apman.managers.word.get(
                self.apman.managers.word.get_id(
                    current_name
                )
            )

            self.lbl_clear_img()
            txt_info.clear()
            self.apman.label_widget.set_gif(lbl_img, word.img)
            txt_info.setPlainText(word.info)
        else:
            self.lbl_clear_img()
            txt_info.clear()

    ##################################################################
    # * --------------------------------------------------------------
    # * LINE EDIT FUNCTIONS
    # * --------------------------------------------------------------
    def line_edit_funcs(self) -> None:
        """
        Initializes the line edit functions.

        This function connects the textChanged signals of the line edit widgets
        to their corresponding slots in the UI.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        # -->> WORD SEARCH
        self.ui.le_ogretici_kelime_ara.textChanged.connect(
            self.txt_tutarial_page_word_search_changed
        )

        # -->> WORD TRANSLATE
        self.ui.txt_cevirici_cumle.textChanged.connect(
            self.txt_translate_page_words_translate_changed
        )

    def txt_translate_page_words_translate_changed(self) -> None:
        """
        Translates the words in the page when the translate button is clicked.

        :param self: The current instance of the class.

        :return: None
        """
        txt_words = self.ui.txt_cevirici_cumle
        btn_translate = self.ui.btn_cevirici_cevir
        btn_translate.setEnabled(bool(txt_words.toPlainText()))

    def txt_tutarial_page_word_search_changed(self) -> None:
        """
        A function that handles the event when the word search in the tutorial page is changed.

        This function is triggered when the user changes the search term in the tutorial page. 
        It first fills the word list with the search results by calling the `fill_words()` method. 
        Then, it resets the current row in the list widget `lw_ogretici_kelime_listesi` by setting it to -1. 
        If any exception occurs during the execution of this function, it is caught and ignored.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        try:
            self.fill_words()
            self.ui.lw_ogretici_kelime_listesi.setCurrentRow(-1)
        except ValueError:
            pass

    ##################################################################
    # * --------------------------------------------------------------
    # * LABEL FUNCTIONS
    # * --------------------------------------------------------------
    def lbl_clear_img(self) -> None:
        """
        Clears the image labels by setting them to a default image.

        :return: None
        """
        path: str = os.path.join(".", "data", "img", "loop.gif")
        lbl_ogretici_secili_kelime_img = self.ui.lbl_ogretici_secili_kelime_img
        lbl_cevirici_cumle_img = self.ui.lbl_cevirici_cumle_img
        self.apman.label_widget.set_gif(lbl_ogretici_secili_kelime_img, path)
        self.apman.label_widget.set_gif(lbl_cevirici_cumle_img, path)

    ##################################################################
    # * --------------------------------------------------------------
    # * GET
    # * --------------------------------------------------------------
    def get_word_list(self) -> list[Word]:
        """
        Retrieves a list of Word objects based on a search text.

        :return: A list of Word objects.
        """
        search_text: str = self.ui.le_ogretici_kelime_ara.text().lower()
        return self.apman.managers.word.get_all(search_text)

    ##################################################################
    # * --------------------------------------------------------------
    # * FILL
    # * --------------------------------------------------------------
    # WORD FILL FUNCTION
    def fill_words(self) -> None:
        """
        Fills the word list.

        :param self: The instance of the class.
        :return: None
        """
        self.fill_word_list()

    # -->> LIST WIDGET
    # WORD
    def fill_word_list(self) -> None:
        """
        Fills the word list in the user interface with safe words.

        Parameters:
            None

        Returns:
            None
        """
        lw_word = self.ui.lw_ogretici_kelime_listesi
        word_list: list[Word] = self.get_word_list()
        safe_word_list: list[str] = []

        for word in word_list:
            if self.apman.managers.word.is_safe(word.name):
                safe_word_list.append(word.name.title())

        lw_word.clear()
        lw_word.addItems(safe_word_list)
        self.ui.statusbar.showMessage(
            f"{len(safe_word_list)} adet kelime bulundu.", 3000)


if __name__ == "__main__":
    import sys
    app = application([])
    win = TIDSApp()
    win.show()
    sys.exit(app.exec_())
