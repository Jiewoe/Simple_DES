import sys
from PyQt5.QtWidgets import QApplication
from ui.src.window_controller import WindowController

app = QApplication(sys.argv)

con = WindowController()
con.init()

sys.exit(app.exec_())