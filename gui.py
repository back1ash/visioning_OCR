import sys
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from main import Tesseract




class Ui_mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(600, 500)
        self.setAcceptDrops(True)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(20, 20, 450, 200))
        # sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy = QSizePolicy()
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QPixmap(r"/sample/sample1.png"))
        self.label.setScaledContents(True)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setGeometry(QRect(20, 240, 450, 200))
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.fileBtn = QPushButton(self.centralwidget)
        self.fileBtn.setObjectName("fileSelectButton")
        self.fileBtn.setGeometry(QRect(500, 100, 75, 23))
        self.copyBtn = QPushButton(self.centralwidget)
        self.copyBtn.setObjectName("DuplicateButton")
        self.copyBtn.setGeometry(QRect(500, 330, 75, 23))
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", "Visioning_OCR", None))
        self.label.setText("")
        self.fileBtn.setText(QCoreApplication.translate("mainWindow", u"\ud30c\uc77c \uc120\ud0dd", None))
        self.copyBtn.setText(QCoreApplication.translate("mainWindow", u"\ubcf5\uc0ac\ud558\uae30", None))
    # retranslateUi

app = QApplication(sys.argv)
window = Ui_mainWindow()
window.show()
sys.exit(app.exec())