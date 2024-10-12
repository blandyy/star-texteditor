# -*- coding: utf-8 -*-
from PySide6 import QtWidgets, QtGui

from star_texteditor.ui.search import Ui_Search


class SearchWindow(QtWidgets.QWidget):
    def __init__(self, editor):
        super().__init__()
        self._code_editor = editor
        self.ui = Ui_Search()
        self.ui.setupUi(self)
        self.setWindowTitle("查找文本")
        self.setMaximumSize(self.width(), self.height())
        self.ui.search_button.clicked.connect(self.search_next)

    def search_next(self):
        search_text = self.ui.search_field.text()
        if search_text:
            found = self._code_editor.find(search_text)
            if not found:
                # 如果没有找到，将光标移动到文本的开始位置，然后再次查找
                self._code_editor.moveCursor(QtGui.QTextCursor.Start)
                self._code_editor.find(search_text)
