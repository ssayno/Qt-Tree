from sys import modules
from PyQt5.QtWidgets import QDirModel, QFileSystemModel, QVBoxLayout, QWidget, QTreeView
from qtpy.QtCore import QDir
import os


class TreeWidget(QWidget):

    def __init__(self, parent=None):
        super(TreeWidget, self).__init__(parent=parent)
        self.layout = QVBoxLayout()
        self.setMinimumWidth(300)
        self.setMaximumWidth(600)
        self.setLayout(self.layout)
        self.add_tree()

    def add_tree(self):
        self.dir_tree = QTreeView()
        tree_model = QFileSystemModel()
        user_dir = os.path.expanduser('~')
        tree_model.setRootPath(user_dir)
        self.dir_tree.setModel(tree_model)
        self.dir_tree.setColumnHidden(1, True)
        self.dir_tree.setColumnHidden(2, True)
        self.dir_tree.setColumnHidden(3, True)
        self.dir_tree.setRootIndex(tree_model.index(user_dir))
        self.layout.addWidget(self.dir_tree)
