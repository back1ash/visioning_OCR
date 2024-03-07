import sys
import os
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from main import Tesseract


class Ui_mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image = r"visioning_OCR\sample\sample1.png"
        self.setupUi()

    def setupUi(self):
        self.resize(600, 500)
        self.setAcceptDrops(True)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowTitle("Visioning_OCR")

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        label = QLabel(self.centralwidget)
        label.setObjectName("label")
        label.setGeometry(QRect(20, 20, 450, 200))
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy)
        label.setPixmap(QPixmap(self.image))
        label.setScaledContents(True)

        textBrowser = QTextBrowser(self.centralwidget)
        textBrowser.setObjectName("textBrowser")
        textBrowser.setGeometry(QRect(20, 240, 450, 200))
        sizePolicy.setHeightForWidth(textBrowser.sizePolicy().hasHeightForWidth())
        textBrowser.setSizePolicy(sizePolicy)

        fileBtn = QPushButton(self.centralwidget)
        fileBtn.setObjectName("fileSelectButton")
        fileBtn.setGeometry(QRect(500, 100, 75, 23))
        fileBtn.setText("파일 선택")

        copyBtn = QPushButton(self.centralwidget)
        copyBtn.setObjectName("CopyButton")
        copyBtn.setGeometry(QRect(500, 330, 75, 23))
        copyBtn.setText("복사하기")

        self.setCentralWidget(self.centralwidget)
        statusBar = QStatusBar(self)
        statusBar.setObjectName("statusBar")
        self.setStatusBar(statusBar)

        self.setPath = QAction('Set Tesseract Path', self)
        self.setPath.triggered.connect(self.setTesseract)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        self.toolmenu = menubar.addMenu('Tools')
        self.toolmenu.addAction(self.setPath)

        QMetaObject.connectSlotsByName(self)
        
    def findFile(self):
        fname = QFileDialog.getOpenFileName(self, filter='exe File(*.exe) ;; All File(*)')
        return fname[0]
    
    def setTesseract(self):
        path = self.findFile()
        filename = os.path.basename(path)
        if filename != "tesseract.exe":
            QMessageBox.critical(self, '파일 선택 오류', 'tesseract.exe를 선택한게 맞는지 확인해주십시오.')
            return
        tesseract.setPath(path)

    def ocr(self):
        pass


app = QApplication(sys.argv)
tesseract = Tesseract()
window = Ui_mainWindow()
window.show()
sys.exit(app.exec())