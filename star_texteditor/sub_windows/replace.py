# -*- coding: utf-8 -*-
from PySide6 import QtWidgets, QtGui

from star_texteditor.ui.replace import Ui_Replace


class ReplacehWindow(QtWidgets.QWidget):
    def __init__(self, editor):
        super().__init__()
        self._code_editor = editor
        self.ui = Ui_Replace()
        self.ui.setupUi(self)
        self.setWindowTitle("替换文本")
        self.setMaximumSize(self.width(), self.height())

        self.ui.butten_find.clicked.connect(self.search_next)
        self.ui.button_replace.clicked.connect(self.replace_text)
        self.ui.button_replace_all.clicked.connect(self.replace_text_all)

    def search_next(self):
        text_to_find = self.ui.search_text.text()
        if text_to_find:
            found = self._code_editor.find(text_to_find)
            if not found:
                # 如果没有找到，将光标移动到文本的开始位置，然后再次查找
                self._code_editor.moveCursor(QtGui.QTextCursor.Start)
                self._code_editor.find(text_to_find)

    def replace_text(self):
        text_to_find = self.ui.search_text.text()
        text_to_replace = self.ui.replace_text.text()
        cursor = self._code_editor.textCursor()
        if cursor.hasSelection():
            selected_text = cursor.selectedText()
            if selected_text == text_to_find:
                cursor.insertText(text_to_replace)
        elif self._code_editor.find(text_to_find):
            cursor = self._code_editor.textCursor()
            cursor.insertText(text_to_replace)

    def replace_text_all(self):
        text_to_find = self.ui.search_text.text()
        text_to_replace = self.ui.replace_text.text()
        self._code_editor.moveCursor(QtGui.QTextCursor.Start)
        while self._code_editor.find(text_to_find):
            cursor = self._code_editor.textCursor()
            cursor.insertText(text_to_replace)
