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
        self.text = "Tesseract sample"
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
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(20, 20, 450, 200))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QPixmap(self.image))
        self.label.setScaledContents(True)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setGeometry(QRect(20, 240, 450, 200))
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setText(self.text)

        fileBtn = QPushButton(self.centralwidget)
        fileBtn.setObjectName("fileSelectButton")
        fileBtn.setGeometry(QRect(500, 100, 75, 23))
        fileBtn.setText("파일 선택")
        fileBtn.clicked.connect(self.redraw)

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
        fname = QFileDialog.getOpenFileName(self, filter='All File(*) ;; exe File(*.exe) ;; bmp File(*.bmp) ;; jpge File(*.jpge) ;; png File(*.png)')
        return fname[0]
    
    def redraw(self):
        formats = [".bmp", ".jpge", ".png"]

        path = self.findFile()
        format = os.path.splitext(path)[1]
        if format not in formats:
            QMessageBox.critical(self, '파일 선택 오류', '.bmp | .jpge | .png 확장자만 지원합니다.')
            return
        self.image = r"{}".format(path)
        self.label.setPixmap(QPixmap(self.image))
        # self.ocr(path)
        
    
    def setTesseract(self):
        path = self.findFile()
        filename = os.path.basename(path)
        if filename != "tesseract.exe":
            QMessageBox.critical(self, '파일 선택 오류', 'tesseract.exe를 선택한게 맞는지 확인해주십시오.')
            return
        print(path)
        tesseract.setPath(path)

    # def ocr(self, path):
    #     self.text = tesseract.translate(path)
    #     self.textBrowser.setText = self.text
    #     print(self.text)
        

tesseract = Tesseract()
app = QApplication(sys.argv)
window = Ui_mainWindow()
window.show()
sys.exit(app.exec())