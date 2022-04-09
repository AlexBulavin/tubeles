# -*- coding: utf-8 -*-
# Tto create virtual environment run:
# $virtualenv {name of virtual environment}
# Example:
# iMac-Alex:tubeles alex$ virtualenv venv
# To activate venv run next code:
# iMac-Alex:tubeles alex$ source venv/bin/activate

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
import threading
from processor import Processor
import threading
import requests
# import init
import sys
import os
import untitled


class ExampleApp(QtWidgets.QMainWindow, untitled.Ui_MainWindow):

    def __init__(self):  # Main Processor ui class...
        super().__init__()

        self.setupUi(self)
        # Обработчики кнопок
        self.btn_select.clicked.connect(self.select)
        self.btn_check.clicked.connect(self.check)
        self.btn_download.clicked.connect(self.download)

    def select(self):  # Select directory metod to save file...

        self.file = QtWidgets.QFileDialog.getExistingDirectory(self, "Select file")
        if self.file != "":
            self.line_save.setText(self.file)
        else:
            pass

    def check(self):  # Check is video available...
        self.title = self.line_title.text()
        self.url = self.line_url.text()
        self.path = self.line_save.text()
        self.th = Processor(self.title, self.url, self.path)
        threading.Thread(target=self.th.running).start()
        self.th.length.connect(self.append)

    def download(self):  # Start download video method...
        self.title = self.line_title.text()
        self.url = self.line_url.text()
        self.path = self.line_save.text()
        self.th = Processor(self.title, self.url, self.path)
        threading.Thread(target=self.th.download).start()
        self.th.receiv.connect(self.progress)

    def append(self, title, description, thumbnail):  # Start stream method...
        # This method to present actual information
        if title != "":
            self.line_title.setText(title)
            self.text_desc.setPlainText(description)
            image = QImage()
            image.loadFromData(requests.get(thumbnail).content)
            self.label_prew.setPixmap(QPixmap(image))
            self.label_prew.show()
        else:
            self.msg()

    def progress(self, size):  # Progress bar method...
        self.progressBar.setValue(size)

    def msg(self):  # Message method...
        # To inform user about what is going on
        dialog = QMessageBox()
        dialog.setText("Проверьте правильность ссылки!")
        dialog.setInformativeText("<i>Скопируйте ссылку на видео из строки браузера...</i>")
        dialog.setWindowTitle("Видео недоступно")
        dialog.setStandardButtons(QMessageBox.Cancel)
        dialog.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        dialog.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
