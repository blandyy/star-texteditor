# -*- coding: utf-8 -*-

import os

from PySide6 import QtCore, QtGui, QtWidgets

from star_texteditor.code_editor import CodeEditor
from star_texteditor.config import Config
from star_texteditor.sub_windows.about import AboutWindow
from star_texteditor.sub_windows.replace import ReplacehWindow
from star_texteditor.sub_windows.search import SearchWindow
from star_texteditor.ui.star_ui import Ui_MainWindow
from star_texteditor.utils import detect_encoding


class StarWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 初始化ui文件中的ui
        self.file_path = ""
        self.file_name = "未命名"
        self.file_type = ""
        self.encoding = ""
        self.default_encoding = "utf-8"
        self.is_save = True

        self.code_editor = CodeEditor()

        self.code_editor.setFrameStyle(
            QtWidgets.QPlainTextEdit.NoFrame
        )  # 去掉文本框边框

        # 设置字体
        font = QtGui.QFont("Arial", 12)
        self.code_editor.setFont(font)  # 为plainTextEdit设置字体

        self.setCentralWidget(self.code_editor)

        # 设置打开文件异步加载定时器
        self.open_file_timer = QtCore.QTimer()
        self.open_file_timer.timeout.connect(self.load_chunk)

        # 增加状态栏字符串数量label
        self.ui.statusbar_charsnum = QtWidgets.QLabel(f"字符数: 0")
        self.ui.statusbar.addPermanentWidget(self.ui.statusbar_charsnum)

        # 增加状态栏光标位置label
        self.ui.statusbar_cursor = QtWidgets.QLabel(f"光标位置: 1:1")
        self.ui.statusbar.addPermanentWidget(self.ui.statusbar_cursor)

        # 增加状态栏文本编码label
        self.ui.statusbar_encoding = QtWidgets.QLabel(
            f"文件编码: {self.default_encoding}"
        )
        self.ui.statusbar.addPermanentWidget(self.ui.statusbar_encoding)

        self.code_editor.cursorPositionChanged.connect(
            self.on_cursor_changed
        )  # 光标位置更改事件绑定方法

        self.ui.action_open.setShortcut("Ctrl+O")
        self.ui.action_open.triggered.connect(self.open_file_dialog)  # 打开按钮绑定方法

        self.ui.action_save.setShortcut("Ctrl+S")
        self.ui.action_save.triggered.connect(self.save_file)  # 保存按钮绑定方法

        self.ui.action_save_as.setShortcut("Ctrl+Shift+S")
        self.ui.action_save_as.triggered.connect(
            self.save_as_file_dialog
        )  # 另存为按钮绑定方法

        self.code_editor.textChanged.connect(self.on_text_changed)

        self.code_editor.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.ui.action_wrap.setText(
            QtCore.QCoreApplication.translate("MainWindow", "开启自动换行", None)
        )
        self.ui.action_wrap.triggered.connect(self.set_wrap)  # 自动换行绑定方法

        self.ui.action_about.triggered.connect(self.show_about)  # 显示关于信息

        self.ui.action_search.setShortcut("Ctrl+F")
        self.ui.action_search.triggered.connect(self.show_search)  # 显示查找对话框

        self.ui.action_replace.setShortcut("Ctrl+R")
        self.ui.action_replace.triggered.connect(self.show_replace)  # 显示替换对话框

        self.code_editor.keyPressEvent = self.on_key_press_event  # 重写键盘监听

    def closeEvent(self, event):
        if not self.is_save:
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setWindowTitle("确认")
            msg_box.setText("文件未保存，是否保存更改？")
            save_button = msg_box.addButton("保存", QtWidgets.QMessageBox.AcceptRole)
            dont_save_button = msg_box.addButton(
                "不保存", QtWidgets.QMessageBox.DestructiveRole
            )
            cancel_button = msg_box.addButton("取消", QtWidgets.QMessageBox.RejectRole)
            msg_box.exec()

            if msg_box.clickedButton() == save_button:
                self.save_file()
                event.accept()
            elif msg_box.clickedButton() == dont_save_button:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def open_file_dialog(self):
        pwd = os.path.dirname(os.getcwd())
        cur_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open File",
            pwd,
            "All Files (*.*)",
        )
        if not cur_file_path:
            return
        self.file_path = cur_file_path
        self.encoding = detect_encoding(self.file_path)
        # 创建并显示进度对话框
        self.open_progress_dialog = QtWidgets.QProgressDialog(
            "文件加载中...", None, 0, 100, self
        )
        self.open_progress_dialog.setWindowTitle("加载中")
        self.open_progress_dialog.setWindowModality(
            QtCore.Qt.WindowModality.ApplicationModal
        )
        self.open_progress_dialog.setAutoClose(False)
        self.open_progress_dialog.setMinimumDuration(0)
        self.open_progress_dialog.show()
        self.read_file_obj = open(self.file_path, "r", encoding=self.encoding)
        self.read_file_size = os.path.getsize(self.file_path)
        self.code_editor.setPlainText("")  # 清空现有内容
        self.open_progress_dialog.setValue(10)
        self.open_file_timer.start(50)  # 立即开始分块加载
        self.file_type = self.file_path.split(".")[-1]
        self.update_statusbar_encoding()
        self.update_window_title_no_save()

    def load_chunk(self):
        if self.read_file_obj:
            _text_chunk = self.read_file_obj.read(Config.max_chunk_size)
            if _text_chunk:
                self.open_progress_dialog.setValue(50)
                cursor = self.code_editor.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText(_text_chunk)
            else:
                self.open_progress_dialog.setValue(90)
                self.open_file_timer.stop()  # 停止计时器，因为文件已读取完毕
                self.read_file_obj.close()
                self.read_file_obj = None
                if self.read_file_size >= Config.max_handle_file_size:
                    # 过大文件使用自动换行
                    self.code_editor.setLineWrapMode(
                        QtWidgets.QPlainTextEdit.WidgetWidth
                    )
                    self.ui.action_wrap.setText(
                        QtCore.QCoreApplication.translate(
                            "MainWindow", "关闭自动换行", None
                        )
                    )
                self.code_editor.set_highlighter_by_file_type(
                    "", self.file_type, self.file_path
                )  # 设置高亮
                self.open_progress_dialog.setValue(99)
                # 将光标移动到最前面
                self.code_editor.moveCursor(QtGui.QTextCursor.MoveOperation.Start)
                # 关闭进度对话框
                if self.open_progress_dialog:
                    self.open_progress_dialog.close()
                    self.open_progress_dialog = None
                print("finish")

    def save_file(self):
        if not self.file_path:
            cur_file_path = self.save_as_file_dialog(is_path=True)
            if not cur_file_path:
                return
            else:
                self.file_path = cur_file_path
        with open(
            self.file_path, "w", encoding=(self.encoding or self.default_encoding)
        ) as wf:
            wf.write(self.code_editor.toPlainText())
        self.update_window_title()
        self.is_save = True

    def save_as_file_dialog(self, is_path: False):
        pwd = os.path.dirname(os.getcwd())
        cur_file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save As File",
            f"{pwd}/{self.file_name}",
            "All Files (*.*)",
        )
        if not cur_file_path:
            return ""
        if is_path:
            return cur_file_path
        self.file_path = cur_file_path
        with open(
            self.file_path, "w", encoding=(self.encoding or self.default_encoding)
        ) as wf:
            wf.write(self.code_editor.toPlainText())
        # 设置高亮
        cur_file_type = self.file_path.split(".")[-1]
        self.code_editor.set_highlighter_by_file_type(
            self.file_type, cur_file_type, self.file_path
        )
        self.file_type = cur_file_type
        self.update_window_title_no_save()

    def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def show_search(self):
        self.search_window = SearchWindow(self.code_editor)
        self.search_window.show()

    def show_replace(self):
        self.replace_window = ReplacehWindow(self.code_editor)
        self.replace_window.show()

    def set_wrap(self):
        if self.code_editor.lineWrapMode() == QtWidgets.QPlainTextEdit.WidgetWidth:
            self.code_editor.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
            self.ui.action_wrap.setText(
                QtCore.QCoreApplication.translate("MainWindow", "开启自动换行", None)
            )
        else:
            self.code_editor.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
            self.ui.action_wrap.setText(
                QtCore.QCoreApplication.translate("MainWindow", "关闭自动换行", None)
            )

    def update_window_title(self):
        if self.file_path:
            self.file_name = os.path.basename(self.file_path)
        self.setWindowTitle(f"{self.file_name} - {Config.app_name}")

    def update_statusbar_encoding(self):
        self.ui.statusbar_encoding.setText(f"文件编码: {self.encoding}")

    def on_text_changed(self):
        if not self.code_editor._highlighter.highlighting:
            self.update_window_title_no_save()
        chars_num = len(self.code_editor.toPlainText().replace("\n", ""))
        self.ui.statusbar_charsnum.setText(f"字符数: {chars_num}")

    def on_cursor_changed(self):
        cursor = self.code_editor.textCursor()
        line = cursor.blockNumber() + 1  # 行号
        col = cursor.columnNumber() + 1  # 列号
        self.ui.statusbar_cursor.setText(f"光标位置: {line}:{col}")

    def update_window_title_no_save(self):
        if self.file_path:
            self.file_name = os.path.basename(self.file_path)
        self.setWindowTitle(f"* {self.file_name} - {Config.app_name}")
        self.is_save = False

    def on_key_press_event(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            # 获取当前行的缩进
            cursor = self.code_editor.textCursor()
            current_line = cursor.block().text()
            leading_spaces = len(current_line) - len(current_line.lstrip(" "))

            # 创建一个与当前行缩进相同的空白字符串
            indent = " " * leading_spaces

            # 在新行中插入缩进
            cursor.insertText("\n" + indent)
            self.code_editor.setTextCursor(cursor)
        elif event.key() == QtCore.Qt.Key_Tab:
            # 捕获 Tab 键，将其替换为四个空格
            cursor = self.code_editor.textCursor()
            cursor.insertText(" " * 4)
        else:
            # 其他按键事件正常处理
            QtWidgets.QPlainTextEdit.keyPressEvent(self.code_editor, event)
