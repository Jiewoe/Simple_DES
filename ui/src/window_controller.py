from ui.src.crack_window import CrackWindow
from ui.src.encryption_window import EncryptionWindow
from encryption.encrypt import Encryptor


class WindowController:
    def __init__(self) -> None:
        self.encryptor = Encryptor()
        self.crack_win = CrackWindow()
        self.encryption_win = EncryptionWindow()
        
        self.crack_win.hide()
        self.encryption_win.show()

    def init(self):
        self.crack_win.init()
        self.encryption_win.init()
        self.encryptor.init()

        self.crack_win.change_window_signal.connect(self.show_encryption_window)
        self.encryption_win.change_window_signal.connect(self.show_crack_window)

        self.encryption_win.generate_signal.connect(self.generate_text)
        self.crack_win.crack_signal.connect(self.crack)

    def show_encryption_window(self, mode: str) -> None:
        self.crack_win.hide()
        self.encryption_win.window_mode_init(mode=mode)
        self.encryption_win.show()

    def show_crack_window(self):
        self.encryption_win.hide()
        self.crack_win.show()

    def generate_text(self, data_dict: dict):
        if data_dict["key"] != "":
            self.encryptor.key_init([int(x) for x in data_dict["key"]])

        if data_dict["mode"] == EncryptionWindow.ENCRYPT:
            if data_dict["codeset"] == "binary":
                text = self.encryptor.encrypt_binary([int(x) for x in data_dict["text"]], is_decrypt=False)
                text = ''.join(map(str, text))
            else:
                text = self.encryptor.encrypt_string(data_dict["text"], is_decrypt=False)
        else:
            if data_dict["codeset"] == "binary":
                text = self.encryptor.encrypt_binary([int(x) for x in data_dict["text"]], is_decrypt=True)
                text = ''.join(map(str, text))
            else:
                text = self.encryptor.encrypt_string(data_dict["text"], is_decrypt=True)

        self.encryption_win.show_result(text)

    def crack(self, data_dict: dict):
        pass