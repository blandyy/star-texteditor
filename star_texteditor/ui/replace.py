# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'replace.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Replace(object):
    def setupUi(self, Replace):
        if not Replace.objectName():
            Replace.setObjectName(u"Replace")
        Replace.resize(400, 200)
        self.verticalLayoutWidget = QWidget(Replace)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 439, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.search_text = QLineEdit(self.verticalLayoutWidget)
        self.search_text.setObjectName(u"search_text")

        self.horizontalLayout.addWidget(self.search_text)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.replace_text = QLineEdit(self.verticalLayoutWidget)
        self.replace_text.setObjectName(u"replace_text")

        self.horizontalLayout_4.addWidget(self.replace_text)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(100, -1, 100, -1)
        self.butten_find = QPushButton(self.verticalLayoutWidget)
        self.butten_find.setObjectName(u"butten_find")

        self.horizontalLayout_6.addWidget(self.butten_find)

        self.button_replace = QPushButton(self.verticalLayoutWidget)
        self.button_replace.setObjectName(u"button_replace")

        self.horizontalLayout_6.addWidget(self.button_replace)

        self.button_replace_all = QPushButton(self.verticalLayoutWidget)
        self.button_replace_all.setObjectName(u"button_replace_all")

        self.horizontalLayout_6.addWidget(self.button_replace_all)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.retranslateUi(Replace)

        QMetaObject.connectSlotsByName(Replace)
    # setupUi

    def retranslateUi(self, Replace):
        Replace.setWindowTitle(QCoreApplication.translate("Replace", u"Form", None))
        self.label.setText(QCoreApplication.translate("Replace", u"\u67e5\u627e\u6587\u672c:", None))
        self.label_2.setText(QCoreApplication.translate("Replace", u"\u66ff\u6362\u6587\u672c:", None))
        self.butten_find.setText(QCoreApplication.translate("Replace", u"\u67e5\u627e", None))
        self.button_replace.setText(QCoreApplication.translate("Replace", u"\u66ff\u6362", None))
        self.button_replace_all.setText(QCoreApplication.translate("Replace", u"\u5168\u90e8\u66ff\u6362", None))
    # retranslateUi

