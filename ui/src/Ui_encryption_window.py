# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Jiewo\Folder\Done\2023_fall\intro_of_information_security\simple_des\Simple_DES\ui\encryption_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EncryptionWindow(object):
    def setupUi(self, EncryptionWindow):
        EncryptionWindow.setObjectName("EncryptionWindow")
        EncryptionWindow.resize(800, 428)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EncryptionWindow.sizePolicy().hasHeightForWidth())
        EncryptionWindow.setSizePolicy(sizePolicy)
        EncryptionWindow.setMinimumSize(QtCore.QSize(800, 428))
        EncryptionWindow.setMaximumSize(QtCore.QSize(800, 428))
        EncryptionWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EncryptionWindow.setWindowIcon(icon)
        EncryptionWindow.setIconSize(QtCore.QSize(26, 26))
        EncryptionWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        EncryptionWindow.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(EncryptionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 821, 451))
        self.main_frame.setAutoFillBackground(False)
        self.main_frame.setStyleSheet("QFrame {\n"
"    background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setLineWidth(1)
        self.main_frame.setObjectName("main_frame")
        self.content_frame = QtWidgets.QFrame(self.main_frame)
        self.content_frame.setGeometry(QtCore.QRect(260, 30, 501, 371))
        self.content_frame.setStyleSheet("QLineEdit {\n"
"    border-radius:10px;\n"
"    background-color:rgb(240, 240, 240);\n"
"    padding-left:10px;\n"
"    padding-right:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(240, 240, 240);\n"
"}\n"
"\n"
"#content_frame {\n"
"    border:3px solid rgb(170, 170, 255);\n"
"    border-radius:20px\n"
"}\n"
"\n"
"")
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")
        self.plain_text_input = QtWidgets.QLineEdit(self.content_frame)
        self.plain_text_input.setGeometry(QtCore.QRect(230, 30, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.plain_text_input.setFont(font)
        self.plain_text_input.setStyleSheet("")
        self.plain_text_input.setText("")
        self.plain_text_input.setObjectName("plain_text_input")
        self.key_input = QtWidgets.QLineEdit(self.content_frame)
        self.key_input.setEnabled(True)
        self.key_input.setGeometry(QtCore.QRect(230, 90, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.key_input.setFont(font)
        self.key_input.setStyleSheet("")
        self.key_input.setInputMask("")
        self.key_input.setText("")
        self.key_input.setDragEnabled(False)
        self.key_input.setReadOnly(True)
        self.key_input.setObjectName("key_input")
        self.set_key_check = QtWidgets.QCheckBox(self.content_frame)
        self.set_key_check.setGeometry(QtCore.QRect(40, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.set_key_check.setFont(font)
        self.set_key_check.setObjectName("set_key_check")
        self.encrpyt_text_label = QtWidgets.QLabel(self.content_frame)
        self.encrpyt_text_label.setGeometry(QtCore.QRect(40, 150, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.encrpyt_text_label.setFont(font)
        self.encrpyt_text_label.setObjectName("encrpyt_text_label")
        self.plain_text_label = QtWidgets.QLabel(self.content_frame)
        self.plain_text_label.setGeometry(QtCore.QRect(40, 30, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.plain_text_label.setFont(font)
        self.plain_text_label.setObjectName("plain_text_label")
        self.generate_button = QtWidgets.QPushButton(self.content_frame)
        self.generate_button.setGeometry(QtCore.QRect(140, 310, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.generate_button.setFont(font)
        self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate_button.setMouseTracking(False)
        self.generate_button.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(85, 0, 127);\n"
"    border-radius:18px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color:rgb(170, 170, 255);\n"
"}\n"
"\n"
"")
        self.generate_button.setObjectName("generate_button")
        self.char_button = QtWidgets.QRadioButton(self.content_frame)
        self.char_button.setGeometry(QtCore.QRect(40, 240, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.char_button.setFont(font)
        self.char_button.setObjectName("char_button")
        self.choose_mode_group = QtWidgets.QButtonGroup(EncryptionWindow)
        self.choose_mode_group.setObjectName("choose_mode_group")
        self.choose_mode_group.addButton(self.char_button)
        self.binary_button = QtWidgets.QRadioButton(self.content_frame)
        self.binary_button.setGeometry(QtCore.QRect(40, 200, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.binary_button.setFont(font)
        self.binary_button.setObjectName("binary_button")
        self.choose_mode_group.addButton(self.binary_button)
        self.encrypted_text_input = QtWidgets.QTextEdit(self.content_frame)
        self.encrypted_text_input.setGeometry(QtCore.QRect(230, 150, 241, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.encrypted_text_input.setFont(font)
        self.encrypted_text_input.setStyleSheet("QTextEdit {\n"
"    background-color:rgb(240, 240, 240);\n"
"    border:none;\n"
"    border-radius:10px;\n"
"    padding-left:10px;\n"
"    padding-right:10px;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical {\n"
"    background-color:rgb(170, 170, 255);\n"
"    border-radius:5px\n"
"}")
        self.encrypted_text_input.setReadOnly(True)
        self.encrypted_text_input.setObjectName("encrypted_text_input")
        self.menu_frame = QtWidgets.QFrame(self.main_frame)
        self.menu_frame.setGeometry(QtCore.QRect(30, 30, 211, 371))
        self.menu_frame.setStyleSheet("QPushButton {\n"
"    border-radius:10px;\n"
"    background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color:rgb(210, 213, 255);\n"
"    border-radius:20px\n"
"}\n"
"\n"
"")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.decryption_button = QtWidgets.QPushButton(self.menu_frame)
        self.decryption_button.setGeometry(QtCore.QRect(20, 90, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.decryption_button.setFont(font)
        self.decryption_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decryption_button.setStyleSheet("QPushButton::hover {\n"
"    background-color:rgb(230, 230, 230)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color:rgb(224, 220, 240)\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icon/decryption.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.decryption_button.setIcon(icon1)
        self.decryption_button.setObjectName("decryption_button")
        self.encryption_button = QtWidgets.QPushButton(self.menu_frame)
        self.encryption_button.setGeometry(QtCore.QRect(18, 20, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.encryption_button.setFont(font)
        self.encryption_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.encryption_button.setStyleSheet("background-color:rgb(95, 0, 147);\n"
"color:white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icon/encryption.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encryption_button.setIcon(icon2)
        self.encryption_button.setCheckable(False)
        self.encryption_button.setObjectName("encryption_button")
        self.crack_button = QtWidgets.QPushButton(self.menu_frame)
        self.crack_button.setGeometry(QtCore.QRect(20, 160, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.crack_button.setFont(font)
        self.crack_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crack_button.setStyleSheet("QPushButton::hover {\n"
"    background-color:rgb(230, 230, 230)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color:rgb(224, 220, 240)\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icon/spider.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.crack_button.setIcon(icon3)
        self.crack_button.setObjectName("crack_button")
        EncryptionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EncryptionWindow)
        QtCore.QMetaObject.connectSlotsByName(EncryptionWindow)

    def retranslateUi(self, EncryptionWindow):
        _translate = QtCore.QCoreApplication.translate
        EncryptionWindow.setWindowTitle(_translate("EncryptionWindow", "Simple-DES"))
        self.set_key_check.setText(_translate("EncryptionWindow", "Set Key"))
        self.encrpyt_text_label.setText(_translate("EncryptionWindow", "Encrypted Text"))
        self.plain_text_label.setText(_translate("EncryptionWindow", "Plain Text"))
        self.generate_button.setText(_translate("EncryptionWindow", "Generate"))
        self.char_button.setText(_translate("EncryptionWindow", "string"))
        self.binary_button.setText(_translate("EncryptionWindow", "binary"))
        self.decryption_button.setText(_translate("EncryptionWindow", "  Decryption"))
        self.encryption_button.setText(_translate("EncryptionWindow", "  Encryption"))
        self.crack_button.setText(_translate("EncryptionWindow", "Crack"))
import ui.src.res_rc
