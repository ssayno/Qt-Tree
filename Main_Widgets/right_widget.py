#!/usr/bin/env python3
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextBlock
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QTextEdit, QWidget


class Right_Widget(QWidget):
    def __init__(self):
        super(Right_Widget, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        #
        temp_button = QPushButton('aa')
        self.text_edit = QTextEdit()
        self.text_edit.setVisible(False)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setVisible(False)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.text_edit)
