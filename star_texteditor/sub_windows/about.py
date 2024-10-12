# -*- coding: utf-8 -*-

import os
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt

from star_texteditor.ui.about import Ui_About


class AboutWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.about_str = """
Star TextEditor
版本: 0.0.1
作者：bland
icon：orange
"""

        self.ui = Ui_About()
        self.ui.setupUi(self)
        self.setWindowTitle("关于")
        self.ui.graphicsView.setFrameStyle(QtWidgets.QGraphicsView.NoFrame)
        self.ui.aboutText.setFrameStyle(QtWidgets.QTextBrowser.NoFrame)
        self.setMaximumSize(self.width(), self.height())

        self.setStyleSheet("background-color: white;")

        scene = QtWidgets.QGraphicsScene()
        resource_path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        pixmap = QtGui.QPixmap(f"{resource_path}/resource/star_mini.jpg")
        scene.addPixmap(pixmap)
        self.ui.graphicsView.setScene(scene)

        self.ui.aboutText.setAlignment(Qt.AlignCenter)
        self.ui.aboutText.append(self.about_str)
