
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from ui.src.Ui_encryption_window import *
from ui.src.window_utils import error_warning

class EncryptionWindow(QMainWindow):
    change_window_signal = pyqtSignal()
    encrypt_signal = pyqtSignal(dict)
    decrypt_signal = pyqtSignal(dict)


    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_EncryptionWindow()
        self.ui.setupUi(self)

    def init(self) -> None:
        self.ui.generate_button.clicked.connect(self.generate)
        self.ui.decryption_button.clicked.connect(self.change_window)
        self.ui.set_key_check.toggled.connect(self.set_key_setting)
        self.ui.char_button.toggled.connect(self.plain_text_setting)

        self.ui.key_input.setReadOnly(True)
        key_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[01]{8,8}"), self.ui.key_input)
        self.ui.key_input.setValidator(key_validator)

    def set_key_setting(self):
        if self.ui.set_key_check.isChecked():
            self.ui.key_input.setReadOnly(False)
        else:
            self.ui.key_input.setReadOnly(True)

    def plain_text_setting(self):
        choose_mode = self.ui.choose_mode_group.checkedId()
        if choose_mode == -3:
            binary_validator = QtGui.QRegExpValidator(QtCore.QRegExp("[01]+"), self.ui.plain_text_input)
            self.ui.plain_text_input.setValidator(binary_validator)
        else:
            self.ui.plain_text_input.setValidator(None)

    def generate(self) -> None:
        plain_text = self.ui.plain_text_input.text()
        if plain_text == "":
            error_warning("Please enter plain text !  ")
            return
        
        if self.ui.set_key_check.isChecked():
            key = self.ui.key_input.text()
            if key == "":
                error_warning("Please set encryption key !  ")
                return
        else:
            key = ""

        choose_mode = self.ui.choose_mode_group.checkedId()
        if choose_mode == -2:
            mode = "unicode"
        elif choose_mode == -3:
            mode = "binary"
        else:
            error_warning("Please choose input model !  ")
            return
        
        data_dict = {
            "mode": mode,
            "key": key,
            "plain text": plain_text
        }

        self.encrypt_signal.emit()

    def change_window(self):
        self.change_window_signal.emit()