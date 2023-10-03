from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from ui.src.Ui_decryption_window import *
from ui.src.window_utils import error_warning

class DecryptionWindow(QMainWindow):
    change_window_signal = pyqtSignal()
    crack_signal = pyqtSignal(dict)

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_DecryptionWindow()
        self.ui.setupUi(self)

    def init(self) -> None:
        self.ui.crack_button.clicked.connect(self.crack)
        self.ui.encryption_button.clicked.connect(self.change_window)
        self.ui.char_button.toggled.connect(self.encrypted_text_setting)

    def encrypted_text_setting(self):
        choose_mode = self.ui.choose_mode_group.checkedId()
        if choose_mode == -3:
            binary_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[01]+"), self.ui.encrypted_text_input)
            self.ui.encrypted_text_input.setValidator(binary_validator)
        else:
            self.ui.encrypted_text_input.setValidator(None)

    def crack(self) -> None:
        choose_mode = self.ui.choose_mode_group.checkedId()
        if choose_mode == -2:
            mode = "unicode"
        elif choose_mode == -3:
            mode = "binary"
        else:
            error_warning("Please choose input model !  ")
            return

        encrypted_text = self.ui.encrypted_text_input.text()
        if encrypted_text == "":
            error_warning("Please enter encrypted text !  ")
            return


        data_dict = {
            "mode": mode,
            "encrypted text": encrypted_text
        }

        self.crack_signal.emit()

    def change_window(self):
        self.change_window_signal.emit()