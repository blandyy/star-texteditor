# -*- coding: utf-8 -*-
import os
import sys

from PySide6 import QtWidgets, QtGui

from star_texteditor.base import StarWindow
from star_texteditor.config import Config

app = QtWidgets.QApplication(sys.argv)  # 创建APP，将运行脚本时（可能的）的其他参数传给Qt以初始化
window = StarWindow()
# 设置标题
window.setWindowTitle(f"未命名 - {Config.app_name}")
resource_path = os.path.dirname(os.path.abspath(__file__))
window.setWindowIcon(QtGui.QIcon(f"{resource_path}/resource/favicon.ico"))
# 设置窗口大小，单位为像素
# window.setMaximumSize(window.width(), window.height())
window.show()  # 显示窗口
sys.exit(app.exec())  # 正常退出APP：app.exec()关闭app，sys.exit()退出进程
