from ui.src.decryption_window import DecryptionWindow
from ui.src.encryption_window import EncryptionWindow
from encryption.encrypt import Encryptor


class WindowController:
    def __init__(self) -> None:
        self.encryptor = Encryptor()
        self.decryption_win = DecryptionWindow()
        self.encryption_win = EncryptionWindow()
        
        self.decryption_win.hide()
        self.encryption_win.show()

    def init(self):
        self.decryption_win.init()
        self.encryption_win.init()

        self.decryption_win.change_window_signal.connect(self.show_encryption_window)
        self.encryption_win.change_window_signal.connect(self.show_decryption_window)

        self.encryption_win.encrypt_signal.connect(self.encrypt)
        self.encryption_win.decrypt_signal.connect(self.decrypt)
        self.decryption_win.crack_signal.connect(self.crack)

    def show_encryption_window(self):
        self.decryption_win.hide()
        self.encryption_win.show()

    def show_decryption_window(self):
        self.encryption_win.hide()
        self.decryption_win.show()

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def crack(self):
        pass