#!/usr/bin/env python3
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImageReader, QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QSplitter, QWidget, QGridLayout
import sys
import qdarkstyle
from Main_Widgets.left_tree import TreeWidget
from Main_Widgets.right_widget import Right_Widget


class Tree(QMainWindow):
    def __init__(self):
        super(Tree, self).__init__()
        self.resize(1000, 600)
        self.central_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        # add widget
        self.add_widget()
        # connect slot signal with func
        self.bind_slot_and_func()

    def add_widget(self):
        #
        splitter_1 = QSplitter()
        self.left_ = TreeWidget(self)
        splitter_1.addWidget(self.left_)
        #self.main_layout.addWidget(splitter_1)
        #
        splitter_2 = QSplitter()
        splitter_2.addWidget(splitter_1)
        self.right_ = Right_Widget()
        self.right_.setMinimumSize(800, 600)
        splitter_2.addWidget(self.right_)
        self.main_layout.addWidget(splitter_2)

    def bind_slot_and_func(self):
        self.left_.dir_tree.doubleClicked.connect(self.get_filetree_doubleClicked_item)

    def get_filetree_doubleClicked_item(self, index):
        file_path = self.left_.dir_tree.model().filePath(index)
        if file_path.endswith('.py'):
            self.right_.text_edit.clear()
            with open(file_path, 'r', encoding='U8') as f:
                text_ = f.read()
            self.right_.image_label.setVisible(False)
            self.right_.text_edit.append(text_)
            self.right_.text_edit.setVisible(True)
        elif file_path.endswith(('.png', '.jpg', 'jpeg')):
            image = QImageReader(file_path)
            scale = self.right_.width() / image.size().width()
            height = int(image.size().height() * scale)
            image.setScaledSize(QSize(self.right_.width(), height))
            pixmap = QPixmap(image.read())
            self.right_.text_edit.setVisible(False)
            self.right_.image_label.setPixmap(pixmap)
            self.right_.image_label.setVisible(True)
            print(file_path)
        elif file_path.endswith(('html', 'htm')):
            print(file_path)
            with open(file_path, 'r', encoding='U8') as f:
                html_code = f.read()
            self.right_.text_edit.clear()
            self.right_.text_edit.setVisible(True)
            self.right_.text_edit.append(html_code)
        elif file_path.endswith(('mp4', 'mkv')):
            print(f'{file_path} is a video')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # set qdarkstyle sheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    tree = Tree()
    tree.show()
    sys.exit(app.exec_())
