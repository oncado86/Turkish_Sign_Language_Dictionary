from PyQt5.QtWidgets import (
    QMessageBox as message_box,
)


class ShowMessageBox:
    """Kullanıcıyla etkileşime geçmek için mesaj kusutu iletişimleri ile ilgili operasyonların tutuluğu sınıf.
    
    @category: Utilities
    """

    def show_message(self, _title: str, _message: str) -> None:
        """Kullanıcıya bir iletişim kutusu gösterir.

        Args:
            _title (str): mesaj başlığı
            _message (str): mesajın içeriği
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
        """Kullanıcıyla etkileşimli iletişim kutusu gösterir.

        Args:
            _title (str): mesajın başlığı
            _message (str): mesajın içeriği

        Returns:
            _type_: soru içeriği
        """
        question = message_box.question(
            None,  # type: ignore
            _title,
            _message,
            message_box.Yes | message_box.No,  # type: ignore
            message_box.No,  # type: ignore
        )

        return question
