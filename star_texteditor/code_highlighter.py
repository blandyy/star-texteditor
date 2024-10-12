# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt, QRegularExpression
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont


class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.highlighting = False

        # 定义 Python 关键词的格式
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.darkBlue)
        keyword_format.setFontWeight(QFont.Bold)

        # 定义 Python 字符串的格式
        string_format = QTextCharFormat()
        string_format.setForeground(Qt.darkRed)

        # 定义 Python 注释的格式
        comment_format = QTextCharFormat()
        comment_format.setForeground(Qt.gray)

        # 定义 Python 数字的格式
        number_format = QTextCharFormat()
        number_format.setForeground(Qt.darkMagenta)

        # 定义 Python 特殊符号的格式
        symbol_format = QTextCharFormat()
        symbol_format.setForeground(Qt.darkGray)

        # 定义 Python 关键词的正则表达式
        self.highlighting_rules = [
            (
                QRegularExpression(
                    "\\b(and|as|assert|break|class|continue|def|del|elif|else|except|"
                    "False|finally|for|from|global|if|import|in|is|lambda|None|nonlocal|"
                    "not|or|pass|raise|return|True|try|while|with|yield)\\b"
                ),
                keyword_format,
            ),
            (QRegularExpression("[\"'].*?[\"']"), string_format),
            (QRegularExpression("#.*?$"), comment_format),
            (QRegularExpression("\\b\\d+\\.?\\d*\\b"), number_format),
            (QRegularExpression("[+\\-*/%=<>(){}\\[\\]:;,.]"), symbol_format),
        ]

    def highlightBlock(self, text: str) -> None:
        self.highlighting = True
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)
        self.highlighting = False


class JsonHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting = False

        # 定义 JSON 关键词和值的格式
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.darkBlue)
        keyword_format.setFontWeight(QFont.Bold)

        value_format = QTextCharFormat()
        value_format.setForeground(Qt.darkGreen)

        # 定义 JSON 字符串的格式
        string_format = QTextCharFormat()
        string_format.setForeground(Qt.darkRed)

        # 定义 JSON 注释的格式
        comment_format = QTextCharFormat()
        comment_format.setForeground(Qt.gray)

        # 定义 JSON 数字的格式
        number_format = QTextCharFormat()
        number_format.setForeground(Qt.darkMagenta)

        # 定义 JSON 特殊符号的格式
        symbol_format = QTextCharFormat()
        symbol_format.setForeground(Qt.darkGray)

        # 定义 JSON 关键词和值的正则表达式
        self.highlighting_rules = [
            (QRegularExpression("\\b(true|false|null)\\b"), keyword_format),
            (QRegularExpression('"[^"\\n]*"'), string_format),
            (QRegularExpression("//[^\n]*"), comment_format),
            (QRegularExpression("\\b-?\\d+\\.?\\d*\\b"), number_format),
            (QRegularExpression("[\\[\\]\\{\\}\\:,]"), symbol_format),
        ]

    def highlightBlock(self, text: str) -> None:
        self.highlighting = True
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)
        self.highlighting = False


class HtmlHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting = False

        # 定义 HTML 标签的格式
        tag_format = QTextCharFormat()
        tag_format.setForeground(Qt.darkBlue)
        tag_format.setFontWeight(QFont.Bold)

        # 定义 HTML 属性的格式
        attribute_format = QTextCharFormat()
        attribute_format.setForeground(Qt.darkMagenta)

        # 定义 HTML 字符串的格式
        string_format = QTextCharFormat()
        string_format.setForeground(Qt.darkRed)

        # 定义 HTML 注释的格式
        comment_format = QTextCharFormat()
        comment_format.setForeground(Qt.gray)

        # 定义 HTML 标签的正则表达式
        self.highlighting_rules = [
            (QRegularExpression("<[a-zA-Z0-9\\-]+"), tag_format),
            (QRegularExpression("[a-zA-Z0-9\\-]+(?=\\s*=\\s*[\"'])"), attribute_format),
            (QRegularExpression("([\"']).*?\\1"), string_format),
            (QRegularExpression("<!--.*?-->"), comment_format),
        ]

    def highlightBlock(self, text: str) -> None:
        self.highlighting = True
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)
        self.highlighting = False


class JsHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting = False
        # 定义 JS 关键词的格式
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.darkBlue)
        keyword_format.setFontWeight(QFont.Bold)

        # 定义 JS 字符串的格式
        string_format = QTextCharFormat()
        string_format.setForeground(Qt.darkRed)

        # 定义 JS 注释的格式
        comment_format = QTextCharFormat()
        comment_format.setForeground(Qt.gray)

        # 定义 JS 数字的格式
        number_format = QTextCharFormat()
        number_format.setForeground(Qt.darkMagenta)

        # 定义 JS 特殊符号的格式
        symbol_format = QTextCharFormat()
        symbol_format.setForeground(Qt.darkGray)

        # 定义 JS 关键词的正则表达式
        self.highlighting_rules = [
            (
                QRegularExpression(
                    "\\b(break|case|catch|class|const|continue|debugger|default|delete|do|else|export|"
                    "extends|finally|for|function|if|import|in|instanceof|new|return|super|switch|this|"
                    "throw|try|typeof|var|void|while|with|yield)\\b"
                ),
                keyword_format,
            ),
            (QRegularExpression("([\"']).*?\\1"), string_format),
            (QRegularExpression("//.*?$|/\\*.*?\\*/"), comment_format),
            (QRegularExpression("\\b\\d+\\.?\\d*\\b"), number_format),
            (QRegularExpression("[+\\-*/%=<>(){}\\[\\]:;,.]"), symbol_format),
        ]

    def highlightBlock(self, text: str) -> None:
        self.highlighting = True
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)
        self.highlighting = False


class NoneHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        QSyntaxHighlighter.__init__(self, parent)
        self.highlighting = False


# https://doc.qt.io/qtforpython-6/examples/example_widgets_richtext_syntaxhighlighter.html
